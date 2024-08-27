#### Higher Order Function

# 1) A function can take one or more functions as parameters
# 2) A function can be returned as a result of another function
# 3) A function can be modified
# 4) A function can be assigned to a variable



#### FUNCTION AS A PARAMETER

def sum_numbers(nums):   # normal function
    return sum(nums) 

def higher_order_function(f,lst): # Function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers,[1,2,3,4,5])
print(result)    # 15
print('\n')


#### FUNCTION AS A RETURN VALUE

def square(x):  # square function
    return x ** 2

def cube(x):    # Cube Function
    return x ** 3  

def absolute(x):   # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute
    
result = higher_order_function('square')
print(result(3))     # 9
result = higher_order_function('cube')
print(result(3))    # 27
result = higher_order_function('absolute')
print(result(-3))   # 3
print('\n')



#### Python Closures
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add
closure_result = add_ten()
print(closure_result(5))   # 15
print(closure_result(10))  # 22
print('\n')


#### Normal Function
def greeting():
    return 'welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_upparcase = func.upper()
        return make_upparcase
    return wrapper
g = uppercase_decorator(greeting)
print(g())     # WELCOME TO PYTHON

## Let us implement the example above with a decorator

'''This decorator function is a higher order function
that takes a function as a parameter'''

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_upparcase = func.uppar()
        return make_upparcase
    return wrapper
@uppercase_decorator
def greetings():
    return 'Welcome to Python'
print(greeting())



'''These decorator functions are higher order functions
that take functions as parameters'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}.".format(
        first_name, last_name, country))

print_full_name("Sharim", "Shaikh",'India')



#### Built in Higher Order Functions

#### Map() Function
# map(function,iterable)

numbers = [1,2,3,4,5]  # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    #[1,4,9,16,25]

numbers_squared = map(lambda x: x ** 2, numbers)
print(list(numbers_squared))    #[1,4,9,16,25]


numbers_str = ['1','2','3','4','5']  #iterable
numbers_int = map(int,numbers_str)
print(list(numbers_str))        # ['1', '2', '3', '4', '5']


names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
def change_to_upper(name):
    return name.upper()
names_upper_cased = map(change_to_upper,names)
print(list(names_upper_cased))  # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# lets apply it with a lamda function
names_upper_cased = map(lambda name: name.upper(),names)
print(list(names_upper_cased))
print('\n')



#### Python - Filter Function
# the filter function call the specified function which return boolean for each item 
# of the specified iterable(list) it filter the item that satisfy the filtering criteria

# syntax
# filter(function,iterable)


# lets filter only even number
#Example 1
numbers = [1,2,3,4,5]  # iterable
def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even,numbers)
print(list(even_numbers))    # 2,4


#Example 2

numbers = [1,2,3,4,5]  #iterable

def is_odd(num):
    if num % 2 != 0:
        return True
    return False
odd_numbers = filter(is_odd,numbers)
print(list(odd_numbers))    # 1 3 5


# filter long name
names = ['virat','rahul','rohit','siraj']
def is_name_long(name):
    if len(name) > 3:
        return True
    return False

long_names = filter(is_name_long,names)
print(list(long_names))      # ['virat', 'rahul', 'rohit', 'siraj']

