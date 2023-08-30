print ('Hello World')

if 5 > 2:
    print ('Five is greater than two!')


# This is a simply comment

"""
This is a comment
written in
more than just one line
"""


x = 5
y = 'John'

print(x)
print(y)

################################

x = 4
x = "Sully"

print(x)

print(type(x))

####### Pascal Case
MyVariableName = "John"
##### Snake Case
my_variable_name = "John"


x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

################################

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#### For numbers, the + character works as a mathematical operator:

x = 5
y = 10
print(x + y)


###

x = "awesome"

def myfunction():
    print("Python is " + x)

myfunction()

###

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


### You can get the data type of any object by using the type() function:

x = 5
print(type(x))


###

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


###

##Since strings are arrays, we can loop through the characters in a string, with a for loop.

for x in "banana":
   print(x)


######

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


  # Python 3: Fibonacci series up to n
def fib(n):
     a, b = 0, 1
     while a < n:
         print(a, end=' ')
         a, b = b, a+b
     print()
fib(1000)


## The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."



###### Pthon Conditions and If statements

a = 33
b = 200
if b > a:
  print ('b is greater than a')
  

a = 33
b = 33
if b > a:
   print('b is greater than a')
elif a == b:
   print('a and b are equal')



a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")



###### Pthon Conditions and If statements


  i = 1
  while i < 8:
     print(i)
     i += 2

i = 1
while i < 6:
   print(i)
   if i == 2:
      break
   i += 1


i = 1
while i < 6:
   i += 1
   if i == 3:
      continue
   print(i)

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

i = 1
while i < 6:
   print(i)
   i += 1
else:
   print('i is no longer less than 6')

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

fruits = ["apple", "banana", "cherry"]
for x in fruits:
   print(x)

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

for x in "bananasnas":
   print(x)


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
fruits = ["apple", "banana", "cherrys"]
for x in fruits:
   print(x)
   if x == "banana":
      break 
   


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
for x in range(6):
   print(x)

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)   


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

def my_function():
  print("Hello from a function")

my_function()

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
#If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
  print("The youngest child is " + kids[0])

my_function("Emil", "Tobias", "Linus")


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
class MyClass:
  x = 5


p1 = MyClass()
print(p1.x)

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

# https://www.w3schools.com/python/python_modules.asp

#  import mysql.connector


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


def myfunc():
   x = 300
   def myinnerfunc():
      print(x)
   myinnerfunc()

myfunc()


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

import mymodule

mymodule.greeting("Jonathan")

a = mymodule.person1["age"]
print(a)

import datetime

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

print(x.strftime("%B"))



print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

x = abs(-7.25)
print(x)

x = pow(4,3)
print(x)

import math

x = math.sqrt(64)
print(x)

x = math.ceil(1.4)
y = math.floor(1.4)

print(x)
print(y)

x = math.pi
print(x)

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

import json
# some JSON:
x = '{"name":"Jhon", "age":30, "city":"NewYork"}'

# parse x:
y = json.loads(x)

#the result is a Python dictionary:
print(y["age"])

# https://www.w3schools.com/python/python_json.asp

# a Python object (dict):
x = {
   "name": "John",
   "age": "30",
   "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

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

print(json.dumps(x))

json.dumps(x, indent=4, separators=(". ", " = "))


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')


import re

txt = "The rain in Mexico"
x = re.search("^The.*Mexico$", txt)


if x:
  print("YES! We have a match!")
else:
  print("No match")


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

import camelcase
c = camelcase.CamelCase()
txt = "hello worl"
print(c.hump(txt))

# List Packages
# Use the list command to list all the packages installed on your system:

# >pip list




 
#
#try:
#   print(x)
#except NameError:
#   print("Variable x is not defined")
#except:
#   print("Something else went wrong")

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

               #   username = input("Enter username:")
               #   print("Username is:" + username)



price = 49
# txt = "The price is {} dollars"
txt = "The price is {:.2f} dollars"

print(txt.format(price))



print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f}{2:.2f}{2:.2f} dollars"
print(myorder.format(quantity, itemno, price))



myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

# To open a file for reading it is enough to specify the name of the file:
# f = open("demofile.txt", "rt")

f = open("demofile.txt", "rt")
print(f.read())
#print(f.read(5))


#for x in f:
#  print(x)

#  Open a file on a different location:
#  f = open("D:\\myfiles\welcome.txt", "r")
#  print(f.read())

#It is a good practice to always close the file when you are done with it.
#f = open("demofile.txt", "r")
#print(f.readline())
#f.close()

# https://www.w3schools.com/python/python_file_write.asp

#     f = open("demofile.txt", "a")
#     f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

# Installation of Matplotlib   -->  pip install matplotlib

import matplotlib

print(matplotlib.__version__)

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

   #   import matplotlib.pyplot as plt
   #   import numpy as np

   #   xpoints = np.array([0,3,4,5,6])
   #   ypoints =  np.array([0,50,55,60,250])
   #   ypoints1 = np.array([10,65,70,75,275])

      # plt.plot(xpoints, ypoints, marker = 'o')
   #   plt.plot(xpoints, ypoints, marker = '*')
   #   plt.plot(xpoints, ypoints1,marker= 'o')

   #   font1 = {'family':'serif','color':'blue','size':20}
   #   font2 = {'family':'serif','color':'darkred','size':15}

   #   plt.title(" Title of Plot ", fontdict = font1)
   #   plt.xlabel(" X axis ", fontdict = font2)
   #   plt.ylabel(" Y axis ", fontdict = font2)



      # plt.plot(ypoints, 'o-.r')

   #   plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
   #   plt.show()


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')


     # import matplotlib.pyplot as plt
     # import numpy as np

     # x = np.random.randint(100, size=(100))
     # y = np.random.randint(100, size=(100))
     # colors = np.random.randint(100, size=(100))
     # sizes = 10 * np.random.randint(100, size=(100))


     # plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

     # plt.colorbar()

     # plt.show()


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

   #      import matplotlib.pyplot as plt
   #      import numpy as np
   #
   #      x = np.array(["A", "B", "C", "D"])
   #      y = np.array([3, 8, 1, 10])
   #
   #      # plt.bar(x,y)
   #      # plt.barh(x,y)
   #
   #      plt.bar(x,y,color="#4CAF50",width=0.1)
   #      plt.show()

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

   #   import matplotlib.pyplot as plt
   #   import numpy as np
   #
   #   x = np.random.normal(170,10,250)
   #
   #   plt.hist(x)
   #   plt.show()
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

   #      import matplotlib.pyplot as plt
   #      import numpy as np
   #
   #      y = np.array([35,25,25,15])
   #      mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
   #      mycolors = ["black", "hotpink", "b", "#4caf50"]
   #      myexplode = [0.2,0,0,0]
   #
   #      plt.pie(y, labels = mylabels, colors = mycolors, explode = myexplode, shadow = True)
   #      plt.legend(title = "Four Fruits:")
   #      plt.show()

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

# Machine Learning

# Machine Learning is making the computer learn from studying data and statistics.
# Machine Learning is a step into the direction of artificial intelligence (AI)
# Machine Learning is a program that analyses data and learns to predict the outcome.
# Numerical : Discrete Data, Continuous Data
# Categorical:  colors, yes/no
# Categorical:  school grades, where A is better than B.

import numpy
speed = [99,86,87,111,86,103,87,94,78,77,85,86]

# (99+86+87+88+111+86+103+87+94+78+77+85+86) / 13 = 89.77
x = numpy.mean(speed)
print(x)

# 77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103     (86 + 87) / 2 = 86.5
y = numpy.median(speed)
print(y)

# from scipy import stats

# 99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86 = 86

# z = stats.mode(speed)
# print(z)


xx = numpy.std(speed)
print (xx)

speed2 = [32,111,138,28,59,77,97]
yy = numpy.std(speed2)
print(yy)



