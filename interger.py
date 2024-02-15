
# number=float(input("Enter a number " ))
# answer= float(round(number,5))
# # print(number)
# print(answer)


# # enter = int(input("Enter a number "))
# # print(type(enter))

# # enter = (input("Enter a string "))
# # print(enter[0:3],"\n",enter[3:6],"\n",enter[6:9])
# # # print(enter[2:5])
# # # print(enter[5:8])

# # age = int(input("Enter your age  "))
# # if age >= 18:
# #     print("You are eligible for voting")
# # else:
# #     print("You are not yet of voting age yet")
    

# # country = input("Enter your country name ")

# # if country == "USA":
# #     print("You are citizen of USA")
# # elif country == "canada":
# #     print("You are a Citizen of Canada")
# # elif country == "UK":
# #     print("You are a UK citizen")
# # else:
# #     print("You cannot travel")
    
    
# # number = int(input("Enter a number "))
# # if number %2 == 0:
# #    print(" this is an even number")
# # else:
# #    print("This is an odd number") 
   

# # number = int(input("Enter a number "))
# # if number == 0:
# #     print(" this is a zero")
# # elif number < 0:
# #     print(" this is a negative number")
# # elif number > 0:
# #     print("this is a positive number")

# # age = int(input("Enter a age "))  
# # if age <= 5:
# #     print("This is an infant")  
# # elif age <= 10:
# #     print("this is a child")
# # elif age <= 19:
# #     print("this is a Teenager")  
# # elif age <=21:
# #     print("this is a young adult")
# # elif age <= 60:
# #     print("this is a Adult")
# # elif age >= 61:
# #     print("this is a Senior Citizen")
# # score = int(input("Enter score:  "))
# # answer = "pass" if score > 43 else  "fail"
# # print(answer)


# # for i in range(13):
# #     print("3 multiplication table", i*3)    
    
# # for i in range(10):
# #     print (i) 
# # print("Multiplication Table of 2")  
# # for i in range(12):    
# #     print(f"2 x {i} = ", i*2 )

# # # i = 0
# # # while i < 11:
# # #     print(i)
# # #     i = i + 1
# # # i = 1
# # # while i <  10:
# # #     print(i, " x ", 5, " = ", i * 5)
# # #     i = i + 1

# # i = 22
# # # Addition
# # print("Addition ", i + 3)

# # # subtraction
# # print("Subtration ", i - 3)

# # # Division
# # print("Division ",round( i / 3, 2) )

# # # Multiplication
# # print("Multiplication ", i * 3)


# # # Floor Division
# # print("Floor Division ", i // 3)

# # # Modulos - Remainder
# # print("Modulos ", i % 3)

# # print(round(7.3333, 2))

# x=3
# for i in range(1,30):
#     if x >=3  and x <= 30:
#         print(x)
#         x=x**2
        
# Saurabh Choudhary10:31 AM
# 1. Arithmetic Operators:

# a. Create a program that takes
# two numbers as input and calculates their sum,
# difference, product, and quotient.

# # b. Write a program that converts 
# # temperature from Celsius to Fahrenheit using the formula: 
# # Fahrenheit = (Celsius * 9/5) + 32.

# # x = int(input("Enter First Number: ")) 
# # y = int(input("Enter Second number: ")) 
# # print("The Sum is: ", x + y)
# # print("The difference is: ", x-y)
# # print("The product is : ", x*y)
# # print("The quotient is : ", x%y)

# celsius = int(input("Enter temperature in Celcius : "))
# print("The Temperature in Fahrenheit is: ",  (celsius *9/5) +32)


# # 2. Comparison Operators:

# # a. Create a program that compares two numbers and prints whether they are equal, greater, or lesser.

# # b. Write a program to check if a given year is a leap year or not using comparison operators.

# x = int(input("Enter First Number : " ))
# y = int(input("Enter Second number : "))
# if x == y:
#     print("x is equal to y")
# elif x < y:
#     print("x is less than y")
# else:
#     print("x is greater than y")

