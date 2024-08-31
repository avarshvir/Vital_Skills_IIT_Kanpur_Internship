import pandas as pd

data1 = {"A": [1, 2, 3, 4, 5],
         "B": [6, 7, 8, 9, 10]}

df = pd.DataFrame(data1, index='a b c d e'.split())
print(df)
print("------------------------------------------")
# Rename columns
df.columns = ['A1', 'A2']

print(df)