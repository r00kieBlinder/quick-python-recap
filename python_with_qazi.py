# comments 
# variables 

# print ('hello world I am gonna finish this course')

# name = "fahim abrar"
# age = 20

# print (name)
# print (age)

# full_name = "Fahim Abrar Shayokh"
# print (full_name)
# length, width = 200, 500
# print (length)
# print (width)
# print (int(length * width))

# your_name = input('please enter your name : ')
# print ('hi ' + your_name)

# DATA TYPES
# STRINGS
# int{1, 2, 3, ...} , float/decimal numbers{.3, .4, ...} (numbers)

# strings 'hello' , 'cookie' => 'hellocookie'
# strings '10' , '20' => '1020'

# math operators (+, -, *, **, /, //. %)


# num1 = int (input('enter a number : '))
# num2 = int (input('enter another number : '))
# print (num1 + num2)
# print (num1 * num2)
# print (num1 ** num2)
# print (num1 / num2)
# print (num1 // num2

# Tip Calculator App

food_amount = float(input("enter food amount $: "))
tip_percentage = float(input ("enter your tip percentage $: ")) / 100
tip_amount = food_amount * tip_percentage
total_payable_amount = food_amount + tip_amount
print ('\n\n')
print ('-----------------------------------------------')
print (f' 🥫 Food Amount : ${food_amount}')
print (f' 🫰 Tip Amount : ${tip_amount}')
print ('\n')
print (f' 💵 Total Payable Amount : 🫱 ${total_payable_amount} ')
print ('-----------------------------------------------')

# STRING FORMATING

# BOOLEAN
# IF THEN ELSE

# baby Weather App
# if it's raining outside, grab you umbrella 
# otherwise, grab your sunglasses

# Boolean (True, False)


# weather = str(input('what is the weather today? : '))

# if weather == 'rain':
#   print ('☔')

# elif weather == 'cloudy':
#   print ('😶‍🌫️')

# elif weather == 'thunderstorm':
#   print ('🌩️')

# else:
#   print ('😎')
  
# comparison operators (==, <, >, <=, >=)


# GRADE CALC APP

# >=90 🫱 A 
# >=80 🫱 B
# >=70 🫱 C
# >=60 🫱 D
# <60 🫱 F

# marks = float(input('What is your score? : '))

# if marks >= 90: 
#   print ('A')
  
# elif marks >= 80: 
#   print ('B')
  
# elif marks >= 70:
#   print ('C')
  
# elif marks >= 60:
#   print ('D')
  
# else: 
#   print ('F')

# EITHER A PASSING GRADE OR A FAILING GRADE and ends at 100
# read the style guide. If you search PEP8 on Google, you'll find it.
# write more "PYTHONIC"

# score = float (input('What is your score? : '))

# if score >= 60 and score <= 100:

# if 60 <= score <=100: 
#   print ('Passed')
  
# else:
#   print ('Failed')

# if score < 60 or score > 100: 
#   print ('you either failed or you super passed')


# def say_my_name():
#   print ('Fahim Abrar')
#   print ('John')
#   print ('Kara')

# say_my_name()

# one argument inside a function

# def say_my_name_2(name):
#   print (name)
  
# say_my_name_2('Buddam')

# multiple argument inside a function + default arguments

# def greeting (name, greet='bye'):
#   '''
#   greetings takes 2 arguments, greet & name and it greets the user

#   >>>greeting ('bye', 'Abrar')
#   "👋 Bye Abrar!"
  
#   '''
  
  # print (f'{greet} {name}!')

# positional arguments 
# greeting('Abrar', 'Hello')

# named arguments
# greeting (greet='Hi', name='Buddam')

def sum (a: int, b: int):
  '''Takes 2 integers and returns their sum
  >>> sum (1, 2)
  3
  '''
  return a + b
  
# print (sum (1, 2))


### Convert this into a function ###
## Tip Calculator App

# food_amount = float(input("enter food amount $: "))
# tip_percentage = float(input ("enter your tip percentage $: ")) / 100
# tip_amount = food_amount * tip_percentage
# total_payable_amount = food_amount + tip_amount
# print ('\n\n')
# print ('-----------------------------------------------')
# print (f' 🥫 Food Amount : ${food_amount}')
# print (f' 🫰 Tip Amount : ${tip_amount}')
# print ('\n')
# print (f' 💵 Total Payable Amount : 🫱 ${total_payable_amount} ')
# print ('-----------------------------------------------')


