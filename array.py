# array using array module 
import array as arr

values = arr.array('i', [1, 2, 3, 4, 5])

print(values)

for i in range(0 , 5):
    print(values[i] , end = " ")

print("\n")

for x in values:
    print(x , end = " , ")

from array import *
val = array('i', [5, 6, 7, 8, 9])
print("\n")
print(val)


val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(val)
for i in range(0 , len(val)):
    print(val[i] , end = " ")

print("\n")

for x in val:
    print(x , end = " , ")

val = array('d', [1, 2, 3, 4, 5, 6 ,7 ,8, 9.5])
print("\n")
print(val)

val = array('u', ['a', 'b', 'c', 'd', 'e'])
print("\n")
print(val)

print(val.typecode)

val.reverse()
for i in range(0 , len(val)):
    print(val[i] , end = " ")
val.insert(2, 'z')
val.append('y')
val[3] = 'w'
print("\n")


copyArray = array(val.typecode, (a for a in val))

copyArray.pop(1)

copyArray.remove('w')
for i in range(0 , len(copyArray)):
    print(copyArray[i] , end = " ")

val = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])
#abc = val[startingindex : endingindex] end not included
a = val[1:5]
print("\n")
print(a)
b = val[2: -3]
print(b)
c = val[::-1]
print(c)
arr= array('i', [])
n = int(input("enter a number:"))
for i in range(0 , n):
    arr.append(int(input("enter a  next value:")))

for x in arr:
    print(x, end = " , ")
    