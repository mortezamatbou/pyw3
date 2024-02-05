import pandas as pd

dataset = {
    'firstName': ['Morteza', 'Hossein', 'Mahyar'],
    'lastName': ['Matbou', 'Allahmoradi', 'Farzam'],
    'age': [32, 25, 31],
    'field': ['IT', 'SW', 'HW'],
}

output = pd.DataFrame(dataset)
# print(output)

# Series
names = ['Morteza', 'Matbou', 32, 'IT']
student_names = pd.Series(names, index=['firstName', 'lastName', 'age', 'field'])
# print(student_names)

names = {'firstName': "Mahyar", "lastName": 'Farzam', 'age': 31, 'field': 'HW'}
student_names = pd.Series(names)
# print(student_names)
# print(student_names['firstName'])


### DataFrame
dataset = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
output = pd.DataFrame(dataset) # index=['a', 'b', 'c', 'd']
# print(output['calories'])

dataset = {
    'firstName': ['Morteza', 'Hossein', 'Mahyar'],
    'lastName': ['Matbou', 'Allahmoradi', 'Farzam'],
    'age': [32, 25, 31],
    'field': ['IT', 'SW', 'HW'],
}

df = pd.DataFrame(dataset)
# print(type(df.loc[0]))
df = df.loc[0:]['firstName']
# print(df)

data = {'firstName': "Morteza", 'lastName': 'Matbou', 'age': 32, 'field': 'IT'}
df = pd.Series(data)
# print(type(df))

data = {
  "calories": [420, 380, 390, 520],
  "duration": [50, 40, 45, 50]
}

df = pd.DataFrame(data)
# print(df.loc[[1,3]]) # return index 1 and 3
# print(df.loc[1:3]) # return items between 1 and 3

df = pd.DataFrame(data, index = ["day1", "day2", "day3", "day4"])
# print(df.loc[['day1','day3']])
# print(df.loc['day1':'day3'])

