"""
DATAFRAME
"""

import numpy as np
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Alice"],
    "Age": [25, 30, 35, np.nan, 29, 25],
    "Department": ["HR", "IT", "Finance", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 70000, 62000, np.nan, 50000]
}


df=pd.DataFrame(data)
print(df)

#what if i want to get only department and salary from the original data frame itself on that case the legendary keyword would enter the chat "loc"

new_df=df.loc[:,["Department","Salary"]]
print(new_df)

#if we want to remove particular row or column we use drop() function
print(df.drop("Age",axis=1))
print(df)
#however in the original data frame the age column would still exist so to get rid of it what we do here is add another parameter naemd inplace and set its value to true now doing so would enable the original datafram to get rid of the age column entirely
df.drop('Age',axis=1,inplace=True)
print(df)

print(df.shape) #<- gives the shape of the matrix
print(df.info())
#df.info method gives all the information regarding the dataframe including the memory usage the dataframe takes and everything

#whilst the describe method what it does is describe the whole dataframe into different parameters
print(df.describe())


"""
BROADCASTING IN PANDAS
definition: to perform all the arithmetric operation to all series or dataframes of different but compatible shapes
"""

#increase salary of everython with 5000
df["Salary"]=df["Salary"]+5000# here the scaler 5000 is virtually streched to be large set of 5000 to fit the salary elemental size and then is added with every elements
#for operation pandas checks the index of the each elemsnts of the both dataframe and virtual set of tthe scaler and if the indrx matches they add it
print(df["Salary"])


#we can rename the columsn as well
df.rename(columns={"Department":"Dept"},inplace=True)
print(df)
#obv the inplace acts as an absolute here it allows the changes to sustain in the actual dataframe