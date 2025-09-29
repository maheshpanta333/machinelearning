import pandas as pd
import numpy as np
#%%
s=pd.Series([1,2,3,4,"as"])
fruit_protein = {
    "Avocado": 2.0,  # grams of protein
    "Guava": 2.6,
    "Blackberries": 2.0,
    "Oranges": 0.9,
    "Banana": 1.1,
    "Apples": 0.3,
    "Kiwi": 1.1,
    "Pomegranate": 1.7,
    "Mango": 0.8,
    "Cherries": 1.0
}
print(s.dtype)
print(s.values)
print(s.index)

#indexing
print(s[0:2])
#iloc->location based indexing takes number for param
print(s.iloc[1:3])

#s.name gives the name to the series itself
s.name="Some Bullshit"
print(s)
#we can use our own indices
#so we are going to add the names of the fruits in the index in so we can access the numbers with the fruits themselves for which we are going to use the list named index
index=['apple','banana','mango','grapes','watermelon']
#so we can use .index attribute and pass the index to set an index for the data set
s.index=index
print(s)


print(s['apple'])


#we cannot use iloc anymore with the label
'''
************comes a here loc where we pass the label itself and in this indexing both start values and end values are included**********
'''
print(s.loc[["apple",'watermelon']]);

'''
****   CONDITIONAL SELECTION 
we select values according to the data we want
'''

#lets take newer data set
protein=pd.Series(fruit_protein,name="Some another bullshit part II")
print(protein)


#now for the operation of conditions to see which value is big and which is small
print(protein[protein>2])
#this would return the proteins with higher protein than two



#logical operators

#to print the values with values of protein between 0.5 to 2 would be 
print(protein[(protein>0.5) & (protein<2)])
print(protein[(protein<1) | (protein>2)])



"""
Question:find sum of the non-null data of the series
"""
ans=pd.Series([2.4,1,np.nan,3,np.nan])
ans.index=index
print(ans.notnull())
print(ans.notnull().sum())

# %%
