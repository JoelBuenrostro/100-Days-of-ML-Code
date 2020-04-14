import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

def plotter(x, y, name):
    plt.plot(x, y)
    plt.title(name)
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.show()

plotter(x, y, 'Plot')