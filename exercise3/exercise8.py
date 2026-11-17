import numpy as np
import matplotlib.pyplot as plt


def probability(x):
    if x <= 0:
        return 0

    return np.sqrt(2 / np.pi) * x**2 * np.exp(-x**2 / 2)


def metropolis(N, sigma, x0=1.0):
    samples = np.zeros(N)
    samples[0] = x0

    accepted = 0

    for i in range(1, N):
        x = samples[i-1]

        x_new = np.random.normal(0, sigma)

        if x_new > 0:
            ratio = probability(x_new) / probability(x)
            alpha = min(1, ratio)

        else:
            alpha = 0.0

        if np.random.random() < alpha:
            samples[i] = x_new
            accepted += 1

        else:
            samples[i] = x

        acceptance_rate = accepted / (N-1)

    return samples, acceptance_rate


N = 100_000
acceptance_rates = []

sigma_values = np.linspace(0.1, 5, 30)

for sigma in sigma_values:
    samples, rates = metropolis(N, sigma)
    acceptance_rates.append(rates)


plt.scatter(sigma_values, acceptance_rates)
plt.xlabel(r"$\sigma$")
plt.ylabel("Acceptance rate")
plt.show()


def statistics_blocking(samples, block_size=1000):
    n_blocks = len(samples) // block_size

    blocks = samples[:n_blocks*block_size].reshape(n_blocks, block_size)

    block_means = np.mean(blocks)
    block_variance = np.var(blocks)

    mean = np.mean(samples)
    variance = np.var(samples)

    mean_error = np.std(block_means) / np.sqrt(n_blocks)
    variance_error = np.std(block_variance) / np.sqrt(n_blocks)

    return mean, variance, mean_error, variance_error


samples = samples[10000:]

mean, variance, mean_error, variance_error = statistics_blocking(samples)

exact_mean = 2 * np.sqrt(2 / np.pi)
exact_var = (3 * np.pi - 8) / np.pi

print(f"MEAN : {mean:.6f} $\pm$ {mean_error:6f}")
print(f"EXACT : {exact_mean:.6f}")
print(f"VARIANCE : {variance:.6f} $\pm$ {variance_error:.6f}")
print(f"EXACT : {exact_var:.6f}")


x = np.linspace(0, 5, 500)
pdf = np.sqrt(2 / np.pi) * x**2 * np.exp(-x**2 / 2)

plt.hist(samples, bins=70, color="green", edgecolor="black", density=True)
plt.plot(x, pdf)
plt.xlabel("x")
plt.ylabel("probability")
plt.show()


def metropolis_hastings(N, sigma, drift=0.5, x0=1.0):
    samples = np.zeros(N)
    samples[0] = x0

    accepted = 0

    for i in range(1, N):
        x = samples[i-1]

        x_new = np.random.normal(0, sigma)

        if x_new > 0:
            ratio = probability(x_new) / probability(x)
            correction = np.exp(-2*drift*(x_new - x)/sigma**2)
            alpha = min(1, ratio * correction)

        else:
            alpha = 0.0

        if np.random.random() < alpha:
            samples[i] = x_new
            accepted += 1

        else:
            samples[i] = x

        acceptance_rate = accepted / (N-1)

    return samples, acceptance_rate


acceptance = []

for sigma in sigma_values:
    samples_h, rates = metropolis_hastings(N, sigma)
    acceptance.append(rates)


samples_h = samples_h[10000:]

plt.plot(x, pdf, color="orange")
plt.hist(samples_h, bins=70, color="blue", edgecolor="black", density=True)
plt.show()


def autocorrelation(samples):
    x = np.asarray(samples, dtype=float)
    x = x - np.mean(x)
    N = len(x)

    fft = np.fft.rfft(x, n=2 * N)
    acf = np.fft.irfft(fft * np.conjugate(fft))[:N]

    acf /= np.arange(N, 0, -1)
    acf /= acf[0]

    return acf


def autocorrelation_time(samples, window=5):
    acf = autocorrelation(samples)

    # Self-consistent window estimate
    tau = 0.5

    for t in range(1, len(acf)):
        if acf[t] <= 0:
            break

        tau += acf[t]

        if t >= window * tau:
            break

    return tau


sigma_values = [0.2, 0.5, 1.0, 2.0, 4.0]

for sigma in sigma_values:
    samples, acceptance = metropolis(200_000, sigma)
    samples = samples[10_000:]

    tau = autocorrelation_time(samples)
    N_eff = len(samples) / (2 * tau)

    print(
        f"sigma={sigma:.1f}, "
        f"acceptance={acceptance:.3f}, "
        f"tau_int={tau:.2f}, "
        f"N_eff={N_eff:.0f}"
    )