# b. Write a program to check if a given year is a leap year or not using comparison operators.

# year = int(input("Enter a year : "))
# leap_year = year // 4
# if (type(leap_year) == int):
#     print ("This is a leap year")
# else:
#     print("This is not a leap year")

# Write a program to check if a number is between 1 and 10 (inclusive) using logical operators.
# number = int(input("Enter a number : "))
# if (number >= 1 and number <= 10):
#     print("number is between 1 and 10")
# else:
#     print("number is not a subset of 10")
    
# Implement a program that prints the multiplication table of a given number using a while loop.
# x = 1
# while (x < 12):
#     print(x, "x ",  3 , " = ",  x*3)
#     x = x+1
    
# count = 0
# while (count < 3): 
#     count = count + 1
#     print("Hello Geek") 

# Implement a program that starts from a given number and counts down to 1 using a while loop.

# count = 12
# while (count >= 2):
#     count = count - 1
#     print(count)

# for count in range(1, 12, +1):
#     print(count)

   

# a = 0
# b = 1

# n = int(input('Enter the number : '))
# counter = 0
# print('a = ',a,'b = ', b)

# while counter < n:
#     b,a = a + b,b    
#     print('a = ',a,'b = ', b)
#     counter = counter + 1

# Required Argument
# def mysum(num1,num2,num3):
#     print(" The sum of the numbers are = ",  num1+num2+num3)
# mysum(3,4,5)


# keyword Argument
# def mysum(num1,num2):
#     print(num1, "is greater than", num2)

# mysum(num2=3, num1=5)

# Default Argument

# def mysum(num1=5,num2=3):
#     print(num1, "is greater than", num2)

# mysum(11, 6)


# def mysum(*num):
#     print(sum(num), "is the sum of all numbers" )
# mysum(11, 6, 6, 7, 8, 9)

# def myfunction(**data):
#     print(data["school"])
#     print(data["city"])
#     print(data["country"])
#     print(data["major"])

# myfunction(school="UofT", city="Toronto", country="Canada", major="maths" )

# method = lambda x,y,w,z,a:  print("multiply = ", x*y*w*z*a)
# method(4,12,13,2,1)
# import math as mt
# method = lambda x:  print("multiply = ", mt.cos (x))
# method(12)

# #global and local variables

# z = 20 # global
# def adder(x,y):
#     z = 20  # local variable
#     print(x+y+z)
# adder(12,11)

# def adder(x,y):
    
#     global num1  ## making local variable into a global variable
#     num1 = x
#     num2 = y
#     print(num1,num2)

# adder(12,11)

# thislist = ["apple", "banana", "cherry", "pear", "berry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1  
  
  
# thistuple = ("bean", "banana", "apple", "aaxle", "cherry", "box")
# print(thistuple)
# thislist = ["bean", "banana", "apple", "aaxle", "cherry", "box"]
# print(thislist)

# # Given list
# thislist = ["apple", "pear", "banana"]

# # Using enumerate() to get index and item pairs
# numbered_list = list(enumerate(thislist, 1))

# # Printing the numbered list
# for x, i in numbered_list:
#     print(f"{x}. {i}")

#titctatoe 
# grid = ["-","-","-","-","-","-","-","-","-" ]
# while True:   
#     print(grid[0] , grid[1] , grid[2])
#     print(grid[3] , grid[4] , grid[5])
#     print(grid[6] , grid[7] , grid[8])
#     symbol = (input("Enter X or O " ))
#     position = int( input("Enter a number between 0 to 8  "))
#     #print (position)
#     grid[position] = symbol
#     grid[3]= "X"

# Make a program for login in which a dictionary is given with correct 
# credentials, ask user to enter there username and password and match
# .with the given dictionary to log them in. 

# data = {
#     'username' : 'hipp',
#     'password' : 'Brampton'
# }

