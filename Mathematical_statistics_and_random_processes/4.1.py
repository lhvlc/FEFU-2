import pandas as pd

# Manually specified data for exam scores and student counts
data = {
    'Экзаменационные оценки': ['Отлично', 'Хорошо', 'Удовлетворительно', 'Неудовлетворительно'],
    'Число студентов': [7, 18, 6, 2]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculation to find the median score category based on student count
cdf = df.sort_values(by='Число студентов').reset_index(drop=True)
total_students = cdf['Число студентов'].sum()
median_index = total_students / 2

# Find the median score category
cumulative_sum = 0
for index, row in cdf.iterrows():
    cumulative_sum += row['Число студентов']
    if cumulative_sum >= median_index:
        median_score = row['Экзаменационные оценки']
        break

# Find the mode score category (мода)
mode_score = df.loc[df['Число студентов'].idxmax(), 'Экзаменационные оценки']

print(f"Median score category: {median_score}")
print(f"Mode score category: {mode_score}")