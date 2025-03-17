import pandas as pd

data = [
    ["Tom", 10],
    ["Jerry", 20],
    ["Mickey", 30],
    ["Donald", 40],
]

df = pd.DataFrame(data, columns=["Name", "Age"])
print(df)