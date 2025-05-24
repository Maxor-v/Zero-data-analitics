import pandas as pd
import matplotlib.pyplot as plt

# Чтение данных из CSV файла
data = pd.read_csv('price.csv', sep=',')

# Печать содержимого DataFrame для проверки
print(data)

# Преобразование цен в числовой формат
data['Цена'] = pd.to_numeric(data['Цена'], errors='coerce')

# Нахождение средней цены
average_price = data['Цена'].mean()
print(f"Средняя цена: {average_price:.2f}")

# Построение гистограммы цен
plt.figure(figsize=(10, 6))
plt.hist(data['Цена'], bins=10, color='blue', alpha=0.7)
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена')
plt.ylabel('Частота')
plt.grid(axis='y', alpha=0.75)
plt.show()
