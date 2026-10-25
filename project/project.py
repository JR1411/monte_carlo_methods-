import numpy as np
import matplotlib.pyplot as plt


# parameters for the simulation
L = 20
m2 = -1
lam = 6
step_size = 1

n_thermal = 1000
n_measures = 3000

rng = np.random.default_rng(42)

# initial field

phi = rng.normal(0, 0.1, size=(L, L))


def potential(x):
    return m2 / 2 * x**2 + lam / 24 * x**4


def local_action(i, j, value):
    neighbors = [
        phi[((i+1) % L, j)],
        phi[((i-1) % L, j)],
        phi[(i, (j+1) % L)],
        phi[(i, (j-1) % L)]
    ]

    kinetic = 1/2 * sum(
        (value - neighbors)**2
        for neighbors in neighbors
    )

    return kinetic + potential(value)


def metropolis_sweep():
    accepted = 0

    for _ in range(L*L):
        i = rng.integers(L)
        j = rng.integers(L)

        old = phi[i, j]
        new = old + rng.uniform(-step_size, step_size)

        delta_S = (local_action(i, j, old) - local_action(i, j, new))

        if delta_S <= 0 or rng.random() < np.exp(-delta_S):
            phi[i, j] = new
            accepted += 1

    return accepted / (L*L)


for _ in range(n_thermal):
    metropolis_sweep()


magnetization = []
acceptance = []

for _ in range(n_measures):
    acceptance.append(metropolis_sweep())
    magnetization.append(np.mean(phi))

magnetization = np.array(magnetization)

print(r"Mean $\vert \Phi \vert$ : ", np.mean(np.abs(magnetization)))
print("acceptance : ", np.mean(acceptance))

fig, ax = plt.subplots(1, 2, figsize=(10, 5))

im = ax[0].imshow(phi, cmap="plasma")
ax[0].set_title("final field configurations")
plt.colorbar(im, ax=ax[0], label="phi")


ax[1].plot(magnetization)
ax[1].set_xlabel("metropolis sweep", fontsize=15)
ax[1].set_ylabel("mean field", fontsize=15)
ax[1].set_title("Field evolution")

plt.tight_layout()
plt.show()
