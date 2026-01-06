# # List Comprehension
# # Practice on numbers divisible by 10
# numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50]
# num_div_by_10 = [num for num in numbers if num % 10 == 0]
# print(num_div_by_10)
#
# ## To extract the common names from the below two variables
# team_a = ['vijay', 'lalitha', 'maneesh', 'taman']
# team_b = ['bharath', 'shruthi', 'pranav', 'skanda', 'maneesh']
# comm_names = [name for name in team_a if name in team_b]
# print(comm_names)
#
# ## To filter the numbers which are greater than or equal to 100 from the below list
# numbers = [20, 30, 100, 282, 10, 6, 100, 19, 1900, 16000]
# num_gr8_100 = [num for num in numbers if num >= 100]
# print(num_gr8_100)
# num_less_100 = [num for num in numbers if num <=100]
# print(num_less_100)

# Practice on tuple data type and they are immutable
numbers = (100, 200, 300, 400, 500)
print(type(numbers))
# To fetch the number from any index value starting from 0 at the begining
print(numbers[0])
print(numbers[-1])
print(numbers[::-1])
# Convert datatype from list to tuple
numbers_1 = [99, 199, 299, 399, 499]
print(numbers_1)
print(type(numbers_1))
print(type(tuple(numbers_1)))
print(numbers_1)
# convert datatype from tuple to list
num_2 = (1, 2, 3, 4, 5)
print(type(num_2))
print(num_2)
print(type(list(num_2)))
print(num_2)
print(type(num_2))


