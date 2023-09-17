import pandas as pd

data = {
    'Name': ['Ogbe', 'Oyeku', 'Iwori', 'Idi'],
    'Direction': ['East', 'West', 'North', 'South'],
    'Element': ['Fire', 'Water', 'Air', 'Earth'],
    'Color': ['Red', 'Blue', 'Yellow', 'Brown']
}

df = pd.DataFrame(data)
print(df)

friends_of_blue = df[df['Color'] == 'Yellow']
print(friends_of_blue)

friends_greater_than_West = df[df['Direction'] == "West"]
print(friends_greater_than_West)
