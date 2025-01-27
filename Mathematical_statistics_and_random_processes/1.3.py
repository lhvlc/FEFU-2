import pandas as pd

# Заданные данные
data = [99.2, 101.2, 99.3, 105.0, 97.3, 103.2, 105.4, 108.2,
        95.4, 96.8, 100.5, 90.3, 110.8, 111.5, 150.5, 140.3,
        89.8, 103.6, 115.8, 125.4, 116.5, 130.4, 90.6, 130.4,
        170.4, 109.2, 160.3, 122.4, 190.3, 202.0, 130.0, 119.6,
        99.9, 119.4, 127.0, 130.0, 140.0, 129.0, 150.0, 168.0]

# Ряд распределения рабочих с постоянным интервалом
k = 4
n = len(data)
r = max(data) - min(data)
h = r / k
print(n, k, r, h)

line_ndf = pd.Series(data, index=data)
cut_df = pd.cut(line_ndf, bins=k, right=False, retbins=True, precision=1)[0]
freq_df = cut_df.groupby(cut_df, observed=True).count()

int_df = pd.DataFrame(index=freq_df.index)
int_df['Середина интервала'] = pd.IntervalIndex.from_breaks(
    [min(data) + h*i for i in range(k+1)], closed='left'
)
int_df['Частота'] = freq_df.values
int_df = int_df.assign(ПлотностьЧастоты=lambda row: (row['Частота'] / h))
int_df = int_df.assign(ОтносительнаяЧастота=lambda row: (row['Частота'] / n))
int_df = int_df.assign(ПлотностьОтносительнойЧастоты=lambda row: (row['ОтносительнаяЧастота'] / h))

print(int_df)

# Ряд распределения рабочих на две группы: не выполняющие и выполнившие/перевыполнившие норму выработки
df = pd.DataFrame(data, columns=['Data'])
df['Status'] = df['Data'] < 100
check_df = df.groupby('Status').count()
print(check_df)