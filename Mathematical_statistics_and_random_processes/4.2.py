import pandas as pd

df = pd.read_csv('data4.2.csv')
print(df)

mod = df.loc[df['Число рабочих'] == max(df['Число рабочих'])]
mod_val = mod['Количество станков'].values[0]
print(mod_val)

# Ранжирование
cdf = df.sort_values(by=['Число рабочих']).reset_index(drop=True)
cdf['Число рабочих'] = cdf['Число рабочих'].cumsum()
print(cdf)
#Взятие среднего индекса
mid_index = ((cdf.loc[cdf['Количество станков'] == mod_val]['Число рабочих'] + 1) / 2).values[0]
print(mid_index)
# # Получение медианного значения
cdf = cdf.sort_values(by=['Число рабочих'], ascending=False)
print(cdf.loc[(cdf['Число рабочих'] >= mid_index)].sort_values(by=['Число рабочих'], ascending=True).head(1)['Количество станков'].values[0])