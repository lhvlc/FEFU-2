import pandas as pd
import numpy as np
from numpy import log10

# Заданные данные
data = [7.0, 6.0, 5.9, 9.4, 6.5, 7.3, 7.6, 9.3, 5.8, 7.2,
        7.1, 8.3, 7.5, 6.8, 7.1, 9.2, 6.1, 8.5, 7.4, 7.8,
        10.2, 9.4, 8.8, 8.3, 7.9, 9.2, 8.9, 9.0, 8.7, 8.5]

dataFrame = pd.DataFrame(data, columns=['Data'])
n = len(dataFrame)
dataFrame

sdf = dataFrame
sdf["Count"] = sdf.groupby("Data")['Data'].transform("count")
sdf = sdf.groupby(['Data']).head(1).sort_values(by=["Data"]).reset_index(drop=True)
sdf

k = int(round(1 + 3.22 * log10(n), 0))
r = round((max(sdf['Data']) - min(sdf['Data'])), 1)
h = round(r / k, 1)
print(n, k, r, h)

line_ndf = pd.Series(dataFrame['Data'].to_numpy().reshape(-1), index=dataFrame['Data'].to_numpy().reshape(-1))
line_ndf

cut_df = pd.cut(line_ndf, bins=k, right=False, retbins=True, precision=1)[0]
cut_df

freq_df = cut_df.groupby(cut_df, observed=True).count()
freq_df

int_df = pd.DataFrame(index=freq_df.index)
int_df['Середина интервала'] = np.array([min(sdf['Data']) + h / 2 + h * i for i in range(k)])
int_df['Частота'] = freq_df.values
int_df = int_df.assign(ПлотностьЧастоты=lambda row: (row['Частота'] / h))
int_df = int_df.assign(ОтносительнаяЧастота=lambda row: (row['Частота'] / n))
int_df = int_df.assign(ПлотностьОтносительнойЧастоты=lambda row: (row['ОтносительнаяЧастота'] / h))
int_df

result_table = int_df.sort_values(by=['Частота'], ascending=False).head(1)
result_table