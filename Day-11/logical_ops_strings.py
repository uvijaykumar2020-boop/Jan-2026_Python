# Logical Operators using Strings
passport_name = 'Vijay kumar'
Drivers_ID = ''
#AND Operation
if passport_name and Drivers_ID:
    print('You are free to Fly')
else:
    print('Sorry ID is Mandatory')
# Other condition
passport_name = 'Ajay Kumar'
Drivers_ID = 'ABCDEF12345'
passport_name1 = 'Alex'
Drivers_ID1 = ''
if not(passport_name or Drivers_ID):
    print('You are free to Fly')
else:
    print('Sorry ID is Mandatory')

if passport_name1 or Drivers_ID1:
    print('You are free to Fly')
else:
    print('Sorry ID is Mandatory')


