import pandas as pd
import seaborn as sns

tips = sns.load_dataset('tips')

block = ('-' * 80)

print(block)
print('            TOP 5 ROWS OF TIPS DATASET')
print(block)
print(tips.head(5))
print(block)

print(block)
print('                 DATASET INFO')
print(block)
print(tips.info())
print(block)

print(block)
print('                 DATASET STATISTICS')
print(tips.describe())
print(block)

print(block)
print('                 NULL VALUES')
print(tips.isnull().sum())
print(block)