def calculateFoodTotal(food_amount, tip_percentage):
  tip_amount = food_amount * (tip_percentage / 100)
  total_payable_amount = food_amount + tip_amount
  print ('\n\n')
  print ('-----------------------------------------------')
  print (f' 🥫 Food Amount : ${food_amount}')
  print (f' 🫰 Tip Amount : ${tip_amount}')
  print ('\n')
  print (f' 💵 Total Payable Amount : 🫱 ${total_payable_amount} ')
  print ('-----------------------------------------------')
  return total_payable_amount


# print (calculateFoodTotal (100, 20))
# print (calculateFoodTotal(food_amount=100, tip_percentage=20))


  
### Modifying the weather app to with functions

  '''
   weather_to_emoji takes in 1 argument as a string (expected inputs : 'rain',     'thunderstorm', 'cloudy') it returns nothing 
   
    >>> weather_to_emoji ('rain')
    '☔'
    >>> weather_to_emoji ('thnderstorm')
    '🌩️'
    >>> weather_to_emoji ('sunny')
    '😎'
  
  '''
#TYPEHINTING
def weather_to_emoji(weather: str) -> None: # here str and none is for documentation purpose so that the reader can understand clearly
  if weather == 'rain':
    print ('☔')
    
  elif weather == 'cloudy':
    print ('😶‍🌫️')

  elif weather == 'thunderstorm':
    print ('🌩️')
    
  else:
    print ('😎')

# weather_to_emoji ('thunderstorm')



# we did exercises.bigger_guy
# import exercises.bigger_guy



# lambda - anonymous function

# implicit return

# sum2 = lambda a, b: a + b
# print (sum2(1, 2))

# greet = lambda greet, name: f"{greet} {name}"
# print (greet('Aloha!', 'Abrar.'))

# farewell = lambda bye, name: f"{bye} {name}"
# print (farewell('Bye!', 'Priyo.'))



# testing your code / unit tests 

def test_sum():
  assert sum(1,2) == 3
  assert sum(-20, 20) == 0
  assert sum(560, 780) == 1340
  print ('Sum Function : All Tests Passed (4/4) 👍')

# test_sum()


# def test_calculate_food_total():
#   assert calculateFoodTotal(100, 20) == 120
#   assert calculateFoodTotal(-100, -20) == 120
  # assert calculateFoodTotal(100.23, 20.43)


# test_calculate_food_total()


# LISTS (ARRAYS)
# Methods -- list.append() vs. functions -- print()
#

fruits = ['🍎', '🥭', '🍓', '🍍', '🍪']
# print (fruits)
# fruits.append ('🍊')
# print(fruits)
# fruits.append ('🍌')
# print(fruits)


# INDEXING

# print(fruits[0])  # apple
# print(fruits[1])  # mango
# print(fruits[5])  # banana

# how to get the last item in the array?
# print(fruits[-1]) # banana
# print(fruits[-3]) # pineapple

# left to right (0, 1, 2, 3, ......)
# right to left (-1, -2, -3, ......)


### SLICING ###

# print (fruits[0:2]) # first inclusive, 2nd exclusive 
# print (fruits[0:3])  
# print (fruits[0: len(fruits) - 1])
# print ('Hi my name is Abrar'[0: 2])
# print ('Hi my name is Fahim'[-1])
# print (fruits[0: 5])
# print (fruits[0:5:1])
# print (fruits[0:5:2]) # from : to : step by
# print (fruits[::-1]) # reverse the list {important for building projects}



# Length function -- len() # to measure the length of the array



### DICTIONARY ### 

# list and Dictionaries are mutable

# Key 🫱 Value

# person = {
#   'name' : 'Qazi', 
#   'shirt' : 'black', 
#   'laptop' : 'apple'
# }
# styling your code is necessary

# print (person['name'])
# print (person['shirt'])
# print (person['laptop'])

# def introducer(): person = {
#   'name' : 'Qazi', 
#   'shirt' : 'black', 
#   'laptop' : 'apple'
# }
#   print (f"👋 Hi my name is {person['name']}, 👕 I am wearing {person['shirt'] shirt, 💻 I am using an {person['laptop']} to code. ")

# introducer ()

def netWorth():
  return person ['assets'] - person['debt']

