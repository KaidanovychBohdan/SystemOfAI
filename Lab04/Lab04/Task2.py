import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Дані X та Y з таблиці
X = np.array([3.33, 1, 63, 0.87, 0.42, 0.27])
Y = np.array([0.48, 1.03, 2.02, 4.25, 7.16, 11.5])

# Функція для апроксимації (наприклад, лінійна: Y = a * X + b)
def func(X, a, b):
    return a * X + b

# Використання методу найменших квадратів для знаходження параметрів a і b
params, covariance = curve_fit(func, X, Y)

# Отримуємо знайдені параметри a та b
a, b = params

# Побудова графіка
plt.scatter(X, Y, label="Експериментальні дані", color="red")  # Експериментальні точки
plt.plot(X, func(X, a, b), label=f"Аппроксимація: Y = {a:.2f}*X + {b:.2f}", color="blue")  # Лінія апроксимації

# Додаємо підписи та легенду
plt.xlabel('X')  # Підпис осі X
plt.ylabel('Y')  # Підпис осі Y
plt.legend()  # Додаємо легенду на графік
plt.grid(True)  # Включаємо сітку для кращої візуалізації
plt.title('Апроксимація методом найменших квадратів')  # Заголовок графіка

# Відображення графіка
plt.show()