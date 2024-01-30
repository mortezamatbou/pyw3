import pandas as pd

data = {
    'firstName': ['Morteza', 'Alireza', 'Saba', 'Nima'],
    'lastName': ['Matbou', 'Hosseini', 'Barzegar', 'Jafari'],
    'age': [32, 25, 28, 21],
    'field': ['IT', 'SW', 'HW', 'HW']
}

# define object as pandas dataframe
df = pd.DataFrame(data)
# print(type(df))
# print(df)

# print all rows from dataframe by firstName column
# print(df['firstName'])

# print all rows from dataframe by firstName and lastName columns
# print(df[['firstName', 'lastName']])

# print dataframe by index 0 and 2
# print(df['firstName'][[0, 2]])

# print all firstName by index 1 to 3 from dataframe
# print(df['firstName'][1:4])

del df
# declare dataframe with label
df = pd.DataFrame(data, index=[10, 20, 30, 40])
# print firstName column for rows by index 10 and 20
# print(df['firstName'][[10, 20]])
# print(df['firstName'][0:1])

del df

