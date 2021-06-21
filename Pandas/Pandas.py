'''Pandas Tutorial: DataFrames in Python

How to create a Pandas DataFrame
    Take a 2 D array as input
    Take a dictionaru as input
    Take a Dataframe as input
    Take a series as input
    Find out the shape of the dataframe
How to select an index or column from a pandas dataframe
How to iterate over a Pandas DataFrame

Packages:
pandas - library offering data structures for data analysis and manipulation
numpy - library adding support for large, multi-dimensional arrays and matrices

Keywords: pd.DataFrame; df.shape; len(); df.iloc[]; df.loc[], df.at[];
df.iat[]; set_index(); df.index; df.reset_index(); .rename()

Reference (Wakelet)
https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python

'''
import numpy as np
import pandas as pd


'''HOW TO CREATE A PANDAS DATAFRAME'''
data = np.array([['','Col1', 'Col2'], ['Row1', 1,2],['Row2', 3,4]]) # Two columns, two row
df = pd.DataFrame(data=data[1:,1:],#Zero based, everythin after the first element
                   index=data[1:,0], # only the 0 element
                   columns=data[0,1:]) # list 0, everything after the first element

'''Take a 2D array as input to your DataFrame'''
# my_2darray = np.array([[1,2,3], [4,5,6]])
# print(my_2darray)
# print(pd.DataFrame(my_2darray))

''' #Take a dictionary as input to you dataframe'''
# my_dict = {1: ['1', '3'], 2: ['1', '2'], 3: ['2', '4']}
# print(my_dict)
# print(pd.DataFrame(my_dict))

'''Take a DataFrame as input to you DataFrame'''
# my_df = pd.DataFrame(data=[4,5,6,7], index=range(0,2), columns=['A', 'B'])
# print(my_df)
# print(pd.DataFrame(my_df))

'''Take a series as input to your DataFrame'''
# my_series = pd.Series({"United Kingdom":"London", "India":"New Delhi", "United States":"Washington", "Belgium":"Brussels"})
# print(my_series)
# print(pd.DataFrame(my_series))

'''Find out the shape of the DataFrame'''
# df = pd.DataFrame(np.array([[1,2,3,], [4,5,6], [7,8,9]]))
# print(df)
# print(df.shape)#dimensions of my data frame height and width
# print(len(df))# only the hight
# print(df.index)
# print(df[0].count)#will not call NaN
# print(list(df.columns.values))
#print(df.columns)


'''HOW TO SELECT AN INDEX OR COLUMN FROM A PANDAS DATAFRAME '''
#using 'iloc[]'
# print(df.iloc[0][0], df.iloc[0][1]) # select [index][column], selecting multiple values

#using 'loc[]'
# print(df.loc[0][:,'Col1']) # loc look for label

#using 'at[]'
# print(df.at[0,'Col1'])

#Select Row
print(df.iloc[0])

#Use 'loc[]' to select column 'A'
# print(df.loc[:,'A'])


#Adding an index to a DataFrame set_index()
# print(df)
# df.set_index('C')

# Adding Rows to a DataFrame
# df = pd.DataFrame(data=np.array([[1,2,3],[4,5,6],[7,8,9]]), index=[2,'A', 4], columns=[48, 49, 50])
#
# print(df)
# print(df.loc[2])#looks at the values at the label
# print(df.iloc[2])#looks at the postion
# # print(df.ix[2])#deprecated
# print(df.loc[:, 48])

# df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
#                   index= [2.5, 12.6, 4.8], columns=[48, 49, 50])
# print(df)

#This will make an index labeled '2' and add the new values
# df.loc[2] = [60, 50 , 40]
# print(df)

##Adding a Colum to your DataFrame
# df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
#                   columns=['A', 'B', 'C'])
# print(df)
# df['D'] = df.index
# print(df)
#
# #append a column to df
# df.loc[:, 'D'] = pd.Series(['5', '6', '7'], index=df.index)
# print(df)
#
# df_reset = df.reset_index(level=0, inplace=True)
# print(df_reset)

##how to delete Indices, rows or Columns from a pandas Data Frame
'''Removing there from the data structure '''

#Deleting an Index from Your DataFrame
# df = pd.DataFrame(data=np.array([[1,2,3],[4,5,6],[7,8,9],[40,50,60],[23,35,37]]),
#                   index=[2.5, 12.6, 4.8, 4.8, 2.5],
#                   columns=[48,49,50])
# print(df)
# df.reset_index().drop_duplicates(subset='index', keep='last').set_index('index')
# print(df)

'''HOW TO DROP A SINGLE COLUMN FROM A DATAFRAME'''
df1 = df.drop(['column_name'], axis=1) # creates a new DataFrame
del(df['column_name']) # applies to the current DF, does not create new DF



'''HOW TO ITERATE OVER A PANDAS DATAFRAME '''
# df = pd.DataFrame(data=np.array([[1,2,3],[4,5,6],[7,8,9]]), columns=['A', 'B', 'C'])
# for index, row in df.iterrows():
#     print(row['A'], row['B'])