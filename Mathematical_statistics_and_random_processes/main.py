import pandas as pd
import numpy as np
import math as m

df = pd.read_csv('data.csv')

# Создаем столбцы с пролагарифмированными данными
df['X'] = np.log(df['x'])
df['Y'] = np.log(df['y'])
df['xy'] = df['x'] * df['y']
df['x2'] = df['x'] ** 2
df['y2'] = df['y'] ** 2
print(df)

b = (df['xy'].mean() - df['x'].mean() * df['y'].mean()) / (df['x'].std() ** 2)
a = df['y'].mean() - b * df['x'].mean()
print(f'y = {a} + {b} * x')