from copy import copy
from neighborlib import swap, invert, insert, reverse_insert

x = [1,2,3,4,5,6]
xprim = copy(x)
i = 2
j = 5

swap(x,i,j)
print(x)
swap(x,i,j)
print(x)
print('')

invert(x,i,j)
print(x)
invert(x,i,j)
print(x)
print('')

insert(x,i,j)
print(x)
reverse_insert(x,i,j)
print(x)
print('')

for i in range(len(x)):
    for j in range(i+1,len(x)):
        print (str(i) + ", " + str(j))
        insert(x,i,j)
        reverse_insert(x,i,j)
        if (x != xprim):
            print("Blad!")
            print(x)