import pandas as pd

import numpy as np

from matplotlib import pyplot as plt

data = pd.read_csv('company_sales_data.csv' , delimiter=',')

# print(data)

month = data['month_number']

# print(month)

total_profit = data['total_profit']

# print(total_profit)

plt.figure('Ex2.1',figsize=(9 ,4 ))

plt.plot(month, total_profit , color = 'violet' , marker = 'o' )

plt.xticks(np.array(month))
plt.yticks(np.array(total_profit))

plt.xlabel('Month')
plt.ylabel('Total profit')

plt.title('Ex2.1')

plt.show()

toothpaste = data['toothpaste']

fig , ax = plt.subplots(1 , 1)

ax.scatter(month, toothpaste , color = 'orange')

ax.set_xlabel('Month')
ax.set_xticks(np.array(month))

ax.set_ylabel('Toothpaste')

ax.set_title('Ex2.2')

plt.show()

facecream = data['facecream']

facewash = data['facewash']

fig , ax= plt.subplots(1 , 1)

data = [list(facecream) , list(facewash)]

ax.bar(month + 0.0 , data[0] , color ='b' , width= 0.25)

ax.bar(month + 0.25 , data[1] , color = 'g' , width = 0.25)

ax.set_xticks(np.array(month))

ax.legend(labels = ['facecream','facewash'] )

ax.set_xlabel('Month' , fontsize = 17 , style = 'italic')

plt.show()

