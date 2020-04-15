from matplotlib import pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

print(tips.head(5))

sns.set_style('darkgrid')
f, axes = plt.subplots(2, 2, figsize=(12, 6))

k1 = sns.kdeplot(tips.total_bill, tips.tip, ax=axes[0, 0])
k2 = sns.kdeplot(tips.tip, ax=axes[0, 1])
sc1 = sns.scatterplot(x='total_bill', y='tip', data=tips, ax=axes[1, 0])
sc2 = sns.scatterplot(x='tip', y='sex', data=tips, ax=axes[1, 1])

plt.show()