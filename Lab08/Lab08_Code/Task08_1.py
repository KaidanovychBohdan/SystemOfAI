import numpy as np
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()  # Використовуємо TensorFlow 1.x у середовищі 2.x

# Генеруємо дані для навчання
x_data = np.random.rand(100).astype(np.float32)
y_data = 3.0 * x_data + 2.0 + np.random.normal(0, 0.05, x_data.shape)

# Моделі параметри
k = tf.Variable(tf.random.uniform([1], -1.0, 1.0), name="k")
b = tf.Variable(tf.zeros([1]), name="b")
y_pred = k * x_data + b

# Функція втратІ
loss = tf.reduce_mean(tf.square(y_pred - y_data))

# Оптимізатор
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train = optimizer.minimize(loss)

# Ініціалізація змінних
init = tf.global_variables_initializer()

# Тренування моделі
with tf.Session() as sess:
    sess.run(init)

    for epoch in range(2001):
        _, loss_value, k_value, b_value = sess.run([train, loss, k, b])
        if epoch % 100 == 0:
            print(f"Епоха {epoch}: втрата={loss_value:.4f}, k={k_value[0]:.4f}, b={b_value[0]:.4f}")
