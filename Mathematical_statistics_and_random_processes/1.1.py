import pandas as pd

# данные о числе членов в каждой семье
data = [3, 2, 5, 4, 6, 5, 3, 2, 4, 3, 4, 2, 3, 2, 5, 2, 3, 4, 2, 5, 7, 6]

# создание DataFrame
df = pd.DataFrame(data, columns=['Data'])

# подсчет количества значений и добавление столбца "Count"
df["Count"] = df.groupby("Data")['Data'].transform("count")

# удаление дубликатов и сортировка
df = df.groupby(['Data']).head(1).sort_values(by=["Data"]).reset_index(drop=True)

# добавление столбца с относительной частотой
df = df.assign(RelFreq=lambda x: (x['Data'] / x['Count']))

print(df)