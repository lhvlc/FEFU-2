import pandas as pd
from math import sqrt

df = pd.read_csv('data5.3.csv')
print(df)

en_df = df.loc[df['Тип оборудования'] == 'Энергетическое'].reset_index(drop=True)
mid_int = [0.3, 0.65, 0.75, 0.9]
en_df['Середина интервала'] = mid_int
print(en_df)

prom_df = df.loc[df['Тип оборудования'] == 'Производственное'].reset_index(drop=True)
mid_int = [0.4, 0.825, 0.875, 0.95]
prom_df['Середина интервала'] = mid_int
print(prom_df)


def get_coef(adf):
    cdf = adf.copy()
    total_freq = sum(cdf['Число единиц оборудования'])
    cdf['Варианта (s)'] = cdf['Число единиц оборудования'] * cdf['Середина интервала']

    selective_mean = sum(cdf['Варианта (s)']) / total_freq

    cdf['Разность (d)'] = round(cdf['Середина интервала'] - selective_mean, 1)
    cdf['Частота (f)'] = abs(cdf['Разность (d)']) * cdf['Число единиц оборудования']
    cdf['Частота (2f)'] = (cdf['Разность (d)'] ** 2) * cdf['Число единиц оборудования']

    disp = sum(cdf['Частота (2f)']) / total_freq
    coef_var = sqrt(disp) / selective_mean * 100
    return coef_var


print(get_coef(prom_df))

print(get_coef(en_df))