# user = input('Enter your username : ')
# if user == data['username']:
#     password = input('Enter your password: ')
#     if password == data['password']:
#         print("You are now logged in")
#     else:
#         print("Wrong password")
# else:
#     print("Wrong Username")
# # and    
# # if password == data['password']:
#     print('You are now logged in')
# else:
#     print('Wrong Username or Password')

    
# data = {
#     'student1' : {'name' : 'saurabh'},
#     'student2' : {'name' : 'hipo'},
#     'student3' : {'name' : 'tia', 'password': 'brampton'},
# }
# student_number = input('Enter Student number')
# student_name = input('Enter name : ')
# new_userp = input('Enter password : ')

# data[student_number]={'name':student_name, 'password':new_userp}
# print(data)

# past = data['student3']['password']
# print(past)


# def tripple_number(n):
#     return n*3
# data = ["man",2,3,4,5,6,7,"boy","girl",0]

# results = map(tripple_number,data)
# print(list(results))


###Stack
# london = []

# def push(item):
#     london.append(item)
#     print(london)

# def pop_item():
#     london.pop(1)
#     print(london)

# def is_empty():
#     if len(london) < 1:
#         print('Empty')
#     else:
#         print('Not empty', 'Length = ',len(london))


# push('Saurabh')
# push('hippo')
# push('tia')
# push('tia')
# push('tia')
# push('tia')
# push('tia')
# push('tia')
# push('tia')
# pop_item()
# is_empty()

# library = []
# def  add_book(n):
#     library.append(n)
#     print(library)

# add_book("story")
# add_book("poetry")
# add_book("children")


# def remove_book(n):
#     library.pop(n)
# #     print(library)

# # remove_book(1)

# # def howmany():
# #     if len(library) < 1:
# #         print("It is Empty")
# #     else:
# #         print ("Library has",  len(library),  "books")
# # howmany()

# ## Stack

# queue= ["story","children"]

# def add_queue(n):
#     queue.append(n)
#     print(queue)
# add_queue("drama")
# add_queue("fiction")
# add_queue("sci-fi")

# def queue_remove():
#     queue.pop(0)
#     print(queue)
# queue_remove()
# # queue_remove()

# def isempty():
#     if len(queue) < 1:
#         print("The queue is empty")
#     else:
#         print("The queue has ", len(queue), "books")
# # isempty()

# def isfull():
#     if len(queue) >= 3:
#         print("The queue is full")
#     else:
# #         print("The queue has", len(queue), "books")
# # isfull()
# stack = ["apple", "bread", "onion", "orange"]
# print(stack)
# queue = ['children', 'drama', 'fiction', 'sci-fi']
# print(queue)
# queue2 = queue.append("sci-fi")
# print("my appended queue is" , queue)
# queue3 = queue.pop(0)
# print("my pop queue is ", queue)
# queue4 = queue.remove("drama")
# print("My removed queue is" , queue)
# queue5 =queue.count("sci-fi")
# print("This occurs this number of times", queue5)
# queue6 = queue.extend(stack)
# print("The new queue list is", queue)
# queue7 = queue.insert(3,"lime")
# print("the Lime queue is now ", queue)
# queue8 = queue.reverse()
# print("The reverse is now ", queue)
# queue9 = queue.sort()
# print("The sorted list is now ", queue)



# try:
#     output = 12 // 4
#     if type(output) is str:
#         raise  SyntaxError("Cannot be a string")
#     elif  type(output) is float:
#         raise  SyntaxError("Cannot be a float")

# except SyntaxError as msg:
#     print("This is not right, error occured here", msg) 
#     print("Error")
    

# else:
#     print("The Answer is: ", output)
# finally:
#     print("The Code was executed with the  expected results")


# Basic Exception Handling:
# Write a Python program that takes two numbers as input from the user and performs division.
#  Use a try and except block to handle the ZeroDivisionError.
# If a user tries to divide by zero, print a meaningful error message.
# first_number = int(input("Enter First Number: "))
# second_number = int(input("Enter Second Number: "))
# #output = first_number // second_number

