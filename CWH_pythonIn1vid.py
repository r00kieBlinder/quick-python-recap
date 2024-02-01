# import cv2
# import math

'''
This is a multiline comment
# This is a comment
# print("Hello World\n")
print(5+8)
# if(age<18): 
#     print("Hello")
'''

# print(math.gcd(3, 6))

'''
a = 34
b = "Harry"
c = 45.32
d = 2

### Arithmetic operators ###
print(a+d)   # Addition
print(a-d)   # Subtraction
print(a*d)   # Multiplication
print(a**d)   # Exponential 
print(a/d)   # Division
print(a//d)   # Floor Division
print(a%d)   # Modulo 

typeA = type(a)
print(typeA)
typeB = type(b)
print(typeB)
e = 3.14
print(type(e))

'''

'''
### Typecasting ###

x = "29"
print(type(x))
x = int(x) 
# float, str
print(type(x))
print(x+2)
'''


# name = '''rOOkie
# is an amazing programmer'''
# print(name)


# name = "rOOkie"
# # print(name[2:5]) 
# # print(name.strip())
# # print(len(name)) 
# var1 = name.lower()
# var2 = name.upper()
# var3 = name.replace("Okie" , "Ot")
# print(var1)
# print(var2)
# print(var3)



'''
### STRING ###
str1 = "This is a "
name1 = "rOOkie"
name2 = "Buddam"
str2 = "This is not a "
print(str2 + name1)
# temp = "This is a {1} and he is a good boy named {0}".format(name1, name2)
temp = f"this is a {name1}  and he is a good boy named {name2}" # fstring format is more useful
print(temp)
'''


'''
Python Collections:
1. List
2. Tuple
3. Set
4. Dictionary
'''

'''
### LIST ###
lst = [61, 2, 3, 4, 5, 6, 41]
print(lst)
# var = lst[2]
var = lst[1:4]
lst[2] = 45
var2 = lst
print(var2)
print(len(lst))
lst.append(100) # appends i.e adds the element in the end of the set of objects
print(lst)
lst.insert(0, 100) # index 1 -> 100
print(lst)
lst.remove(61) # removes the element from the set of objects
print(lst)
lst.pop() # 1 element at the end disapears 
print(lst)
del lst[3]
print(lst)
lst.clear()
print(lst)

'''

'''
### TUPLE ###
a = ("Abrar", "Zia", "Tanvir")
var = type(a)
print(var)
# a[0] = "Zarif" # a tuple is unchangeable 
# tuple is generally used when you don't want to change your elements
print(a)
a = list(a) # we can do after typecasting 
a[0] = "Zarif"
print(a)
'''


'''
### SET ###
s1 = {23, 2, 2, 2, 2, 2, 2, 5, 6, 34, 6, 3, 5, 6, 12}
# s1.add(444)
# s1.update([13, 14, 15, 16, 17])
print(len(s1))
# print.remove(166) # will through error if element is not in set
#print.discard(166) # will remove if there any or else it will run smoothly
# Like list you can do : .pop, .clear, del
# and... intersection, union
print(s1)
'''


'''
### Dictionary ###

harryDict = {
    "Name" : "Harry", 
    "Class" : "11th",
    "Marks" : 34.35,
    "Hours in School" : 6
}
print(harryDict)
print(harryDict["Marks"])
harryDict["Marks"] = 50
print(harryDict)
harryDict.pop("Hours in School")
print(harryDict)
# you can also use : del, .clear, .pop, .update

'''

'''
### Conditional Statements ###

age = int(input("Enter your age\n"))
if(age>18):
    print("You can drive a car")
elif(age==18):
    print("You are an awesome teen")
else:
    print("You cannot drive a car")

'''


### LOOPS ###

# Scenario : you have to print numbers between 1 to 1000
# for i in range(1, 1001):
#     print(i)

# li = [1, 245, "this"]
# for item in li: 
#     print(item)

# Quiz: Use for loop to iterate dictionary, set, and tuples

# dictionary
# capital_city ={
#     "Germany" : "Berlin",
#     "Bangladesh" : "Dhaka",
#     "Japan" : "Tokyo" 
# }
# for i in capital_city:
#     print(i)

#tuple
#a = ("Abrar", "Zia", "Tanvir")
#for i in a:
#    print(i)


# set
# a = {1, 2, 3, 4, 5}
# for item in a: 
#     print(item)




