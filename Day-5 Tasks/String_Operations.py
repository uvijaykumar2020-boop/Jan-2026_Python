# String Operations - Indexing and Concatenating
# Indexing value always starts from 0
#Indexing start from -1 from the reverse and string is immutable
# name = "Vijay Kumar U"
# print(name[0])
# print(name[-1])
# print(name[-2])
# print(len(name))

# Concatenating means joining two or more strings
# message = "Hello World "
# message_1 = "Welcome to AI Era, how can we help you?"
# Greeting_mesg = message + message_1
# print(Greeting_mesg)
# print('version ' + str(2.0))
#
# name = "vijay kumar"
# print(name.upper())

# nums = [1, 7, 8, 14, 21, 30, 50]
#[num for num]
# print(nums_div_7)

ai_team = ['alice', 'Bob', 'Charlie']
data_team = ['alice', 'Bob', 'jim']
comm_names = [name for name in ai_team if name  in data_team]
print(comm_names)


