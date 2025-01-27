import pandas as pd

# Manually specified data
data = {
    'Группы гостиниц по числу принимаемых туристов в месяц, чел.': [
        '1800-2000', '2000-2200', '2200-2400', '2400-2600', '2600-2800', '2800-3000', '3000-3200'
    ],
    'Число гостиниц, процент к итогу': [7.3, 10.4, 12.2, 25.5, 22.4, 14.6, 7.6]
}

# Create a DataFrame
df = pd.DataFrame(data)
# Example calculation (adjust this based on your specific requirement)
mid_int = [1900, 2100, 2300, 2500, 2700, 2900, 3100]
step = 200
df['Середина'] = mid_int
df

df['Разница'] = df['Середина'] - 2500  # Example of using a specific value for middle_diff
df['Разница (s)'] = df['Разница'] / step
df['Варианта (s)'] = df['Разница (s)'] * df['Число гостиниц, процент к итогу']
df

# Example calculation based on the modified data
mid_arithm = sum(df['Варианта (s)'] * step) / sum(df['Число гостиниц, процент к итогу'])
selective_mean = mid_arithm + 2500  # Adjusted based on the specific middle difference used
selective_mean

print(f"Selective mean: {selective_mean}")