import numpy as np
import matplotlib.pyplot as plt
from numba import njit


def probability(x):
    return np.sqrt(2 / np.pi) * x**2 * np.exp(-x**2 / 2)


x = np.linspace(0, 5, 300)

pdf = probability(x)


def metropolis(N, x0=1.0, seed=42):
    rng = np.random.default_rng(seed)

    samples = np.zeros(N)
    samples[0] = x0

    accepted = 0

    for i in range(1, N):
        x = samples[i-1]

        x_new = abs(rng.normal(0, 1))

        alpha = min(1.0, (x_new/x)**2)

        if rng.random() < alpha:
            samples[i] = x_new
            accepted += 1
        else:
            samples[i] = x

    acceptance_rate = accepted / (N-1)

    return samples, acceptance_rate


N = 100000

samples, acceptance = metropolis(N)

samples = samples[10000:]


def statistics(samples, blocksize=1000):
    N = len(samples)
    n_blocks = N // blocksize

    data = samples[:n_blocks * blocksize]
    blocks = data.reshape(n_blocks, blocksize)

    mean = np.mean(data)
    var_data = np.var(data)

    block_means = np.mean(blocks)

    means_error = np.std(blocks) / np.sqrt(n_blocks)

    squared_deviation = (blocks - mean)**2
    block_second_moment = np.mean(squared_deviation)

    variance_error = np.std(block_second_moment) / np.sqrt(n_blocks)

    return mean, means_error, var_data, variance_error


mean, mean_error, variance, var_error = statistics(samples)


exact_mean = 2 * np.sqrt(2 / np.pi)
exact_var = (3*np.pi - 8) / np.pi

print(f"MEAN : {mean:.5f} $\pm$ {mean_error:.5f}")
print(f"EXACT MEAN : {exact_mean:.5f}")

print(f"VARIANCE : {variance:.5f} $\pm$ {var_error:.5f}")
print(f"EXACT VARIANCE : {exact_var:.5f}")

plt.plot(x, pdf)
plt.hist(samples, bins=70, color="green", edgecolor="black", density=True)
plt.xlabel("x")
plt.ylabel("probability density")
plt.show()
