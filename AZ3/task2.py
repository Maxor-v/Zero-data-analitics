import numpy as np
import matplotlib.pyplot as plt

# Генерация двух массивов из 5 случайных чисел
x = np.random.rand(5)  # первый набор данных
y = np.random.rand(5)  # второй набор данных

# Печатаем массивы для проверки
print("Массив x:", x)
print("Массив y:", y)

# Построение диаграммы рассеяния
plt.scatter(x, y)
plt.title('Диаграмма рассеяния')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
