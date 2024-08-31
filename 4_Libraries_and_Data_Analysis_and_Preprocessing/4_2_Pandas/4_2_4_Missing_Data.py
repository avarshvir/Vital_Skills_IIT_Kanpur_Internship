import pandas as pd
import numpy as np
df = pd.DataFrame({
    'A': [1,2,np.nan],
    'B': [5,np.nan,np.nan],
    'C':[1,2,3]
},index=['a1', 'a2', 'a3'])

print(df)
print("----------------------")
print(df.dropna())
print("----------------------")
print(df)

print("-----------------------------")
#fill values
print(df.fillna('Fill'))
print(df['A'].fillna(value=df['A'].mean()))
print(df.fillna(value = df.mean(),inplace=True))
print(df)