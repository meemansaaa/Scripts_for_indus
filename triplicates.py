import pandas as pd
import numpy as np

file = 'dnawise_3.xlsx'
df = pd.read_excel(file)
print(df.head(5))

def triplicate():
    newdf = pd.DataFrame(np.repeat(df.values, 3, axis = 0))
    newdf.columns = df.columns #to copy the same column names
    newdf.to_excel('triplicated_dnawise3.xlsx')
    print(newdf.head(6))


triplicate()