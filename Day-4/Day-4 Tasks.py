# print("Welcome to AI bot \n your Virtual Assistant \n how can we help")
# print('\\ Python is good program lang')

# Basic Python Relational Operators or Comparision and assignment operators.
a = 2
b = 7
print(a)
print(id(a))
print(b)
print(id(b))
print(a == b)
print(a != b)

a = a+b
print(a)
print(id(a)) # it prints the memory location. If values gets change, memory location as well changes.
print(id(b))

a -= 2
print(a)
print(b)
print(id(a))
print(id(b))

b *= 10
print(b)
print(a)
print(id(b))
print(a ==b)
print(a > b)
print(a < b)
a *= 10 # assignment operators
print(a)
print(b)
print(a != b)
print(a >=b) # if any operator is true, irrespective of another - output results true only
print(a <=b)

a /= 7
print(a)

x = 20
print(x > 10 and x <=20)
print(x <=10 and x !=30)
print(x <=10 and x ==20)
print(not(x>10)) # not used for less than or greater than.

# Example to show the append to the value set
set = [10, 20, 30, 40]
print(set)
print(id(set))

# Appending to the existing set
set.append(50)
print(set)
print(id(set))

# When you append to same, memory doesn't change. it is mutable option
# when you define some value as it was immutable and perform any operation, memory also changes.
p = 10
q = 20
print(p)
print(q)
print(id(p))
print(id(q))
p += 10
q += 20
print(p)
print(q)
print(id(p))
print(id(q))



















