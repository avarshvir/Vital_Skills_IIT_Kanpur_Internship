import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
print(df)

print("----------------------------------------------")

#selection and indexing
print(df[['W','Z']])
print("-----------------")
print(df['W'])
print("--------------------------")
#SQL syntax (not recommended)
print(df.W)
print("-------------------------------------")
#creating new column
df['new'] = df['X'] + df['Y']
print(df)
print("----------------------------------------")
#removing columns
# 0 -> for row, 1 -> coumns
df.drop('new',axis=1,inplace=True)
print(df)
print("----------------------------------------")
#removing row
df.drop('D',axis=0,inplace=True)
print(df)
print("-------------------------------------------")
# selecting row
print(df.loc['A'])
print("----------------------")
#selecting
print(df.iloc[0])
print("------------------------------------------")
#conditional selection
print(df>0)  # boolean value
print(df[df>0])     #numeric value