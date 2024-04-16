import numpy as np
import pandas as pd
#Initialize given data into dataframe
df = pd.DataFrame(
    data = [
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
        [7.0, 8.0, 9.0],
        [np.nan, np.nan, np.nan]],
        columns= ["A", "B", "C"]
    )
print(df)

print()

#Create a new Dataframe using dictionary
df2 = pd.DataFrame({
    "sum" : df.sum(),
    "min" : df.min(),
    "max" : df.max(),
    "std" : df.std()
})
#Transpose because the order is inverted
print(df2.T)