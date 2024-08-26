# List comprehension is considerably faster than processing a list using the for loop.

# syntax
    # [i for i in iterable if expression]   


# For instance if you want to change a string to a list of characters. You can use a couple of methods. Let's see some of them
   # ONE WAY
language = 'Python'
lst = list(language)   # changing the string to list
print(type(lst))       # list
print(lst)             # ['P', 'y', 't', 'h', 'o', 'n']
 
   # SECOND WAY
lst = [i for i in language]
print(type(lst))     #list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']


#### Generating Numbers 
numbers = [ i for i in range(11)]   # to generate number from 0 to 10
print(numbers)                      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#### It is possible to do mathematical operations during iteration
squares = [ i * i for i in range(11)]
print(squares)      # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#### It is also Possible to make a list of tuple
numbers = [(i, i * i) for i in range(11)]
print(numbers)      # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]
print('\n')


### List Comprehension can be combined with if expression

# Generating odd Numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]    # to generate odd numbers in range 0 to 21
print(odd_numbers)        # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Generating even numbers
even_numbers = [ i for i in range(11) if i % 2 == 0]
print(even_numbers)       # [0, 2, 4, 6, 8, 10]


# Filter Numbers : let's filter out positive even number from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_num = [ i for i in range(21) if i % 2 == 0 and i > 0]
print(positive_even_num)       # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# Flatting a three dimentional array
list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('\n')



#### LAMBDA FUNCTION
# Creating a lamda Function
    # we use a lambda keyword followed by a parameter(s),follower by an expression

# syntax
    # x = lambda param1, param2, param3: param1 + param2 + param2
    # print(x(arg1, arg2, arg3))

# Name Function
def add_two_nums(a,b):
    return a + b
print(add_two_nums(2,3))   # 5

# Lets change the above function to a lamda function
add_two_nums = lambda a, b : a + b
print(add_two_nums(2,3))

# Self invoking lamda function
print((lambda a, b : a+b)(2,3))   # 5

square = lambda x : x ** 2
print(square(3))   # 9
cube = lambda x : x ** 3
print(cube(3))     # 27

# Multiple variable

multiple_variable = lambda a,b,c : a ** 2 - 3 * b + 4 * c
print(multiple_variable(5,5,3))     # 22


#### Lamda function inside anotherr function
def power(x):
    return lambda n : x ** n
cube = power(2)(3)            # # function power now need 2 arguments to run, in separate rounded brackets
print(cube)                   # 8
two_power_of_five = power(2)(5)
print(two_power_of_five)     # 32
