import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Создание гистограммы
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, density=True, alpha=0.6, color='b', edgecolor='black')

# Добавление параметров графика
plt.title('Гистограмма нормального распределения')
plt.xlabel('Значения')
plt.ylabel('Плотность вероятности')

# Отображение графика
plt.grid()
plt.show()
