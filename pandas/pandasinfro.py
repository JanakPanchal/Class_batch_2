import pandas as pd
from openpyxl.workbook import Workbook
# Pandas DataFrame.append()
#new branch
# Add the rows of other dataframe to the end of the given dataframe.
# Pandas DataFrame.apply()
# Allows the user to pass a function and apply it to every single value of the Pandas series.
# Pandas DataFrame.assign()
# Add new column into a dataframe.
# Pandas DataFrame.astype()
# Cast the Pandas object to a specified dtype.astype() function.
# Pandas DataFrame.concat()
# Perform concatenation operation along an axis in the DataFrame.
# Pandas DataFrame.count()
# Count the number of non-NA cells for each column or row.
# Pandas DataFrame.describe()
# Calculate some statistical data like percentile, mean and std of the numerical values of the Series or DataFrame.
# Pandas DataFrame.drop_duplicates()
# Remove duplicate values from the DataFrame.
# Pandas DataFrame.groupby()
# Split the data into various groups.
# Pandas DataFrame.head()
# Returns the first n rows for the object based on position.
# Pandas DataFrame.hist()
# Divide the values within a numerical variable into "bins".
# Pandas DataFrame.iterrows()
# Iterate over the rows as (index, series) pairs.
# Pandas DataFrame.mean()
# Return the mean of the values for the requested axis.
# Pandas DataFrame.melt()
# Unpivots the DataFrame from a wide format to a long format.
# Pandas DataFrame.merge()
# Merge the two datasets together into one.
# Pandas DataFrame.pivot_table()
# Aggregate data with calculations such as Sum, Count, Average, Max, and Min.
# Pandas DataFrame.query()
# Filter the dataframe.
# Pandas DataFrame.sample()
# Select the rows and columns from the dataframe randomly.
# Pandas DataFrame.shift()
# Shift column or subtract the column value with the previous row value from the dataframe.
# Pandas DataFrame.sort()
# Sort the dataframe.
# Pandas DataFrame.sum()
# Return the sum of the values for the requested axis by the user.
# Pandas DataFrame.to_excel()
# Export the dataframe to the excel file.
# Pandas DataFrame.transpose()
# Transpose the index and columns of the dataframe.
# Pandas DataFrame.where()
# Check the dataframe for one or more conditions.
# Check the dataframe for one or more conditions.
list = [[10, 20,40 ,50],[20 , 30 , 40 ,50]]
list2 = [30,40,50,30]
df = pd.DataFrame(list)
print(df)

d = pd.DataFrame([[7, 8], [9, 10]], columns = ['x','y'])
d2 = pd.DataFrame([[11, 12], [13, 14]], columns = ['x','y'])
d = d.append(d2)
print(d)
print(d.count())
print(d.median())
# print(df.where(11))
print(d['x'][1])
# #create excel
# writer = pd.ExcelWriter('Test.xlsx')
# #append data in excel
# print(d.to_excel(writer))
# #save file
# writer.save()

x = {"Name" :[ "Janak", "Roy", "Mohit", 'Rohan'], "Location" : ["Us", "Uk", "Canada" , "Uk"] }
d1 = pd.DataFrame(x)
print(d1)

p = pd.read_json("demo.json")
print(p)

p = pd.read_excel("Test.xlsx")
print(p.sum())
name = ["a","c","d","z"]
print(sorted(x["Name"]))

# import sqlite3
# con = sqlite3.connect("database.db")
# pd.read_sql_query()


#https://git-scm.com/downloads