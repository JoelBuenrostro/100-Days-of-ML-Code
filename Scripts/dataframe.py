import numpy as np
import pandas as pd

data = np.array([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]])
rows = ['a', 'b']
cols = ['One', 'Two', 'Three', 'Four', 'Five']

df = pd.DataFrame(data, index=rows, columns=cols)

print(df)