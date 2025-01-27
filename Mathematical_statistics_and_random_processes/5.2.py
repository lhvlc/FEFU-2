import pandas as pd
from math import sqrt

df = pd.read_csv('data5.2.csv', index_col=0)
mid_int = [50, 200, 400, 750, 2000, 4000]
df['Середина интервала'] = mid_int  # Принимаем, что последний интервал идёт до 5000
print(df)

cdf = df.copy()
total_freq = sum(cdf['Число предприятий'])
cdf['Варианта (s)'] = cdf['Число предприятий'] * cdf['Середина интервала']
print(cdf)

selective_mean = sum(cdf['Варианта (s)']) / total_freq
print(selective_mean)

cdf['Разность (d)'] = round(cdf['Середина интервала'] - selective_mean, 1)
cdf['Частота (f)'] = abs(cdf['Разность (d)']) * cdf['Число предприятий']
cdf['Частота (2f)'] = (cdf['Разность (d)'] ** 2) * cdf['Число предприятий']
cdf = cdf.astype({'Частота (f)': 'int64'})
print(cdf)

mid_lin_disp = sum(cdf['Частота (f)']) / total_freq
mid_lin_disp

disp = sum(cdf['Частота (2f)']) / total_freq
disp

coef_var = sqrt(disp) / selective_mean * 100
coef_var