#Challenge #1: Write a Python script that removes all occurrences of a given element from a list.
fav_nums = [9, 99, 369, 96, 69, 9, 209, 99, 9, 109]
repeat_num = 9
unique_nums = [i for i in fav_nums if i!=repeat_num]
print(unique_nums)
#Challenge #2: Write a Python script that removes all duplicate elements from a list.
#Write a Python script that removes all duplicate elements from a list
vj_list = [10, 20, 10, 20, 30, 40, 50, 10, 20, 40, 50, 60, 10, 20]
unique_vj_list = []
for i in vj_list:
    if i not in unique_vj_list:
        unique_vj_list.append(i)
print(unique_vj_list)
"""
Challenge #3:
Given the string nums = '10,20,30,40,50', write a Python script that converts it into a list of
integers: [10, 20, 30, 40, 50].
"""
nums = '10: 20: 30: 40: 50'
num_list = [int(i) for i in nums.split(':')]
print(num_list)

