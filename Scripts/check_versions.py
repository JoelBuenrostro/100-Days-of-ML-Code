import sys
import numpy
import matplotlib
import pandas
import sklearn
import plotly
import cufflinks
import seaborn

line = ('=' * 79)
space = (' ' * 79)

print(line)
print('  Python  ')
print(line)
print('  Python : {}'.format(sys.version))
print(space)

print(line)
print('  Numerical  ')
print(line)
print('  Numpy : {}'.format(numpy.__version__))
print('  Pandas : {}'.format(pandas.__version__))
print(space)

print(line)
print('  Visualization  ')
print(line)
print('  Matplotlib : {}'.format(matplotlib.__version__))
print('  Seaborn : {}'.format(seaborn.__version__))
print('  Plotly : {}'.format(plotly.__version__))
print('  Cufflinks : {}'.format(cufflinks.__version__))
print(space)

print(line)
print('  Machine Learning  ')
print(line)
print('  Sklearn : {}'.format(sklearn.__version__))
print(space)