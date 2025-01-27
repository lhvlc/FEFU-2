import pandas as pd
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

# Создание DataFrame
data = {
    'Организация': [1, 2, 3],
    'Общие затраты': [8428.42, 9354.24, 13185.65],
    'Число застрахованных человек (тыс.)': [15.4, 12.8, 730.8],
    'Средние затраты на лечение 1 человека (р.)': [547.3, 30.7, 429.5]
}
df = pd.DataFrame(data)

step = 10
plt.xlim(-step * 2, 800)
plt.xlabel("Число застрахованных человек (тыс.)")
plt.ylim(0, 600)
plt.ylabel("Средние затраты на лечение 1 человека (р.)")
axes = plt.gca()
cum_dist = 0.0
for index in range(len(df)):
    row = df.iloc[index]
    coord = (cum_dist, 0)
    width = row['Число застрахованных человек (тыс.)']
    height = row['Средние затраты на лечение 1 человека (р.)']
    S = row['Общие затраты']

    rectangle = mpatches.Rectangle(coord, width, height)

    axes.add_patch(rectangle)
    # plt.text(cum_dist + width/2, 0 + height/2, S, horizontalalignment='center', verticalalignment='center')

    cum_dist += step + width

plt.show()