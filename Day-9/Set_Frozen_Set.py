# # set is mutable, unordered and unique elements.
# num = {100, 200, 300, 400, 500, 600}
# print(type(num))
# print(num)
#
# # Creating set with different data types
#
# mix_details = {100, 'vijay', 5.7, 35, 'UnitedStates', 'IT Professional', ' 13'}
# print(type(mix_details))
# print(mix_details)
#
# # how to add other elements to existing set.
# mix_details.add(101010)
# print(mix_details)
#
# # to remove some elements from set
# mix_details.remove(101010)
# print(mix_details)
#
# # accessing all the elements from the set
# for i in mix_details:
#     print(i)
#
# # Checking specific element from the set
# if 35 in mix_details:
#     print( "35 is present in mix_details")
# else:
#     print( "35 is not present in mix_details")
################################################################
#Set Comprehension
range = {10, 5, 20.0, 19.9, 29, 36, 200, 632}
gr8_range = {i for i in range if i >=19.9}
less_range = {j for j in range if j <=19.9}
print(gr8_range)
print(less_range)
print(type(gr8_range))