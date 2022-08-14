  #This is single line comment
"""
This is a comment
written in
more than just one line
"""

#Single line assignment
from copyreg import constructor
from turtle import towards
from typing import Reversible
from wsgiref import handlers

#################################################################

x=44 #int
y=3.5 #float
name ='Rithick' #string
is_cool =True #boolean

print(x)

#Multiline assignment
x,y,name,is_cool =(19,7.3,'rithick',False)
a=x+y
print(is_cool,a)
print(name)
print(type(y))

#casting 
b=str(x)
print(type(b))

#concatination
#only string can be cooncatinated and int must be converted to string
print('Hello, My name is '+ name +'and i am ' + str(x) + ' years old')

#arguments by position
print('Hello, My name is {name}and i am {age} years old'.format(name=name,age=x))

#using F-string (only available in python 3.6+ versions)
print(f'Hello, My name is {name}and i am {x} years old')

#string methods
s='ajay'
#capitalize
print(s.capitalize())
#upper case
print(s.upper())
#lower case
print(s.lower())
#swapcase
print(s.swapcase())
#get length of string

print(len(s))
#replace string
print(s.replace('Rithick','hello'))
print(s)
#count
name='rithick'
print(s.count(name))

#################################################################

#Lists (changable)(looks like javascript Array)

list = ['one','two','three']

print(list,list[1])

# list constructor
# constr=list['may','june','july']
# print(constr)

list[2]="eight"
list.append('four')
list.sort()
list.remove("one")
list.insert(3,"six")
list.reverse()
list.pop()
print(list)

#################################################################

#Tuples(unchangable)
fruits=('apple','grape','orange')
print(fruits,type(fruits))

#get value
print(fruits[2])
#cannot change the value in tuple
# fruits[1]='mango'

#delete tuple
# del fruits
# print(fruits)

#################################################################

#Set(no duplicate)(looks like javascript object)
car_set={'bmw','audi','honda'}

# check if in set
print('bmw' in car_set)
#add duplicate
car_set.add('bmw')
#add to start
car_set.add('kia')
#remove
car_set.remove('audi')
# car_set.clear()
# del car_set
print(car_set)

#################################################################

#Dictionary(like javascript objects)
#create Dictionary
#Dictionary is a key/value pairs
person={
    'name':'rithick',
    'age':19,
    'student':'yes'
}
print(person,type(person))
#get values of dictionary(use brackets to get respective values or get() method)
print(person.get('student'))
print(person['name'])
#adding new values
person['phoneNumber']='8056285647'
print(person)
print(person.keys())
print(person.items())

#copy dictionary
new_person=person.copy()
new_person['city']='chennai'
print(new_person)

#remove items
del(person['age'])
person.pop('student')
print(person)

# person.clear()
# print(len(person))


#useing constructor
person1 =dict(name='frank',age=20,student='yes')
print(person1,type(person1))

#################################################################

#List of Dictionary(like javascript arrays)
movies =[{
    'name':'harry potter',
    'rating':10,
    'review':'amazing'
},{
    'name':'avengers',
    'rating':9,
    'review':'good'
},
{
    'name':'fast and furious',
    'rating':7.9,
    'review':'super'
}]

print(movies,movies[2])
# specific field 
print(movies[1]['review'])

#################################################################

#Function (use def to define a function)
def sayHello(name,age):
    print(f'hello i am {name} and i am {age} years old.')

sayHello('Jon',19)

#Return values
def getSum(num1,num2):
    total =num1 +num2
    return total

value = getSum(25,39)
print(value)

#Lambda function (like arrow function in javascript)
newSum = lambda num1 ,num2 : num1*num2
print(newSum(5,7))

#################################################################

# If/Else/Elif/Nested If statement and conditional statements 
# conditional(==,!=,>,<,<=,>=)
# Logical operator (and,or ,not)
#if
x=85
y=76
if x>y:
    print(f'{x} is greater than {y}')
    
#if else
if x>y:
    print(f'{x} is greater than {y}')
else:
    print(f'{x} is lesser than {y}')
   
#elif 
if x>y:
    print(f'{x} is greater than {y}')
elif x==y:
    print(f'{x} is equal to {y}')
else:
    print(f'{x} is lesser than {y}')
    
# Nested If
x=5
if x >2:
    if x<=10:
        print(f'{x} is greater than 2 and less than or equal to 10')
        
# # Using Logical operator(and ,or ,not)
if x >2 and x<=10:
        print(f'{x} is greater than 2 and less than or equal to 10')
if x >2 or x<=10:
        print(f'{x} is greater than 2 and less than or equal to 10')
if not(x==y):
        print(f'{x} not than or equal to {y}')

#################################################################

# Membership Operator (not , not in)(checks if present or not)
z= 7
numbers=[1,2,3,4,5]
if z in numbers:
    print(z in numbers)
    
if z not in numbers:
    print(z not in numbers)

# Identity operator (is ,is not)(checks both are equal or not)
j=3
k=4
if j is k:
    print(j is k)
if j is not y:
    print(j is not y)
    
#################################################################
    
# Loops (for loop,while)
bikes =['pulsar','yemaha','tvs','ola']
#For loop
for bikeCompany in bikes:
    print(f'current bike: {bikeCompany}')
    
#break
for bikeCompany in bikes:
    if bikeCompany == 'yemaha':
        break
    print(f'current bike: {bikeCompany}')

#continue
for bikeCompany in bikes:
    if bikeCompany == 'yemaha':
        continue
    print(f'current bike: {bikeCompany}')
    
#range
for i in range(len(bikes)):
    print(bikes[i])

for i in range(0,11):
    print(f'Numbers {i}')
    
#While loop (executes as long as the condition is true)
count =0
while count <=10:
    print(f'count: {count}')
    count +=1

#################################################################

#Modules(install using pip manager (including Django))
# import datetime
from datetime import date
# import time
from time import time
today = date.today()
# today =datetime.date.today()
timeStamp = time()
print(today,timeStamp)

#################################################################

# Classes (like javascript class but here we use (self) in place of (this) keywords)
#create class
class User:
    #constructor
    def __init__(self,name,email,age):
        self.name =name
        self.email =email
        self.age=age
        
    #methods
    def greeting(self):
        return f'My name is {self.name} and my age is {self.age} and my email is {self.email}.'
    
    def has_birthday(self):
        self.age+=1
        
    #Extand class
class Customer(User):
      #constructor
    def __init__(self,name,email,age):
        self.name =name
        self.email =email
        self.age=age
        self.balance = 0
    
 
    
    
#init user object
newName = User('Marco','marco@gmail.com',19)
print(newName.email,type(newName))

#running class method
newName.has_birthday()
print(newName.greeting())

#Random 
import random
print(random.randrange(1,500));

#multiline strings(use three double quotes)
a="""Hello this 
is multiline 
string statement"""
print(a[10])

#loop a string
for b in "Rithick":
    print(b)
#check string
print("is" in a)
#slicing
print(a[5:10])
print(a[9:])
print(a[:6])
print(a[-5:-8])
# The strip() method removes any whitespace from the beginning or the end:

c = " Hello, World! "
print(c.strip())
#Replace
print(c.replace("W","F"))

# The split() method splits the string into substrings if it finds instances of the separator:

print(c.split(","))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity,price,itemno))


#Git push
print("git push")