def introducer(): 
  person = {
  'name' : 'Abrar', 
  'shirt' : 'black',
  'laptop' : 'Apple MacBook M1',
  'assets' : 100,
  'debt' : 50,
  'favoriteFruits' : ['🍎', '🥭', '🍊'],
  'netWorth' : lambda: person ['assets'] - person['debt']
}
  person ['shirt'] = 'Orange'
  person ['assets'] = 1000

  
  print (f" 👋 Hi my name is {person['name']}, \n 👕 I am wearing a {person['shirt']} shirt, \n 💻 I am using {person['laptop']}, \n 💵 and my net worth is {person['netWorth']()}$, \n 🥝 my favorite fruit is {person['favoriteFruits']}")


# introducer()



#### TUPLES () ####

# immutable

# numbers = (1, 2)
# print (numbers)
# print (type(numbers))
# print (numbers[0])
# print (numbers[1])



######## SETS {} 👉🏻 Used for getting unique stuff ########

# list1 = ['ruby', 'python', 'JavaScript'] 
# list2 = ['ruby', 'SQL', 'JAVA', 'JavaScript']


# programming_languages = set (list1 + list2)
# print  (programming_languages)
# print ('GO' in programming_languages)   # 👉🏻 False 
# print ('SQL' in programming_languages)   # 👉🏻 True


# print (set (programming_languages))


# print ({1, 2, 2})



### Special Keywords ### 
# list, len, max, min, set, dict, etc. 




'''
### EXERCISE ###

Create a function unique, that takes in a list and returns only unique items

>>> unique (['ruby', 'ruby', 'python'])
['ruby', 'python']

'''

# noob way
# unique = ['ruby', 'ruby', 'python']
# programmingLanguages = set (unique)
# print (programmingLanguages)


# better way 
# def unique (languages) :
#   return list(set(languages))

# print (unique (['ruby', 'ruby', 'python']))


# # pro way using lambda function (overkill) # not necessary
# unique = lambda languages: list(set(languages))

# print (unique (['ruby', 'ruby', 'python'])






##### LOOPS #####

fruits = ['🍎', '🥭', '🍓', '🍍', '🍪']
# print ('fruit :', fruits[0], 0)
# print ('fruit :', fruits[1], 1)
# print ('fruit :', fruits[2], 2)
# print ('fruit :', fruits[3], 3)
# print ('fruit :', fruits[4], 4)


# for fruit in fruits:
#    return (fruit)


# for fruit in enumerate(fruits):
#   print ('fruit :', fruit[1], fruit[0])


# for index, fruit in enumerate(fruits):
#   print ('fruit :', fruit, index)



# for number in [1, 2, 3, 4, 5] : 
#   print (number)


# do this 5 times 
# for _ in range (5):
#   print ('haha')


# add 10 apples to the fruits list
# for _ in range(10): 
#   fruits.append('🍎')

# print (fruits)




# fruits.append ('🍎')
# fruits.append ('🍎')
# fruits.append ('🍎')
# fruits.append ('🍎')
# fruits.append ('🍎')
# fruits.append ('🍎')
# fruits.append ('🍎')
# fruits.append ('🍎')
# fruits.append ('🍎')
# fruits.append ('🍎')


# print (fruits)

##### TUPLE UN-PACKING #####






##### WHILE LOOPS #####
# WATCHOUT FOR: 👉🏻 INFINITE LOOP 

# abrar = 'sitting'
# while abrar != 'standing':
#   print ('Get your Fat Butt up 💯 !')

# counter = 0
# while counter < 10: 
#   print (counter)
#   counter += 1 









# numbers = [1, 2, 3, 4, 5]

# '''
# >>> double ([1, 2, 3, 4, 5])
# [2, 4, 6, 8, 10]
# '''

# def double(numbers : list) -> list: 
#   result = []
#   for number in numbers:
#     result.append (number * 2)

#   return (result)
    
# print (double ([1, 2, 3]))

# create empty list
# loop through & append to that list
# return that list


# # my practice
# numbers = [11, 12, 13, 14, 15]

# def double (numbers : list): 
#   result = []
#   for number in numbers: 
#     result.append (number * 2)

#   return (result)

# print (double([11, 12, 13, 14, 15]))




'''
Count Words if given a string,should count & return the number of words

phrase : str

>>> count_words ('Hi my name is Abrar')
5
'''

# def count_words (phrase): 
#   print (phrase)

# count_words(len('Hi my name is Abrar'.split()))


# #Or 
# def count_words (phrase) : return len(phrase.split())

