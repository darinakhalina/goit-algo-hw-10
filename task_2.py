import matplotlib.pyplot as plt
import scipy.integrate as spi
import numpy as np


def f(x):
    return x**2


a = 0
b = 2

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y, "r", linewidth=2, label="f(x)")

limit_x = np.linspace(a, b)
limit_y = f(limit_x)
ax.fill_between(limit_x, limit_y, color="gray", alpha=0.3)

points = 100000
random_x = np.random.uniform(a, b, points)
random_y = np.random.uniform(0, f(b), points)

points_under_curve = sum(random_y <= f(random_x))
area = (b - a) * f(b)
area_under_curve = area * (points_under_curve / points)

quad_value, error = spi.quad(f, a, b)

ax.axvline(x=a, color="gray", linestyle="--")
ax.axvline(x=b, color="gray", linestyle="--")
ax.set_title("Графік інтегрування f(x) = x^2 від " + str(a) + " до " + str(b))
ax.legend()
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")

plt.grid()
plt.show()

print("Значення методом Монте-Карло:", area_under_curve)
print("Точне значення:", quad_value)
