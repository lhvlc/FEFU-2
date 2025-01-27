import pandas as pd
import matplotlib.pyplot as plt

# Создание DataFrame
data = {
    'Годы': [1, 2, 3, 4, 5],
    'Млн. руб.': [15317, 22620, 37593, 42245, 50789]
}
df = pd.DataFrame(data)

# Линейный график
df.plot(kind='line', x='Годы', y='Млн. руб.', marker='o')
plt.xlabel('Годы')
plt.ylabel('Млн. руб.')
plt.title('График')
plt.grid(True)
plt.show()

# Барплот
df.plot(kind='bar', x='Годы', y='Млн. руб.')
plt.xlabel('Годы')
plt.ylabel('Млн. руб.')
plt.title('График')
plt.show()

# Гистограмма
df.plot(kind='hist', y='Млн. руб.')
plt.ylabel('Частота')
plt.title('Гистограмма')
plt.show()

# График плотности
df['Млн. руб.'].plot(kind='kde')
plt.ylabel('Плотность')
plt.xlabel('Млн. руб.')
plt.title('График плотности')
plt.show()

# График площади
df.plot(kind='area', x='Годы', y='Млн. руб.')
plt.xlabel('Годы')
plt.ylabel('Млн. руб.')
plt.title('График площади')
plt.show()

# Box plot
df.plot(kind='box')
plt.ylabel('Млн. руб.')
plt.title('Box Plot')
plt.show()