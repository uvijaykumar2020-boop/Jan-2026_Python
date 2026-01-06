# converting string to tuple
name = tuple("Vijay Kumar U")
print(name)

#unpack of tuple
num = 100, 200, 300
print(type(num))

num_1 = 100,
print(type(num_1))

# Nested Tuple
matrix = [[10, 20, 30],
          [40, 50, 60],
          [70, 80, 90]]
print(matrix)
# to fetch the number 60
print(matrix[1][2]) # first set [10, 20, 30] is considered and index value as 0.
# So we have to select the index value 1 and then followed by the with in the set 40, 50, 60, here 60 element is in the 2 index place