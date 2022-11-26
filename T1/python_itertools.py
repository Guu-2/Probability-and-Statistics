import itertools

#provide three Infinite Iterators


# Count(start, step): Trình lặp này bắt đầu in từ số “bắt đầu” và in vô hạn.
# Nếu các bước được đề cập, các con số sẽ bị bỏ qua nếu bước khác là 1 theo mặc định. 
# Xem ví dụ dưới đây để biết cách sử dụng với vòng lặp for in.

for i in itertools.count(0 , 2):
    print(i)
    if i == 10:
        break;

#cycle(iterable):: Trình lặp này in tất cả các giá trị theo thứ tự từ vùng chứa đã truyền. 
# Nó khởi động lại quá trình in từ đầu một lần nữa khi tất cả các phần tử được in theo cách tuần hoàn.

cnt = 0

for i in itertools.cycle('AB'): #có thể thay bằng list
    
    if cnt > 6:
        break;
    else:
        print(i , end = ' ')
        cnt +=1
        
#repeat (val, num): Trình lặp này in lặp đi lặp lại giá trị đã truyền vô số lần. 
# Nếu từ khóa tùy chọn num được đề cập, thì nó lặp lại số lần num.

print(list(itertools.repeat(9 , 4)))

print("The cartesian product using repeat:")
print(list(itertools.product([1, 2], repeat = 2)))
print()
   
print("The cartesian product of the containers:")
print(list(itertools.product(['cafe', 'dev', 'n'], '2')))
print()
   
print("The cartesian product of the containers:")
print(list(itertools.product('AB', [3, 4])))

from itertools import permutations
   
print ("All the permutations of the given list is:") 
print (list(permutations([1, 'cafedev'], 2)))
print()
print ("All the permutations of the given string is:") 
print (list(permutations('AB')))
print()
   
print ("All the permutations of the given container is:") 
print(list(permutations(range(3), 2)))

   
from itertools import combinations
   
print ("All the combination of list in sorted order(without replacement) is:") 
print(list(combinations(['A', 2], 2)))
print()
   
print ("All the combination of string in sorted order(without replacement) is:")
print(list(combinations('AB', 2)))
print()
   
print ("All the combination of list in sorted order(without replacement) is:")
print(list(combinations(range(2), 1)))

from itertools import combinations_with_replacement
   
print ("All the combination of string in sorted order(with replacement) is:")
print(list(combinations_with_replacement("AB", 2)))
print()
   
print ("All the combination of list in sorted order(with replacement) is:")
print(list(combinations_with_replacement([[(1) , (2) , (3)]], 3)))
print()
   
print ("All the combination of container in sorted order(with replacement) is:")
print(list(combinations_with_replacement(range(2), 1)))

import itertools
import operator
 
# initializing list 1
li1 = [1, 4, 5, 7]
   
# using accumulate()
# prints the successive summation of elements
print ("The sum after each iteration is : ", end ="")
print (list(itertools.accumulate(li1)))
   
# using accumulate()
# prints the successive multiplication of elements
print ("The product after each iteration is : ", end ="")
print (list(itertools.accumulate(li1, operator.mul)))
   
# using accumulate()
# prints the successive summation of elements
print ("The sum after each iteration is : ", end ="")
print (list(itertools.accumulate(li1)))
   
# using accumulate()
# prints the successive multiplication of elements
print ("The product after each iteration is : ", end ="")
print (list(itertools.accumulate(li1, operator.mul)))

#chain (iter1, iter2 ..): Hàm này được sử dụng để in tất cả các giá trị trong các mục
# tiêu có thể lặp lại lần lượt được đề cập trong các đối số của nó.

li1 = [1 , 2 ,3 , 4]

li2 = [5 , 6 , 7 , 8]

li3 = [9 , 10 , 11 , 12]

print("all values in mentioned chain are : " , end = " ")

print(list(itertools.chain(li1 , li2 , li3)))

# initializing list 1
li1 = [1, 4, 5, 7]
   
# initializing list 2
li2 = [1, 6, 5, 9]
   
# initializing list 3
li3 = [8, 10, 5, 4]
   
# initializing list of list
li4 = [li1, li2, li3]
 
# using chain.from_iterable() to print all elements of lists
print ("All values in mentioned chain are : ", end ="")
print (list(itertools.chain.from_iterable(li4)))


#compress(iter, selector): Trình lặp này chọn lọc các giá trị cần in từ vùng 
# chứa đã truyền theo giá trị danh sách boolean được truyền như các đối số khác. 
# Các đối số tương ứng với boolean true được in ra nếu không tất cả đều bị bỏ qua.
print ("The compressed values in string are : ", end ="")
print (list(itertools.compress('CAFEDEVN', [1, 0, 0, 0, 0, 1, 0, 0, 1])))


li = [0, 10 , 22 , 2 , 3, 1 , 4 , 6 , 7 , 9]

#in phần từ từ vị trí đầu tiên chia hết cho 2
# using dropwhile() to start displaying after condition is false
print ("The values after condition returns false : ", end ="")
print (list(itertools.dropwhile(lambda x : x % 2 == 0, li)))

li = [2, 4, 6, 7, 8, 10, 20]
   
# using takewhile() to print values till condition is false.
print ("The list values till 1st false value are : ", end ="")
print (list(itertools.takewhile(lambda x : x % 2 == 0, li )))

#filterfalse (func, seq): Như tên cho thấy, trình lặp này chỉ in các giá trị
# trả về false cho hàm đã truyền.

li = [2, 4, 5, 7, 8 , 6]
 
# using filterfalse() to print false values
print ("The values that return false to function are : ", end ="")
print (list(itertools.filterfalse(lambda x : x % 2 == 0, li)))


#islice(iterable, start, stop, step): Trình lặp này i chọn lọc các giá trị 
# được đề cập trong vùng chứa có thể lặp lại của nó được truyền dưới dạng đối số.
# Trình lặp này nhận 4 đối số, vùng chứa có thể lặp lại, vị trí bắt đầu, 
# vị trí kết thúc và bước nhảy.

# initializing list 
li = [2, 4, 5, 7, 8, 10, 20]
     
# using islice() to slice the list acc. to need
# starts printing from 2nd index till 6th skipping 2
print ("The sliced list values are : ", end ="")
print (list(itertools.islice(li, 1, 6, 2)))

#starmap (func., tuple list): Trình vòng lặp này nhận một hàm và danh sách 
# tuple làm đối số và trả về giá trị theo hàm từ mỗi bộ danh sách.

li = [ (1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10, 1) ]
   
# using starmap() for selection value acc. to function
# selects min of all tuple values
print ("The values acc. to function are : ", end ="")
print (list(itertools.starmap(min, li)))