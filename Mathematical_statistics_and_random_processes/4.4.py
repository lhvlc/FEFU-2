import pandas as pd

df = pd.read_csv('data4.4.csv', index_col=0)
print(df)

most_freq = df.loc[df['Число транспорта'] == max(df['Число транспорта'])]
most_freq_val = most_freq.index[0]  # исправление: использовать most_freq.index[0] вместо mod.index[0]
print(most_freq_val)

bottom_freq = 14
cur_freq = 38
prev_freq = 15.3
next_freq = 10.4
h = 2
mod_val = bottom_freq + ((cur_freq - prev_freq)/((cur_freq - prev_freq) + (cur_freq - next_freq))) * h
print(mod_val)

# Ранжирование
cdf = df.cumsum()
print(cdf)

print(bottom_freq + (((max(cdf['Число транспорта']) / 2) + cdf.loc[most_freq_val]['Число транспорта']) / cur_freq) * h)