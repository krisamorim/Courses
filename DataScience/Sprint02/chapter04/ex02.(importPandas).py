import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

atlas = [
    ['France', 'Paris'],
    ['Russia', 'Moscow'],
    ['China', 'Beijing'],
    ['Mexico', 'Mexico City'],
    ['Égypt', 'Cairo'],
]

geography = ['country', 'capital']

world_map = pd.DataFrame(data=atlas, columns=geography)

print(world_map)