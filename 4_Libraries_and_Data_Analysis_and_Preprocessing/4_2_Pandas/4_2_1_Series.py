import numpy as np
import pandas as pd
data1 = [1,2,3,4,5]
indexD = ['a','b','c','d','e']
series_data = pd.Series(data1, indexD)
print(series_data)

print("---------------------------------------------")
data2 = [1,2,6,4,5]
indexD2 = ['a','b','f','d','e']
series_data2 = pd.Series(data2,indexD2)
print(series_data2)

print("---------------------------------------------")
print(series_data + series_data2)