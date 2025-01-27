import pandas as pd
import numpy as np

# Заданные данные
data = [5, 4, 2, 1, 6, 3, 3, 4, 3, 2, 2, 5, 6, 4, 3, 5, 4, 1, 2, 3, 3, 4, 1, 6,
        5, 1, 3, 4, 3, 5, 4, 3, 3, 4, 4, 6, 4, 4, 3, 1, 5, 4, 3, 2, 6, 3, 4,
        5, 5, 3, 3, 3, 3, 4, 5, 5, 6, 2, 4]

df = pd.DataFrame({'Data': data})  # Создаем DataFrame из данных

print(df)  # Выводим исходные данные

# Добавление столбца Count для подсчета количества вхождений каждого значения Data
df["Count"] = df.groupby("Data")['Data'].transform("count")

# Группировка по уникальным значениям Data, подсчет количества и сортировка
df = df.groupby(['Data']).head(1).sort_values(by=["Data"]).reset_index(drop=True)
print(df)  # Выводим результаты группировки

k = 3
line_ndf = pd.Series(df['Data'].to_numpy().reshape(-1), index=df['Data'].to_numpy().reshape(-1))
print(line_ndf)

cut_df = pd.cut(line_ndf, bins=k, right=False, retbins=True, precision=1)[0]
print(cut_df)

freq_df = cut_df.groupby(cut_df, observed=True).count()
print(freq_df)