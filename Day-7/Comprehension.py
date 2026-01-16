#Comprehension Syntax
#expression for loop and if condition

numbers = [10, 100, 200, 300, 400, 500]
numbers1 = [num for num in numbers if num > 10]
print(numbers1)
new_numbers = []
for num in numbers:
    if num > 100:
        new_numbers.append(num)
        print(new_numbers)
# with Comprehension
new_numbers1 = [num for num in numbers if num > 200]
print(new_numbers1)
# To convert in to set
new_numbers2 = {num for num in numbers if num > 200}
print(new_numbers2)
print(type(new_numbers2))
# to print each number of powersquare and assign to new list with condition number greater than 10
new_numbers3 = {num **2 for num in numbers if num > 10}
print(new_numbers3)





