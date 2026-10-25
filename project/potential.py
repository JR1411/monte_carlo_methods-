import numpy as np
import matplotlib.pyplot as plt


def potential(x):
    return - x**2 / 2 + (6/24) * x**4


x_values = 2 * np.linspace(-1, 1, 1000)

potential_curve = potential(x_values)


plt.plot(x_values, potential_curve, color="black")
plt.xlabel("x", fontsize=15)
plt.ylabel("y", fontsize=15)
plt.tick_params("both", labelsize=15)
plt.title(r"potential $V = -\frac{x^2}{2} + \frac{6}{24}x^4$", fontsize=20)
plt.show()
