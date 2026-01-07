# dictionary data type
# dictionary is key-value pair, mutable, comma is differentiator b/w elements and is unordered.
from email.policy import default

person = {
    "name" : "Vijay",
    "Age" : 35,
    "role" : "Sr Data Protection Engineer",
    "work_location": "Los Angeles"
    }
print(type(person))
print(person)

##Adding new key-value pair to existing dictionary
print(person)
person['India_home_address'] = "Kurnool"
print(person)

##Best Practices for dictionary data type
##use get() as a safe method to avoid any errors.
# Also avoid duplicate keys
print(person.get('India_house_address')) # avoiding script error & displaying none.
print(person.get('work_location'))
print(person.get('name'))
print(person.get('salary', 'correct chesuko :-)'))
