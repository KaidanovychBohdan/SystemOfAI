import numpy as np
import matplotlib.pyplot as plt

# Дані з таблиці
X = np.array([0.1, 0.3, 0.4, 0.6, 0.7])
Y = np.array([3.2, 3, 1, 1.8, 1.9])

# Створюємо поліном 4-го степеня на основі даних
coefficients = np.polyfit(X, Y, 4)

# Функція полінома на основі знайдених коефіцієнтів
polynomial = np.poly1d(coefficients)

# Створюємо нові точки для побудови гладкого графіка
X_smooth = np.linspace(min(X), max(X), 200)
Y_smooth = polynomial(X_smooth)

# Побудова графіка інтерполяційного полінома і точок
plt.plot(X_smooth, Y_smooth, label="Інтерполяційний поліном", color="blue")
plt.scatter(X, Y, color="red", label="Експериментальні точки")

# Підписи осей
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Інтерполяція поліномом 4-го степеня')

# Додаємо легенду та сітку
plt.legend()
plt.grid(True)

# Відображення графіка
plt.show()

# Визначаємо значення полінома у точках 0.2 і 0.5
y_at_02 = polynomial(0.2)
y_at_05 = polynomial(0.5)

# Виводимо значення в точках
print(f"Значення полінома в точці X = 0.2: {y_at_02}")
print(f"Значення полінома в точці X = 0.5: {y_at_05}")