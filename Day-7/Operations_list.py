#reverse operation
from operator import truediv

list = [10, 20, 30, 8, 112, 834, 0, 34, 294, 54]
list.reverse()
print(list)

# sorting example
numbers = [1, 0, 65, 2, 39, 76, 20, 100, 1000, 4, 24, 63]
numbers.sort()
print(numbers)

# default behavior of sorting is ascending
# print ors sort the values in descending order
numbers.sort(reverse=True)
print(numbers)

# sorted operation also exists
num10 = [10, 0, 2, 200, 2000, 21, 12]
sortednumbers = sorted(num10)
print(num10)
print(sortednumbers)
# Appending new element to a list
list1 = [10, 20, 30, 40, 60]
list1.append(50)
print(list1)
list2 = sorted(list1)
print(list2)
print(sorted(list1))
# to add multiple new elements at the end of the list
print(list2)
list2.extend([70, 80, 90, 100])
print(list2)
# To remove all the elements from the defined list
l1 = [1, 2, 3, 4, 5, 6]
print(l1)
l1.clear()
print(l1)
# to remove  last element from the list and return
l1 = [100, 200, 300, 1000]
print(l1)
l2 = l1.pop()
print(l2)



