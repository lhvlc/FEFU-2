import pandas as pd
from math import sqrt

data = {
    'Возраст': [17, 18, 19, 20, 21],
    'Число студентов': [10, 50, 70, 30, 10]
}
df = pd.DataFrame(data)

r = max(df['Возраст']) - min(df['Возраст'])
print(r)

cdf = df.copy()
total_freq = sum(cdf['Число студентов'])
cdf['Варианта (s)'] = cdf['Число студентов'] * cdf['Возраст']
print(cdf)

selective_mean = sum(cdf['Варианта (s)']) / total_freq
print(selective_mean)

cdf['Разность (d)'] = round(cdf['Возраст'] - selective_mean, 1)
cdf['Частота (f)'] = abs(cdf['Разность (d)']) * cdf['Число студентов']
cdf['Частота (2f)'] = (cdf['Разность (d)'] ** 2) * cdf['Число студентов']
cdf = cdf.astype({'Частота (f)': 'int64'})
print(cdf)

mid_lin_disp = sum(cdf['Частота (f)']) / total_freq
print(mid_lin_disp)

disp = sum(cdf['Частота (2f)']) / total_freq
print(disp)

coef_var = sqrt(disp) / selective_mean * 100
print(coef_var)