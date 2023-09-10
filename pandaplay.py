from pandas import DataFrame
import pandas as pd

# declaring a series
obj = pd.Series([2, 1, -7, 3])
print(obj)
print(obj.index)

obj2 = pd.Series([2, 1, -7, 3], index=['a', 'b', 'c', 'd'])
print(obj2)

dictionary = { 
    'Pears': 3,
    'Apples': 2,
    'Oranges': 4
}

obj3 = pd.Series(dictionary)
print(obj3)

fruits = [
    'Cherries',
    'Pears',
    'Apples',
    'Oranges'
]

obj4 = pd.Series(dictionary, index=fruits)
print(obj4)

print('a' in obj2)
print(pd.isnull(obj4))

obj5 = obj4

for i in range(len(obj4)):
    if pd.isnull(obj4[i]):
        obj4[i] = 0
        print(f'The element {i} was null')

# Dataframes

data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Jon', 'Doe', 'Jane', 'Docy', 'Billy'],
    'total buy': [22.4, 34.5, 99.2, 50.1, 12]
}

df = pd.DataFrame(data)
print(df)
print(df.name)
print(df['total buy'])
print(df.columns)
print(df.index)
print(df.values)


print(df.head(2))

location = ['Ewe', 'Igbo', 'Benin', 'Togo', 'Nigeria']
df['location'] = location
print(df.location)

df.index = df.name0
print(df)
print(df.index)
print(df.iloc[0])
print(df.iloc[-1])
