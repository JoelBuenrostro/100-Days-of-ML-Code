# Cheat sheet

## Pip
### Install packages
```bash
pip install packagename
```
### Update packages
```bash
pip install packagename --upgrade
```
### Create a virtual environment
```bash
python3 -m venv myenvname
```


## Conda
### Create a conda virtual environment
```bash
conda create --name myenvname
```


## Basic Python
### Print
```python
print('Hello world')
```
### For loop
```python
for x in range(10):
    print(x)
```
### While loop
```python
x = 0
while x < 10:
    print(x)
    x = x + 1
```
### If
```python
x = 10
if x > 5:
    print(Greater than five)
else:
    print(Less than five)
```
### Functions
```python
def square(number):
    return number ** 2
```

## NumPy
### Array creation
```python
a = np.array([2,3,4])
```

## Pandas
### Read CSV
```python
f = pd.read_csv('path')
```
### Get dataframe column names
```python
df.columns
```
### Save dataframe to csv file
```python
df.to_csv('filename.csv', index=False, sep=',', encoding='utf-8')
```
### Read Excel files
```python
f = pd.read_excel('path', 'sheet')
```
### Select multiple columns at once
```python
df[['Name1', 'Name2', 'Name3']]
```
### Select multiple rows
```python
df.iloc[[0, 1, 2]]
```
