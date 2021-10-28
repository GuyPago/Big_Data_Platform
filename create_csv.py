import pandas as pd
import numpy as np
import sqlite3
fruits = ['Orange', 'Grape', 'Apple', 'Banana', 'Pineapple', 'Avocado']
colors = ['Red', 'Green', 'Yellow', 'Blue']
rows = 1000000

df = pd.DataFrame({'id': np.arange(1, rows + 1),
                   'fruit': np.random.choice(fruits, rows),
                   'price': np.random.randint(10, 101, rows),
                   'color': np.random.choice(colors, rows)})
df.to_csv('df.csv', index=False)
