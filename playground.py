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