# print (count_words('I am Batman'))



# # I did this extra : 
# def countWords (phrase):
#   print (len(phrase.split()))

# countWords(str(input()))


##### could not learn Debugging in Replit #####




'''
create a function that given a list of numbers, it can return their sum

>>> sum_list([1, 2, 3])
6
'''

def sum_list (numbers):
  count = 0
  for number in numbers : 
    count += number

  return count

# print (sum_list([1, 2, 3]))
# print (sum_list([1, 2, 3, 4]))

# find_max

''' 
>>> find_max([1, 5, 10, 3])
10

'''
# def find_max (numbers : list):
#   current_max = numbers[0]
#   for number in numbers: 
#     if number > current_max: 
#       current_max = number

#   return current_max

# print (find_max([1, 2, 3, 10, 17, 4, 5, 6, 29]))


# numbers = [1, 5, 10, 3]
# current_max = 1 #numbers = [0]
# is 1 > current_max ? no 
# is 5 > current_max ? yes
# current_max = 5
# is 5 > current_max ? no
# current_max = 10
# is 3 > current_max ? no
# end the loop






##### DICTIONARY PRACTICE #####

'''
>>> word_frequency ('I love Batman because I am Batman')
{'I' : 2, 'love': 1, 'because': 1, 'Batman': 2, 'am': 1}
'''

# def word_frequency (phrase):
#   result ={}
#   words = phrase.split()
#   for word in words:
#     if word not in result:
#       result[word] = 1
#     else:
#       result[word] += 1

#   return result


# # print(word_frequency ('I love Batman because I am Batman'))

# print (word_frequency(input('Please enter your phrase : ')))



# result = {
#   'I' = 2, 
#   'love' = 1,
#   'Batman' = 2,
#   'because' = 1,
#   'am' = 1,
# }


# # loop 1
# is 'I' in result? no 
# create a new key value pair
# set the key to 'I' and value to 1

# # loop 2 
# is 'love' in result? no
# set the key to 'love' and value to 1

# # loop 3
# is 'Batman' in result? no
# set the key to 'Batman' and value to 1

# # loop 4
# is 'because' in result? no
# set the key to 'bacause' and value to 1

# # loop 5 
# is 'I' in result? yes
# increment the value of 'I' key by 1

# # loop 6
# is 'am' in result? no
# set the key to 'am' and value to 1

# # loop 7
# is 'Batman' in result? yes 
# increment the value of 'Batman' key by 1








######### HIGHER ORDER FUNCTIONS ######### 
# map 
# filter 

'''
>>> double ([1, 2, 3])
[2, 4, 6]
'''



# def double_number (number):
#   return number * 2

# print(list(map(double_number, [1, 2, 3])))


# print(list(map(lambda num: num * 2, [1, 2, 3])))   # this code is similar to line (721-724)
# print(list(map(lambda num: num ** 2, [1, 2, 3])))

# print (double_number(4))

# def double (numbers : list): 
#   result = []
#   for number in numbers: 
#     result.append (number * 2)

#   return (result)




##### FILTER #####

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# print(list(filter(lambda number : number % 2 == 0, numbers)))


'''
>>> numbers = [1, 2, 3, 4, 5, 6]
# how to check for an EVEN number?
>>> 2 % 2 == 0
True 
>>> 4 % 2 == 0
True 
>>> 6 % 2 == 0
True 
# every even number divided by 2 has no remainder 
# every even number divided by 2 has no remainder (EVEN NUMBER)
>>> 5 % 2 == 0
False

'''
# % -- represents divisible with remainder 0


### END OF HIGHER ORDER FUNCTIONS ###



#### LIST COMPREHENSIONS ####
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# # filter - and give me only EVEN numbers 
# print([number for number in numbers if number % 2 == 0])

# # map - double numbers 
# print([number * 2 for number in numbers])

# # filter - and give me only ODD numbers
# print([number for number in numbers if number % 2 != 0])

# # give me all of the odd numbers CUBED 
# print([number ** 3 for number in numbers if number % 2 != 0])






### SPECIAL BUILT-IN FUNCTIONS with Python ###
# >>> sum([1, 2, 3])
# 6
# >>> len([1, 2, 3])
# 3
# >>> max([1, 2, 3])
# 3
# >>> max([1, 2, 3, 10, 5, 7])
# 10
# >>> min([1, 50, -7, 337])
# -7