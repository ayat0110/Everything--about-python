#Python Dictionaries
#Dictionaries are used to store data values in key:value pairs.
#Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
thisdict={"brand":"ford","model":"mustang","year":1964}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
print(type(thisdict))
#The values in dictionary items can be of any data type
thisdict={
    "brand":"ford",
    "electric":False,
    "year":1964,
    "color":["red","white","blue"]
}

#Creating Variables
x=5  # x is of type int
y="jhon" # x is now of type str
print(x)
print(y)
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(type(x))
x = "John"
# is the same as
x = 'John'
#python is case sensitive
a = 4
A = "Sally"
#A will not overwrite a 
print(isinstance(x,int))
#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#The global Keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def __gt__(self,other):
        return True if self.age > other.age else False
dobby=Dog("dob",10)
otherdobby=Dog("dobbby",20)
print(dobby.__gt__(otherdobby))


percentage = float(input("Enter the percentage of marks obtained: "))

if percentage > 90:
    grade = "A"
elif percentage > 75:
    grade = "B"
elif percentage > 65:
    grade = "C"
else:
    grade = "Fail"

print("The grade assigned is:", grade)

for x in range(3):
 print("hi")
 
languages = ['Swift', 'Python', 'Go', 'JavaScript']

# access items of a list using for loop
for language in languages:
    print(language)
    
# use of range() to define a range of values
values = range(4)

# iterate from i = 0 to i = 3
for i in values:
    print(i)