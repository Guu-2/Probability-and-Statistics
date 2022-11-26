str = "Life is a mixture of ups and downs and one who has life must have seen various colours of life. Sometimes the colours are vivid and bright and sometimes they are just black and white. Life is a challenge and one who has the courage and strength to face it bravely is the one who goes through it and emerges as a great and successful person in life. Every person who has life is given various opportunities to make his life happy and prosperous and the one who understands this surely succeed in life. People who think that life is easy must know how people who don’t have a home to live and food to eat survive on this planet.Life places us in different situations of sorrow, grief, happiness, defeat, love, hatred, failure, success and much more. So one must realize this fact that life is not a bed of roses, it even has thorns which we need to accept so that we do not get into a state of depression and face life with courage and vigour.There are times when we are happy about certain events in life and celebrate such occasions with great enthusiasm but we should not forget that life will not always give you fruits without sowing seeds from time to time. So, make sure you always make the best possible efforts to gain success in life as without efforts you cannot achieve anything in life.One must accept this bitter truth that good times and bad times never last forever so one should always be ready to face difficulties in life even if he’s on the top of the world. And the one who is suffering from pain and misery should also know that there will be the time when all his sufferings will end and life will offer him new opportunities to succeed. Life is beautiful when you accept every little thing and ignore those that make you suffer. It’s our own perspective that makes our life happy or miserable, so one must have a positive attitude towards life to make it happening and worthy."
str = str.replace("." , " ")
str = str.replace("," , " ")


print(len(str.split(" ")))

arr = str.split()

list_count = []

set_count = {i for i in arr}

list_check = [i for i in set_count]

list_w = []

for i in set_count:
    list_count.append(arr.count(i))
    list_w.append(i)        


top30_w= []
top30_c = []
def max(a):
    index = 0
    max = list_count[0]
    for i in range(0 , len(list_count)):
        if(list_count[i] > max):
            max = list_count[i]
            index = i
    return index
      
      

for i in range(0, 30):
    top30_c.append(list_count[max(list_count)])
    top30_w.append(list_w[max(list_count)])
    list_count.remove(list_count[max(list_count)])

    
# top30.append(list_w[index])
# list_count.remove(list_count[index])
# # print(str.count(list_w[index]))  
# # print(max)
# print(len(list_count))
print(top30_c)
print((top30_w))      

# print(list_count)

# print(len(list_count))
# list_count1 = list_count.copy()

from matplotlib import pyplot as plt
import numpy as np

word = top30_w

frequency = top30_c

plt.figure("Ex3" , figsize=(15 , 5))



plt.plot(word , frequency , color = 'g' , marker = 'o')

plt.xlabel("Word" , fontsize = 12 , style = 'italic')
plt.xticks(np.array(word) , fontsize = 6)

plt.ylabel("Frequency" , fontsize = 12 , style = 'italic')
plt.yticks(np.array(frequency) , fontsize = 12 )


plt.title("Line grap of frequency 30 most common word" , fontsize = 14 , style = 'italic')

plt.show()



