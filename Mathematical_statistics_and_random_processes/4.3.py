import pandas as pd
df = pd.read_csv('data4.3.csv', index_col=0)
print(df)

freq_prom = df.loc[df['Промышленность'] == max(df['Промышленность'])].index[0]
freq_act = df.loc[df['Сфера услуг'] == max(df['Сфера услуг'])].index[0]
freq_med = df.loc[df['Медицина'] == max(df['Медицина'])].index[0]
print(freq_prom, freq_act, freq_med)

cdf = df.copy()
cdf.loc[:, ['Промышленность', 'Сфера услуг', 'Медицина']] = cdf.loc[:,
                                                            ['Промышленность', 'Сфера услуг', 'Медицина']].cumsum()
print(cdf)

mod_prom = 35 + ((35.6 - 34.9) / (35.6 - 34.9) + (35.6 - 8.1)) * 10
print(mod_prom)

med_prom = 35 + (((100 / 2) + 43.9) / 35.6) * 10
print(med_prom)

mod_act = 25 + ((29.7 - 14.1) / ((29.7 - 14.1) + (29.7 - 26.3))) * 10
print(mod_act)

med_act = 25 + (((100 / 2) + 14.1) / 29.7) * 10
print(med_act)

mod_med = 45 + ((27.7 - 11.5) / ((27.7 - 11.5) + (27.7 - 24.6))) * 5
print(mod_med)

med_med = 45 + (((100 / 2) + 24.5) / 27.7) * 5
print(med_med)