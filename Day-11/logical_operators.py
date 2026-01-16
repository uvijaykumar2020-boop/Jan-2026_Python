#Logical operators in Python using AND, OR, NOT
# AND Operation
name = True
Age = 15
if Age > 14 and name:
    print("You are allowed to take driving lesson")
else:
    print("you are not allowed at this age")
# OR Operation
US_citizen = True
Green_card = False
if Green_card or US_citizen:
    print(" you have rights to vote in US")
else:
    print("Sorry, you are not eligible to participate for voting in US")

#Not Operation
name = True
salary = 100000 # in US$
if not(salary > 100000 or name):
    print(" Sorry you are not allowed for govt subsidies")
else:
    print(" you are allowed for govt subsidies")

#Another example for Not
person = False
Assets = 1000000
if not(Assets > 1000000 or person):
    print("Sorry, you are not allowed to buy house in this city")
else:
    print(" you are allowed to buy house in this city")


