# List Operations: Concatenation
#Combination of two or more lists into a single list is called concatenation
list1 = [100, 200, 300, 400, 500]
print(list1)
print(type(list1))
list2 = list1 + [500, 600, 700, 800]
print(list2)
list3 = list1 + list2 + [900, 1000]
print(list3)

#slicing is called the extraction the values using index position, starting from 0 in the begining
list10 = [10, 20, 30, 40, 50, 60]
print(list10)
print(list10[0:3])
print(list10[1:])
print(list10[-1])
print(list10[::-1])
print(list10[1::2])
print(list10[::2])



