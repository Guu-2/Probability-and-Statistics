import pandas as pd

from matplotlib import pyplot as plt

import numpy as np

data = pd.read_csv('iris.csv' , delimiter = ',')

A = data['sepal.length']

B = data['sepal.width']

fig , ax = plt.subplots(1 , 1)

ax.scatter(A , B , color = 'green')

ax.set_xlabel('sepal.length')

ax.set_ylabel('sepal.width')

ax.set_title('Ex1.1')

plt.show()


data = pd.read_csv('iris.csv' , delimiter = ',')

A = data['sepal.length']

fig , ax = plt.subplots(1 , 1)

ax.hist(np.array(A) , bins = 20)

ax.set_xticks([20])

ax.set_xlabel('marks')

ax.set_ylabel('sepal.length')

ax.set_title('Ex1.2')

plt.show()



