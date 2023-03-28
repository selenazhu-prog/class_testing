# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import datetime

#Numeric
x = 10
y = 5.1
z = x * y

print(z)

print(type(x))
print(type(y))
print(type(z))

x = 100
x += 15
print(x)

x -= 15
print(x)

x *= 15
print(x)

x /= 15
print(x)

x = 100
x = x + 15
print(x)

x = 100
print(x + 15)
print(x)

#Booleans
x = 10
y = 11
print(x == x)
print(x == y)

x = True
y = False
print(x != y)

x = 10
y = 11
print(x >= y)
print(x <= y)

#Strings
x = 'Hello world!'
y = "Hello world!"
print(x == y)

my_string = "I don't like Mondays!"
my_string = 'The professor said "the homework is due Sunday" in class.'

x = 'abc'
y = '123'
z = x + y
print(z)

x += y
print(x)


my_string = ' hello world!'
big_string = my_string.upper()
print(big_string)

cap_string = my_string.capitalize()
print(cap_string)

space_string = my_string.strip()
print(space_string)

fixed_string = my_string.strip().capitalize()
print(fixed_string)

name = 'Bob'
my_string = f'Hello {name}, welcome to class.'
print(my_string)

my_string = 'Hello {}, welcome to class.'.format(name)
print(my_string)

my_string = 'Hello %s, welcome to class.' % name
print(my_string)

#Lists
x = [1, 2, 3]
print(x)
print(len(x))

x = ['a', 'b', 'c', 'd', 'e']
print(x[1:3])
print(x[0])
print(x[::2])

print(x[:3])
print(x[3:])
print(x[:3] + x[3:])

x = ['a', 1, 4.2, True, 'Hello world', [1, 2, 3]]
print(x[0])
print(x[0] == 'a')

print(x[-1])
print(x[-1][0])

#Other list-like objects
my_list = ['a', 'a', 'b', 'c']
my_tuple = ('a', 'a', 'b', 'c')

my_list[0] = 'A'
print(my_list)

my_tuple[0] = 'A'

my_list = ['a', 'a', 'b', 'c']
my_set = {'a', 'a', 'b', 'c'}

print(my_list)
print(my_set)

my_string = 'Hello world!'
print(my_string[0])
print(my_string[3:7])
print(my_string[::-1])

#Dictionaries
my_dict = {'a':100, 'b':200, 'c':300}
print(my_dict['a'])

#Dates
my_date = datetime.datetime(2020, 3, 1)
print(my_date)

print(my_date.year)
print(my_date.month)
print(my_date.day)

time_since_covid = datetime.datetime.now() - my_date
print(time_since_covid)