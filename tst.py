import pandas as pd
import numpy as np
import sqlite3
fruits = ['Orange', 'Grape', 'Apple', 'Banana', 'Pineapple', 'Avocado']
colors = ['Red', 'Green', 'Yellow', 'Blue']

df = pd.DataFrame({'id': np.arange(1, 1000001),
                   'fruit': np.random.choice(fruits, 1000000),
                   'price': np.random.randint(10, 101, 1000000),
                   'color': np.random.choice(colors, 1000000)})
print(df)
df.to_csv('df.csv', index=False)