# try: 
#     output = first_number / second_number
#     # if type(output) is str:
#     #     raise  SyntaxError("Cannot be a string")
#     if second_number == 0:
#         raise ZeroDivisionError("Number cannot be divided by Zero")
#     if 

# except ZeroDivisionError as msg:
#     print("This is not right, ", msg)
# else: 
#     print("The answer is: ", output)
# finally:
#     print("The Code was executed as expected")





# Input Validation:
# Write a program that prompts the user to enter their age. 
# Use a try and except block to handle the ValueError that may occur if the user enters a non-integer value. 
# If a non-integer value is entered,
# print an error message and ask the user to enter their age again.

# # your_age = int(input("Enter your age: "))
# try:
#     # your_age = int(input("Enter your age: "))
#     your_age = 5
#     if type(your_age) is str:
#         raise ValueError ("The Age must not be a string ")
#     elif type(your_age) is float:
#         raise ValueError ("The Age must not be a float")

# except ValueError as msg:
#     print("This is not right, ", msg)
#     print(your_age)
#     your_age = int(input("Enter your age: "))

# else: 
#     print(" Your age is, " , your_age)
# finally:
#     print("This code was excuted correctely")



# # Multiple Exceptions:
# # Create a Python program that attempts to convert a user-input string to an integer. 
# # Use a try and except block to handle both ValueError and TypeError. Print different error messages for each type of exception.
# user_input = input("Enter your age: ")
# try:
#     user_input = int(user_input)
#     # if type(user_input) is str:
#     #     raise TypeError("This is a string")
#     # if type(user_input) is str:
#     #     raise NameError("This is a string")
#     # elif type(user_input) is float:
#     #     raise ValueError("This is a float")
# except ValueError as msg:
#     print("Not Allowed, ", msg)
# except NameError as msg:
#     print("Wrong output Not Allowed", msg)

# else:
#     print("The code is correct")
## PCAP = Certified Associate in Python Programing
## Object Oriented P

# class school:
#     def __init__(self,subject, topic):
#         self.study = subject
#         self.top = topic

# john = school("math", "Calculus")
# print("John: " , john.study)
# print("John: " , john.top)

# jane = school("biology", "blood vessels")
# print("\r")
# print("Jane: " , jane.study)
# print("Jane: " , jane.top) 

# doe = school("Chemistry", "Molecules")
# print("Doe: " , doe.study)
# print("Doe: " , doe.top)




# junior= school()
# print(junior.students)
# print(junior.location)
# print(junior.dress_code)

# government = school()
# print(government.administrator)
# print(government.students)


 
# class school:
#     def __init__(self,subject, topic):
#         self.study = subject
#         self.top = topic

# class calculator:
#     def __init__(self, num1, num2):
#         self.n1 = num1
#         self.n2 = num2
#     def adder (self):
#         print (f"Addition of {self.n1} and {self.n2} is equal to: ", self.n1 + self.n2)
#     def subtractor(self):
#         print (f"Subraction of {self.n1} and {self.n2} is equal to: ", self.n1 - self.n2)

# obj1 = calculator(14,13)
# obj1.adder() 
# obj1.subtractor()
# print(obj1.n1)

# obj2 = calculator(23,34)
# obj2.adder()



# class tictactoe:
#     def __init__(self):
#         self.grid = ["-","-","-","-","-","-","-","-","-"] 
#         print(self.grid[0],self.grid[1],self.grid[2])
#         print(self.grid[3],self.grid[4],self.grid[5])
#         print(self.grid[6],self.grid[7],self.grid[8])
#         self.userinputX()
        
#     def userinputX(self):
#         # symbol = (input("Enter X or O " ))

#         self.x = int(input("Enter a number between 0-8: "))
#         print(self.x)
#         self.grid[self.x] = "X"
#         self.displaygrid()
#         self.userinputO()
    
