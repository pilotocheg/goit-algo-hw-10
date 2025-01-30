import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


# Визначення функції та межі інтегрування
def f(x):
    return x**2


a = 0  # Нижня межа
b = 2  # Верхня межа

# Метод Монте-Карло
N = 10000  # Кількість випадкових точок
x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, f(b), N)

dots_under_curve = y_rand < f(x_rand)

# Обчислення площі методом Монте-Карло
monte_carlo_result = (b - a) * f(b) * np.sum(dots_under_curve) / N
# Аналітичне обчислення площі
analytic_result, _ = quad(f, a, b)

# Виведення результатів
print(f"Метод Монте-Карло: {monte_carlo_result}")
print(f"Аналітичне значення: {analytic_result}")
print(f"Похибка: {abs(monte_carlo_result - analytic_result)}")

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, "r", linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color="gray", alpha=0.3)

# додавання випадкових точок на графік
ax.scatter(x_rand, y_rand, c=dots_under_curve, cmap="coolwarm", s=1, alpha=0.5)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color="gray", linestyle="--")
ax.axvline(x=b, color="gray", linestyle="--")
ax.set_title("Графік інтегрування f(x) = x^2 від " + str(a) + " до " + str(b))

plt.grid()
plt.show()
