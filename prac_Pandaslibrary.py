import pandas as pd

# what is pandas in python

# Pandas is a Python library used for data analysis and data manipulation in table format (rows and columns).

# Simple meaning:
# Pandas helps us to:

# Store data
# Organize data
# Clean data
# Analyze data easily

# Real-Life Example

# Suppose a company has:

# Customer data
# Sales data
# Profit reports

# pandas helps analyze:

# Total sales
# Best customers
# Monthly profit
# State-wise reports


# example data to learn pandas library
data = {

            'Name':['Imran','Ramesh','Dhruv','Abdul','Aryan'],
            'Age':[16,21,22,22,8],
            'salary':[10000,20000,30000,25000,100]
}

df = pd.DataFrame(data)
# print(df)

# basic details of dataframe 

#print(df.head(2))# head give = top two data
#print(df.tail(2))#tail give =  bottom two value
#print(df.info()) #info give = table iformation
#print(df.describe()) #describe give =  statistical detail on data
#df1 = df.rename(columns={'Salary':'Monthly_salary'})
#print(df1) # here rename = could change column value
#print(df1.shape)# here shape give = row and column


# load and save from csv file 

# df1 = df.to_csv('my_data.csv',index=False)
# print(df1)
# df1 = pd.read_csv('my_data.csv')
# print(df1)

#select only column 

# df1 = df[['Name']]
#print(df1) 


#select multiple column

# df1 = df[['Name','Age']]
#print(df1) 

#select only row
#loc - local base on index

# df1 = df.loc[df.Name == 'Ramesh']
#print(df1) 
# df1 = df.loc[(df.Name == 'Ramesh') & (df.salary >= 20000)]
# print(df1) 

# index value base

# df1 = df.loc[0:2]
# print(df1)
# df1 = df.iloc[0]
# print(df1)
# df1 = df.iloc[0:2] #start[start:stop:step]
# print(df1)

# df1 = df.rename(columns={'salary':'monthly_salary'},inplace=True)
# print(df1)
# print(df)


# Filter data 

# df1 = df[(df.monthly_salary > 20000) & (df.Age > 20)]
# print(df1)
# df1 = df.where(df.monthly_salary >= 30000)
# df1 = df.where((df.Age >= 18) & (df.monthly_salary >= 20000))
# print(df1)


# Add new column


# df['Team'] = ['CEO','HR','DT','DS','CA']
# print(df)
# df['Bonus'] = df.monthly_salary * 0.25;
# print(df)


# Add  row value
# df1 = df.loc[5] = ['Ansari',24,60000,'PB',8000]
# print(df)


# Update dataframe value


# df1 = df.loc[df.Name == 'Ramesh','monthly_salary'] = 60000
# print(df)
# # using index value
# df1 = df.loc[0,'monthly_salary'] = 50000
# print(df)


# delete row and colum value 

# delete row 
# df1 = df.drop(df[df.Name == 'Ansari'].index,inplace = True)
# print(df)
# #delete row using index value
# df2 = df.drop(4,axis=0,inplace = True)
# print(df)

#delete column
# df1 = df.drop(['Bonus'],axis = 1,inplace = True)
# print(df)

# delete multiple column
# df2 = df.drop(['Bonus','Team'],axis = 1,inplace = True)
# print(df)


# Sort dataframe value in Ascending using sort_values() method

# df1 = df.sort_values('monthly_salary')
# print(df1) 


# Sort dataframe value in descending using sort_values() method

# df1 = df.sort_values('monthly_salary',ascending=False)
# print(df1) 


# Working with date time using method to_datetime()

# df['doj'] = ['2024-01-01','2022-01-02','2021-03-01','2026-06-01']
# print(df)
# print(df['doj'].dtype)
# df['doj'] = pd.to_datetime(df['doj'])
# print(df)
# print(df['doj'].dtype)


# df['doj2'] = ['01-02-2025','01-03-2023','01-02-2024','01-02-2022']
# print(df)
# print(df['doj2'].dtype)

# formate date 

# df['doj2'] = pd.to_datetime(df['doj2'],format='%d-%m-%Y')
# print(df)
# print(df['doj2'].dtype)

# df1 = df.drop('doj2',axis=1,inplace = True)
# print(df)


# print(df['doj'].dt.year)
# print(df['doj'].dt.month_name())
# print(df['doj'].dt.day)
# print(df['doj'].dt.day_name())

# df['month'] = df['doj'].dt.month
# print(df)
# df1 = df['month'].value_counts()
# print(df1)
# count how many 1st month in dateframe
# df1 = df[df.month == 1].value_counts()
# print(df1)


# Aggration and groupby


# df1 = df.groupby('month')['monthly_salary'].sum()
# print(df1)
# df1 = df.groupby('month').agg({'monthly_salary':'mean','Name':'count'})
# print(df1)
# print(df)



# Concanate and mearj datafram(join)


# df1 = pd.DataFrame({'ID':[1,2,3],'Name':['A','B','C']})
# print(df1)
# df2 = pd.DataFrame({'ID':[1,2,3,4],'Score':[99,88,5,55]})
# print(df2)
# Using concat() method
# df3 = pd.concat([df1,df2])
# print(df3)
# df3 = pd.concat([df1,df2],axis=1)
# print(df3)


# df3 = pd.merge(df1,df2,how='inner')
# print(df3)
# df3 = pd.merge(df1,df2,how='left')
# print(df3)
# df3 = pd.merge(df1,df2,how='right')
# print(df3)


# df3 = df.rename(columns={'monthly_salary':'salary'},inplace=True)
# print(df3)

# Prompt to filter salary > 70000 and January employees
# df3 = df[(df.month == 1) & (df.salary > 10000)]
# print(df3)

# Using query method
# df3 = df.query("(month == 1) & (salary >= 10000)")
# print(df3)

# import data 

# df2 = pd.read_csv('test_data.csv')
# print(df2)

#Check for Missing Values
#print(df2.isnull())
#How many missing value to column
#print(df2.isnull().sum())
#print(df2.isna)
#fill missing value 
#print(df2.fillna(20000))