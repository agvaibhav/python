# Python code to demonstrate namedtuple() and
# Access by name, index and getattr()
 
# importing "collections" for namedtuple()
import collections
 
# Declaring namedtuple()
Student = collections.namedtuple('Student',['name','age','DOB'])
 
# Adding values
S = Student('Nandini','19','2541997')
 
# Access using index
print ("The Student age using index is : ",end ="")
print (S[1])
 
# Access using name 
print ("The Student name using keyname is : ",end ="")
print (S.name)
 
# Access using getattr()
print ("The Student DOB using getattr() is : ",end ="")
print (getattr(S,'DOB'))




# program 2

>>> from collections import namedtuple
>>> Point = namedtuple('Point','x,y')
>>> pt1 = Point(1,2)
>>> pt2 = Point(3,4)
>>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
>>> print dot_product
11



#program 3

>>> from collections import namedtuple
>>> Car = namedtuple('Car','Price Mileage Colour Class')
>>> xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
>>> print xyz
Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
>>> print xyz.Class
Y


#program 4

from collections import namedtuple
N = int(input())
s=[None]*N
col = namedtuple('col',input().split())
for i in range(N):
    s[i]=col(*(input().split()))

sum_marks=0
for j in range(N):
    sum_marks = sum_marks+int(s[j].MARKS)

print("{0:.2f}".format(float(sum_marks/N)))
