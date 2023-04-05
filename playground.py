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