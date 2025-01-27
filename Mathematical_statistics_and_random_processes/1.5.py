import pandas as pd
import numpy as np

# Загрузка данных
df = pd.read_csv('data.csv', index_col=0, delimiter="\t")

# Расчет необходимых параметров
k = 5
n = len(df)
r = (max(df['Среднегодовой объем выпускаемой продукции (тыс. руб.)']) -
     min(df['Среднегодовой объем выпускаемой продукции (тыс. руб.)']))
h = r / k
print(n, k, r, h)

# Преобразование данных в одну линию
line_ndf = pd.Series(df['Среднегодовой объем выпускаемой продукции (тыс. руб.)'].to_numpy().reshape(-1),
                     index=df['Среднегодовой объем выпускаемой продукции (тыс. руб.)'].to_numpy().reshape(-1))

# Группировка данных по диапазонам
scut_df = pd.cut(line_ndf, bins=k, right=False, retbins=True, precision=1)[0].rename("Диапазон")
cut_df = df.merge(scut_df, left_on='Среднегодовой объем выпускаемой продукции (тыс. руб.)', right_index=True)
cut_group = cut_df.groupby('Диапазон')

# Анализ данных
count_series = cut_group['Диапазон'].count().rename("Количество предприятий").sort_values()
sum_series = cut_group['Среднегодовой объем выпускаемой продукции (тыс. руб.)'].sum().rename("Совокупный объём выпущенной продукции").sort_values()

# Построение аналитической таблицы
travm_df = df[['Среднегодовой объем выпускаемой продукции (тыс. руб.)', 'Среднее списочное число рабочих (чел.)',
               'Количество посещений больниц в связи с травмами']]
travm_df = travm_df.assign(Травматизм=lambda row: (row['Количество посещений больниц в связи с травмами'] /
                                                  row['Среднее списочное число рабочих (чел.)']))

travm_df = travm_df.merge(scut_df, left_on='Среднегодовой объем выпускаемой продукции (тыс. руб.)', right_index=True)
travm_df = travm_df.sort_values(by=["Среднегодовой объем выпускаемой продукции (тыс. руб.)",
                                    'Среднее списочное число рабочих (чел.)'], ascending=[False, False])

# Вывод результатов
print(count_series)
print(sum_series)
travm_df.plot(x='Среднегодовой объем выпускаемой продукции (тыс. руб.)', y='Травматизм',
              xticks=range(1950, 4200 + 1, 250))