print("Hello world")
'''print('Comment syntax') # This is a comment
'''  # For multiline comments
# Python has no command for declaring a variable it is created the moment we assign a value to it
x=5
y="John"
print(x,y,"This is variable print")
# To specify a type of a variable we can use typecasting
x=str(3)
y=int(3)
z=float(3)
print(type(x),type(y),type(z))
# Both single quote and double quote works as same
# variable names are case sensitive
# variable name can only start with alphanumeric digits and underscore sign
# myName=> camelCase MyName=>PascalCase  my_name=>snake_case
x,y,z="Aayush","Abhishek","Ozil"
print(x,y,z)
# or
x=y=z="abhishek" #if we want to assign same variable to different
print(x,y,z)
# If we have a collection of values in list, tuple then we can unpack that values in variables.
# It is called unpacking
fruits=["Mango","Apple","Pomegranate"]
x,y,z=fruits;
print(x,y,z);
# To output multiple variables seperated by comma
# we can also use '+' sign but if we combine a number with a string then python may give an error
# To create a global variable from inside a function we can use global keyword
def myfunc():
    global x
    x="fantastic this is a global variable"
myfunc()
print("Global Variable: "+x)
# Data types
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

x=1j #denoting a complex number
print(type(x))
#a=int(x)
# gives error because we cannot convert complex number to any another numbers

# python does not have a random function but it has a built in random module
import random
print(random.randrange(0,100,1))

# Python Strings
# we can assign a multiline strings using triple quotes """"""
x='''Here is a multiline
variable
here we go'''
print(x)

# python does not have character type but string is treated as array of characters
# starts with 0
a="Hello World"
print(a[0])
for x in a:
    print(x)
# to find out the length of string we get
print(len(a))
# To check a string we have
txt="  The best things in life are free"
print('best' in txt) #outputs a boolean value
# As it is a boolean value we can use in keyword for if conditions
# Also we can use 'not in' statement for negation of above statement
# Slicing Strings
# We can return a specific part of a string by using slicing
print(txt[2:])
# Python modify strings
print(txt.upper()) # .lower
# Strip method is used to remove whitespace from beginning or end of a text
print(txt.lstrip())
# to replace string we can use replace function
print(txt.replace('The','A'))
# To split a string into lists we use split
print(txt.split(' '))
# String concatenation we can use +
txt='My name is '
txt=txt+'Aayush'
print(txt)
# Escape characters are used after backslash '\'
# Python lists
myList=['Apple','Banana','Mango','Strawberry']
print(myList)
# For list length
print(len(myList))
# List items can be of any datatype
print(type(myList))
# We can also use list() constructor for creating lists
myList2=list(('Apple','Banana','Mango','Strawberry'))
print(myList2)
print(myList[2:4])
if 'Apple' in myList: # To search a item we can use in keyword
    print('Apple is present in myList')

# We can simply change the item in the list by using index of a particular item
myList[1]='Pomegranate'
print(myList)
# Also to change the range of values we can simply
myList[1:2]='Banana','Cherry'
print(myList)
# To insert a value without replacing any other items on the lists we can use the insert keyword
myList.insert(2,'Watermelon')
print(myList)
# We can also use append('value to append a value at the end of the list')
myList.append('Papaya')
print(myList)
# To append elements from another list we can use extend;
myList.extend(myList2)
print(myList)
# Extend method does not necessarily has to append only the lists it can also append tuple
# To remove an item from a list we can use remove method
myList.remove('Strawberry')
print(myList)
# TO remove specified index we can use pop method
myList.pop(7)
print(myList)
# If the index is not specified then the last item will be removed
myList.pop()
print(myList)
# del keyword is also used to remove specified index from a list
# Or it can delete the list completely
del myList[1]
print(myList)
# myList.clear() clears all the items on the list but doesn't delete the whole list
# Looping through a list
for x in myList:
    print(x)

# To loop through index numbers we have
for i in range(len(myList)):
    print(i)

# Looping through list comprehension
[print(x) for x in myList if 'a' in x]
print(myList)
newList=[]
for x in myList:
    if "a" in x:
        newList.append(x)
print(newList)

# Sort Lists
print(myList)
myList.sort()
print(myList)
# for descending order of sorting we do reverse=true attribute
myList.sort(reverse=True)
print(myList)
# We can join two list simply by using '+' operator or by using append module or extend
# Python  tuples
myTuple=('Mango','Banana','Apple')
print(myTuple)
print(type(myTuple))
# Tuple is a collection which is ordered and unchangeable
# To create a tuple with a single value we should place a comma after an item
# We can also use tuple constructor to create a tuple just like in lists
# Accessing of item in tuple is same as of lists
# To change a value in a tuple we can simply convert it into list and change the value and then convert it back to tuple
tupleList=list(myTuple)
print(tupleList)
tupleList.append('Orange')
tupleList.append('Orange')
myTuple=tuple(tupleList)
print(myTuple)
# but we can add one tuple with another also

