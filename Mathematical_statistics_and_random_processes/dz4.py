import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

xs = [78,82,87,79,89,106,67,88,73,87,76,115]
ys = [133,148,134,154,162,195,139,158,152,162,159,173]
n = len(xs)

df = pd.DataFrame({'x': xs, 'y': ys})

x_mean = df.x.mean()
y_mean = df.y.mean()

σx = df.x.std()
σy = df.y.std()
σ = [σx, σy]

b = ((df.x * df.y).mean() - x_mean * y_mean) / σx**2
a = y_mean - b*x_mean

r_xy = b * min(σ) / max(σ)

linreg = lambda t: a + b*t

y_krishechka = linreg(df.x)
dif_y = df.y - y_krishechka

A = (abs(dif_y / df.y)).mean() * 100

print(f'y = {a} + {b}*x')
print(f'r_xy = {r_xy}')
print(f'A = {A}')

_x = df.sort_values('x')['x']
_y = df.sort_values('x')['y']

plt.plot(_x,_y)

lx = np.linspace(min(_x), max(_x), 100)
ly = linreg(lx)

plt.plot(lx,ly)

mr = ( (1-r_xy**2) / (n-2) )**.5
mb = ( sum(dif_y**2) / sum((df.x - x_mean)**2) / (n-2) )**.5
ma = ( sum(dif_y**2) * sum(df.x**2) / sum((df.x - x_mean)**2) / n / (n-2) )**.5
t_table = 2.23

print(f'ma = {ma}\nmb = {mb}\nmr = {mr}\n')
print(f'ta = {a/ma}\ntb = {b/mb}\ntr = {r_xy/mr}\n')
print(f't_table = {2.23}')

x_p = 1.07 * x_mean
y_p = linreg(x_p)
m = 1 # пока что так, вроде количество параметров, а вроде и нет

mp = ( sum(dif_y**2) / (n-m-1) )**.5 * ( 1 + 1/n + (x_p - x_mean) / sum((df.x - x_mean)**2) )**.5

Delta_yp = t_table * mp

y_p-Delta_yp, y_p+Delta_yp