#     def userinputO(self):
#         self.O = int(input("Enter a number between 0-8: "))
#         print(self.O)
#         self.grid[self.O] = "O"
#         self.displaygrid()
#         self.userinputX()
    

#     def displaygrid(self):
#         print(self.grid[0],self.grid[1],self.grid[2])
#         print(self.grid[3],self.grid[4],self.grid[5])
#         print(self.grid[6],self.grid[7],self.grid[8])

# obj1 = tictactoe()


# class mobile():
#     def __init__(self):
#         self.keyboard = 'abc'
#         self.camera = '1mp'
#         self.android = '1.0'
#         self.size = '5inc'

# class smart_phone(mobile):
#     def __init__(self):
#         super().__init__()
#         self.camera ='5mp'
#         self.android = '5.0'
#         self.keyboard = 'qwerty'

# galaxy  = smart_phone()
# print(galaxy.android)
# print(galaxy.size)


# class car():
#     def __init__(self):
#         self.door = '4'
#         self.trunk = '15'
#         self.engine = '6.0'

# class honda(car):
#     def __init__(self):
#         super().__init__()
#         print("This is a child class init")
#         self.color = "red"
#         self.engine = "7.5"


# f = open("hippoly.txt","r")
# print(f.read())
# d = open("/Users/hippolyteasah/Library/CloudStorage/OneDrive-Personal/Python/Python Training/module1.py", "r")
# print(d.read(10))
# f.close()

# f = open("hippoly.txt","r")
# # f.write("\nbakery, this is a test file")
# for x in f:
#     print(x)

# from crypt import methods
# from importlib.metadata import files
# from inspect import Attribute
# from turtle import position


# d = open("hip.csv","a")
# data = input("Enter your text here: ")
# d.write(f"\nbakery, \nbanana, \napple, \noranges \n{data}")
# # for x in d:
# #     print(x)
# d.close()

# f = open("module1.py","r")
# # f.write("\nbakery, \nbread, \nbutter, \npears, \nkiwi")
# for x in f:
#     print(x)

# d = ["apple", "banana", "kiwi", "orange", "pears"]
# for x in d:
#     print(x)

# file object Attribute ( r, a, w, x ) t, b
# file positions()?
# getcwd(): - Returns the current working directory.
# listdir(): - Lists the contents of a directory.
# mkdir(): - Creates a new directory.
# rmdir(): - Removes an empty directory.
# rename(): - Renames a file or directory.
# remove(): - Deletes a file.
# path.exists(): - Checks if a file or directory exists.
# path.isfile(): - Checks if a path is a file.
# path.isdir(): - Checks if a path is a directory.
# # path.getsize(): - Gets the size of a file.
# # path.getmtime(): - Gets the last modified time of a file.
# # path.join(): - Joins two path components.
# # path.split(): - Splits a path into a tuple containing the parent directory and the file name.
# # file methods?
# # Renaming of files?


# import datetime
# # print(os.getcwd())
# print(os.listdir())
# fsize = os.path.getsize('interger.py')
# print("File size in Bytes: " + str(round(fsize, 3))+ " bytes") 
# print("File size in Kilobytes: " + str(round(fsize/1024, 3))+ " KB")
# print("File size in Megabytes: " + str(round(fsize/1024**2, 3))+ " MB")
# print("File size in Gigabytes: " + str(round(fsize/1024**3, 5))+ " GB")
# fmtime= os.path.getmtime('interger.py')
# fdatetime = datetime.datetime.fromtimestamp(fmtime)
# print(fdatetime)
# import os 
# if os.path.exists("hippolyt.txt"):
#     print("File exist")
# else:
#     print("File doesnt exists")


import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
# print(json.dumps(x))
print(x["name"],x["children"],x["age"])

import json
f = open('C:\\Users\\HP\\Downloads\\html css practice\\Thinkcloudly python\\users.json','r')
# print(f.read())
data = json.loads(f.read())
print(type(data))

print(data[0]['name'])
f.close()








