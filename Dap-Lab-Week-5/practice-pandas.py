import pandas as pd

# Create the initial DataFrame
data = {
    'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'],
    'Age': [25, 30, 22, 35, 28],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'Salary': [50000, 55000, 40000, 70000, 48000]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\n" + "="*50 + "\n")

# 1. Accessing and Modifying the Index
print("1. Accessing the default index:")
print(df.index)
print("\n" + "="*50 + "\n")

# 2. Setting a Custom Index
print("2. Setting 'Name' as index:")
df_with_index = df.set_index('Name')
print(df_with_index)
print("\n" + "="*50 + "\n")

# 3. Resetting the Index
print("3. Resetting the index:")
df_reset = df_with_index.reset_index()
print(df_reset)
print("\n" + "="*50 + "\n")

# 4. Indexing with loc
print("4. Accessing row with loc (after setting 'Name' as index):")
row = df_with_index.loc['Alice']
print(row)
print("\n" + "="*50 + "\n")

# 5. Changing the Index
print("5. Setting 'Age' as new index:")
df_with_new_index = df.set_index('Age')
print(df_with_new_index)
print("\n" + "="*50 + "\n")

# DataFrame Access Methods
print("DataFrame Access Methods:")
print("\n" + "="*50 + "\n")

# 1. Accessing Columns
print("1. Accessing 'Age' column:")
age_column = df['Age']
print(age_column)
print("\n" + "="*50 + "\n")

# 2. Accessing Rows by Index
print("2. Accessing row at index 1:")
second_row = df.iloc[1]
print(second_row)
print("\n" + "="*50 + "\n")

# 3. Accessing Multiple Rows or Columns
print("3. Accessing first three rows and 'Name', 'Age' columns:")
subset = df.loc[0:2, ['Name', 'Age']]
print(subset)
print("\n" + "="*50 + "\n")

# 4. Accessing Rows Based on Conditions
print("4. Rows where Age > 25:")
filtered_data = df[df['Age'] > 25]
print(filtered_data)
print("\n" + "="*50 + "\n")

# 5. Accessing Specific Cells
print("5. Salary at index 2:")
salary_at_index_2 = df.at[2, 'Salary']
print(salary_at_index_2)