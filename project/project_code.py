import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

M2 = -1.0
LAM = 6.0


def potential(phi, h):
    return h*phi + 0.5*M2*phi**2 + LAM/24*phi**4


def action(phi, beta, h):
    # Count each nearest-neighbor bond once.
    dx = phi - np.roll(phi, -1, axis=0)
    dy = phi - np.roll(phi, -1, axis=1)

    kinetic = 0.5 * np.sum(dx**2 + dy**2)
    interaction = np.sum(potential(phi, h))

    return beta * (kinetic + interaction)


def metropolis_sweep(phi, beta, h, step):
    L = phi.shape[0]
    accepted = 0

    # Local updates, one proposal per site on average
    for _ in range(L * L):
        i = rng.integers(L)
        j = rng.integers(L)

        old = phi[i, j]
        new = old + rng.uniform(-step, step)

        neighbors = (
            phi[(i+1) % L, j]
            + phi[(i-1) % L, j]
            + phi[i, (j+1) % L]
            + phi[i, (j-1) % L]
        )

        delta_kinetic = (
            2*(new**2 - old**2)
            - (new-old)*neighbors
        )

        delta_S = beta * (
            delta_kinetic
            + potential(new, h)
            - potential(old, h)
        )

        if delta_S <= 0 or rng.random() < np.exp(-delta_S):
            phi[i, j] = new
            accepted += 1

    return accepted / (L*L)


def simulate(L, beta, h, thermal=1500,
             measurements=1000, thin=5):

    # Random initial configuration
    phi = rng.normal(0, 0.5, (L, L))
    step = 1.0

    # Thermalization and proposal tuning
    for sweep in range(thermal):
        acceptance = metropolis_sweep(phi, beta, h, step)

        # Tune only during early thermalization
        if sweep < thermal // 2:
            if acceptance > 0.55:
                step *= 1.01
            elif acceptance < 0.45:
                step *= 0.99

    magnetizations = []
    actions = []
    acceptance_rates = []

    # Equilibrium measurements
    for _ in range(measurements):
        rates = []

        for _ in range(thin):
            rates.append(metropolis_sweep(phi, beta, h, step))

        magnetizations.append(np.mean(phi))
        actions.append(action(phi, beta, h) / (L*L))
        acceptance_rates.append(np.mean(rates))

    M = np.asarray(magnetizations)
    A = np.asarray(actions)

    mean_m = np.mean(M)
    mean_abs_m = np.mean(np.abs(M))

    chi_m = L**2 * (np.mean(M**2) - mean_m**2)
    chi_a = L**2 * (np.mean(A**2) - np.mean(A)**2)

    binder = 1 - np.mean(M**4) / (3*np.mean(M**2)**2)

    return {
        "M": mean_m,
        "abs_M": mean_abs_m,
        "action_density": np.mean(A),
        "chi_M": chi_m,
        "chi_A": chi_a,
        "binder": binder,
        "acceptance": np.mean(acceptance_rates),
    }


def scan(betas, sizes, fields):
    results = {}

    for h in fields:
        for L in sizes:
            measurements = []

            for beta in betas:
                result = simulate(L, beta, h)
                measurements.append(result)

                results[(h, L)] = measurements

    return results


# Initial exploratory scan
betas = np.linspace(0.2, 1.2, 15)
sizes = [8, 12, 16]
fields = [0.0, 0.1, 0.2]

results = scan(betas, sizes, fields)


# Plot magnetization susceptibility
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

for ax, h in zip(axes, fields):
    for L in sizes:
        chi = [r["chi_M"] for r in results[(h, L)]]

        ax.plot(betas, chi, "o-", label=f"L={L}")

    ax.set_title(f"h = {h}")
    ax.set_xlabel(r"$\beta$")
    ax.set_ylabel(r"$\chi_M$")
    ax.grid(alpha=0.3)
    ax.legend()

plt.tight_layout()
plt.show()