# Unpacking in Tuples is same as in list but we have to put a small bracket outside
(x,y,z,*a)=myTuple
print(x,y,a,z)
print(myTuple.count('Orange'))

# Set in python
mySet={'Apple','Banana','Orange'}
# Once a set is created we cannot change items but we can add new item
mySet.add('Pineapple')
print(mySet)
# or to combine two set we can use .update We can remove an item simply by .remove or .discard(value) difference
# between remove and discard is that if item does not exists then remove will throw an error but discard doesn't Also
# .pop() also removes an item i.e. last item but as set is not ordered it returns the removed item
# clear method empties the set where as del keyword deletes the set completely
# union method returns a new set containing the combined values of both sets whereas update inserts item of another set
# intersection_update method will only keep the items that are already in both sets
# intersection will return a new set

# Python Dictionaries
myDict={
    'name':'Aayush',
    'roll':181509,
    'college':'NCIT'
}
print(myDict)
# to access the elements which are in key:value pair we can access then by using key for each item
print(myDict['name'])
# we can also get the same result by using get keyword
print(myDict.get('name'))
# to get all the keys in dictionary we can use keys() method
print(myDict.keys())
# we can also add new items in the dictionary by assigning a value to a key randomly outside the declaration also
myDict['Surname']='Regmi'
print(myDict)
# to return values we can simply use values method
print(myDict.values())
# The following method returns the key value pairs as a list of tuples
print(myDict.items())
if 'name' in myDict:
    print('true')
# we can also update the values in dictionary by using update
myDict.update({'bike':'F-z V3'})
print(myDict)
# pop method removes the specified value from a dictionary
myDict.pop('bike')
myDict.popitem()
print(myDict)
# Looping through a dictionary
# To loop through both key and values we can use
for x,y in myDict.items():
    print(x,y)
# We should use copy method to copy a dictionary to another dictionary
# If we just simply assign a value of one dict to another then the new dictionary will just be a instance of old one

# Python functions
# function is defined using def keyword
# def my_function(*args):
#     print('This is a function',args[2])

# my_function()
# if we have multiple arguments then we can also pass by putting an asterisk in the argument
# my_function('Aayush',181509,'NCIT')
# We can also send keyword arguments

def my_function(**args):
    print('This is a function',args['name'])

my_function(name='Aayush',roll=181509,college='NCIT')
# It is also called as kwags i.e. keyword arguments

# Python lambda
# lambda is a small anonymous function
# lambda arguments: expression
x=lambda a:a+10
print(x(5))
# It can take any number of arguments
x=lambda a,b:a+b
print(x(5,6))

def my_function(n):
    return lambda a:a*n

new_func=my_function(2)
print(new_func(7))
# Python arrays
# python does not have a built in arrays but python lists can be used instead
# However if we wish to use arrays in python we can use numpy arrays instead

# Classes in Python
# Python is an object oriented language
# i.e. everything in python is an object
# Class is like a bluprint for object creation
class myClass:
    x=4
    def newFunction(self):
        print(self.x)

p1=myClass()
print(p1.x)
p1.newFunction()

# python init function is executed whenever the class is being initiated
class myClass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def my_function(self):
        print(f'{self.name}: name age is {self.age}')
p1=myClass('Aayush',21)
print(p1.name)
# __init__ function is called automatically
p1.my_function()
# we can also delete object properties
del p1.name
print(p1.age)
del p1

# Python Inheritance
class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def print_name(self):
        print(f'First name: {self.firstname} Last name: {self.lastname}')

x=Person("Aayush","Regmi")
x.print_name()
class Student(Person):
    def __init__(self,fname,lname,age,college):
        super().__init__(fname,lname)
        self.age=age
        self.college=college

    def print_name(self):
        print(f'Name: {self.firstname} {self.lastname} Age: {self.age} College: {self.college}')

y=Student('Mesut','Ozil','21','Ncit')
y.print_name()

# Python dates
# date in python is not the datatype of it's own we must import datetime module
import datetime
x=datetime.datetime.now()
print(x.strftime("%A"))
print(datetime.datetime(2020,5,8))

# Python Math
print(min(2,5,9))
print(max(2,5,9))
print(abs(-2.9))
print(pow(2,3))
# We can also import a build in math module
import math
print(math.sqrt(4))

# Python JSON
