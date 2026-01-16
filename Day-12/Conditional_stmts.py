# Understanding the Syntax of conditional statements
"""
if condition1:
    # True block
    # statement-1
elif condition2:
    # False block
    # statement-2
elif condition3:
    # True block
    # statement-4
else:
    # else statements
    print()

"""
"""
Syntax Reminder
if_some_condition is true:
    # print statememt if the condition is met
elif other_condition is true:
    # print statement2 is this condition is met
else:
    print statement3 if neither of above statements met
   
"""

Age = 15
if Age >= 18:
    print(' you are an adult')
elif Age <18 and Age>=13:
    print('You are Teenager')
else:
    print('you are still Child ')
