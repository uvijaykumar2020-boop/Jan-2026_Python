#To access each element/value in the list

lucky_numbers = [9, 109, 369, 999, 0, 209, 99]
print(lucky_numbers)
for lky in lucky_numbers:
    print(lky)
# here we wanted to check specific lucky number in the list or not using condition
vj_fav_lky = 999
if vj_fav_lky in lucky_numbers:
    print(f'{vj_fav_lky} found in the lucky numbers')
else:
    print(f'{vj_fav_lky} not in the lucky numbers')
dj_fav_lky = 9
if dj_fav_lky in lucky_numbers:
    print(f'{dj_fav_lky} found in the lucky numbers')
else:
    print(f'{dj_fav_lky} not in the lucky numbers')
tj_fav_lky = 8
if tj_fav_lky in lucky_numbers:
        print(f'{tj_fav_lky} found in the lucky numbers')
else:
        print(f'{tj_fav_lky} not in the lucky numbers')

# Creating new list of the o/p based on the condition

our_fav_list = []
for fav_list in lucky_numbers:
    if fav_list > 9:
        our_fav_list.append(fav_list)
        print(our_fav_list)
print(type(our_fav_list))

