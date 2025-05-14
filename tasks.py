#variables and datatypes
intvar=23
floatvar=23.32
boolvar=True
strvar="Hello,this is vrishin"
print(type(intvar),type(floatvar),type(boolvar),type(strvar))

#input/output
# name=input("enter your name \n")
# print("User Name is "+name)

#Operators
#arithmetic
a=1+1
a=a-1
a=a*3
a=a/2
a=a**2
a=a//1

#assignment
b=32
b+=2
b-=2
b*=2
b/=2
b%=10
b//=2
b%=2

#comparison

print(a==10) #false
print(a!=10)
print(a>10)
print(a<10)
print(a>=10)
print(a<=10)

#logical

print(a>10 and a<15)
print(a>18 or b>18)
print(not(a>18 and b>18))

#conditional statements
a=20
if(a>18):
    print("a can get driving license")
elif(a>16):
    print("a can apply for learners license")
else:
    print("grow up")

a=10

#loops
while(a>0):
    a -= 1
    if(a==8):pass #8 will be printed
    elif(a==6):continue #will not be printed
    elif(a==2):break # code exits
    print(a)


for i in range(0,5):
    print(i)

#Functions in python


def func(x=12):
    print(x)#default x=12

func()
func(1000)

#Lists, Tuple, Sets and Dictionaries

##List
li=[1,2,3,"a","b","c"]
#insert elements
li.append(23)
li.insert(2,"two")
print(len(li)) #length
#edit- update , remove
li[1]="one"
li.remove("a")
li.pop(3)
print(li[1])
print(li)
#comprehension
new_li=[x for x in li if type(x)==int]
print(new_li)

##tuples
fruit_tup=("apples","mango","lichi") #packing
print(fruit_tup[2])
(apples,mango,lichi)= fruit_tup #unpacking
print(apples)

##sets
myset={"apple","banana","cherry"}
myset.add("mango")
myset.discard("apple")
for i in myset:
    print(i)

##dictionaries
dict={
    "name":"vrishin",
    "age":21,
    "city":"ahmedabad",
}
print(dict["age"])
print(dict.keys())
dict["age"]=20
dict["role"]="intern"
dict.pop("age")


#Lambda Functions
multi=lambda x,y:x*y
print(multi(5,6))

#*args and **kwargs
def argfunc(*args):
    print(f"These all are arbitary arguments:- {args}") #stored as tuple
def kwargfunc(**kwarg): #stored as a dicitonary file
    print(kwarg["name"])

argfunc("2","vrishin","2004")
kwargfunc(name="vrishin")

#Map, Filter, and Reduce
def conv_to_int(x):
    return int(x)

str_li=["1","2","3","4"]
int_li=list(map(conv_to_int,str_li))
print(int_li)

 
from functools import reduce
res = reduce(lambda x, y: x + y, int_li)
print(res)

def is_even(x):
    return x%2==0

even_li=list(filter(is_even,int_li))
print(even_li)

#Importing Modules
import math
from math import sqrt
print(math.pi)
print(math.sqrt(16))

#Object-Oriented Programming (OOP) in python

class Animal:
    def make_sound(self):
        print("Animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

animal=Animal()
animal.make_sound() #Animal sound
dog=Dog()
dog.make_sound() #Bark
cat=Cat()
cat.make_sound() #Meow

#file handling

with open('test.txt', 'w') as file:
    file.write("Hello, this is a test file.\n")
    file.write("This is the second line.\n")

with open('test.txt', 'r') as file:
    content = file.read()
    print(content)
    file.close()

import os
os.remove("test.txt")

#error handling(try/except)

try:
    a=10/0
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No error occurred")
finally:
    print("This block always executed")

#iterators and generators

li=[1,2,3,4,5]
li_iter=iter(li)
print(next(li_iter)) #1
print(next(li_iter)) #2

def gen_func(n):
    for i in range(n):
        yield i*i

gen=gen_func(5)
gen_iter=iter(gen)
print(next(gen_iter)) 
print(next(gen_iter)) 
print(next(gen_iter)) 

#decorators
def decorator_func(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@decorator_func
def say_hello():
    print("Hello!")

say_hello()