speed1 = [32,111,138,28,59,77,97]
x1 = numpy.var(speed)
print(x1)

x2 = numpy.std(speed1)
print(x2)


ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
x = numpy.percentile(ages, 75)
print(x)


x = numpy.percentile(ages, 90)
print(x)


x3 = numpy.random.uniform(0.0, 5.0, 250)
print(x3)

import numpy
import matplotlib.pyplot as plt

plt.hist(x3,5)
plt.show()


import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show()



# https://www.w3schools.com/python/python_ml_multiple_regression.asp

# https://www.w3schools.com/python/pandas/pandas_analyzing.asp


# https://www.w3schools.com/python/pandas/pandas_csv.asp


import pandas as pd
df = pd.read_csv('data.csv')
print(df.to_string())
# to_string() to print the entire DataFrame




df = pd.read_json('data.json')

print(df.to_string()) 

# JSON = Python Dictionary

# JSON objects have the same format as Python dictionaries.



print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')


df = pd.read_csv('data.csv')
print(df.head(10))
print(df.tail())
print(df.info())


# https://www.w3schools.com/python/python_ml_multiple_regression.asp  
# https://www.w3schools.com/python/pandas/pandas_cleaning_empty_cells.asp 


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

#import pandas as pd
#import matplotlib.pyplot as plt

#df = pd.read_csv('data.csv')
#df.plot()
#plt.show() 

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')


            #df = pd.read_csv('data.csv')
            #df.plot(kind = 'scatter', x = 'Duration', y = 'Calories' )
            #plt.show()                                        

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

# https://www.w3schools.com/python/pandas/pandas_compiler.asp

# https://www.w3schools.com/spaces/index.php

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

print('=-=-=-=-=-=-=-=-=-=-Python and Mysql=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')




##  Install conecction of MySQL Connector
##  python -m pip install mysql-connector-python

import mysql.connector 

mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="",
   database="mydatabase"
)

print(mydb)

## To create a database in MySQL, use the "CREATE DATABASE" statement:
#  mycursor = mydb.cursor()
#  mycursor.execute("CREATE DATABASE mydatabase")

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
   print(x)

   
######executed sucessfully###############
## mycursor = mydb.cursor()
## mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
####################

######executed sucessfully###############
## mycursor = mydb.cursor()
## mycursor.execute("CREATE TABLE customers1 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
####################

######executed sucessfully###############
## mycursor = mydb.cursor()
## mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
####################


######executed sucessfully###############
## mycursor = mydb.cursor()
## sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
## val = ("John", "Highway 21")
## mycursor.execute(sql, val)
## mydb.commit()
## print(mycursor.rowcount, "record inserted.")
####################

######executed sucessfully###############
## mycursor = mydb.cursor()

## sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
## val = [
##  ('Peter', 'Lowstreet 4'),
##  ('Amy', 'Apple st 652'),
##  ('Hannah', 'Mountain 21'),
##  ('Michael', 'Valley 345'),
##  ('Sandy', 'Ocean blvd 2'),
##  ('Betty', 'Green Grass 1'),
##  ('Richard', 'Sky st 331'),
##  ('Susan', 'One way 98'),
##  ('Vicky', 'Yellow Garden 2'),
##  ('Ben', 'Park Lane 38'),
##  ('William', 'Central st 954'),
##  ('Chuck', 'Main Road 989'),
##  ('Viola', 'Sideway 1633')
##]

## mycursor.executemany(sql, val)

## mydb.commit()

## print(mycursor.rowcount, "was inserted.")
####################



######executed sucessfully###############
## mycursor = mydb.cursor()

## sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
## val = ("Michelle", "Blue Village")
## mycursor.execute(sql, val)

## mydb.commit()

## print("1 record inserted, ID:", mycursor.lastrowid)
####################



######executed sucessfully###############
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM customers WHERE id > 5")
# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)
####################


mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123567' WHERE id = '5'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")




