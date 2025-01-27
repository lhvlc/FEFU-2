import pandas as pd

# Manually specified data
data = {
    'Цехи': [1, 2, 3, 4],
    'Средняя ЗП, руб.': [1100, 1230, 1150, 1350],
    'ФОТ, в % к итогу': [20, 30, 10, 40]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate the average salary using the provided data
average_salary = sum((df['Средняя ЗП, руб.'] * df['ФОТ, в % к итогу']) / 100)

print(f"Средняя ЗП: {average_salary}")