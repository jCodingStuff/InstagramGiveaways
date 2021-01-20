import numpy as np
import pandas as pd

df = pd.read_csv('ids.csv')
print(df.shape)

usernames = list(df.username.to_numpy())
print()
print(usernames)
