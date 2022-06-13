import pandas as pd
import numpy as np

prices = [10.1,20,52,45]

p = pd.Series(prices)

print(p)
print(p.max())
print(p.min())
print(p.mean())