#### Declaring and Calling a Function
# syntax
        # Declaring a function
        # def function_name():
        #     codes
        #     codes
        # # Calling a function
        # function_name()


#### Function Without Parameter
  # function can be declared without parameter
def generate_full_name():
    first_name = 'Sharim'
    last_name  = 'Shaikh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)    # O/P---> Sharim Shaikh
generate_full_name()    # Calling a function

def add_two_num():
    num_one = 3
    num_two = 19
    total = num_one + num_two
    print(total)        # 22
add_two_num()           # Calling a function


#### Function Returning a value - part 1
     # we use return keyword instead of print()
def generate_full_name():
    first_name = 'Sharim'
    last_name = 'Shaikh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())     # Sharim Shaikh

def add_two_num():
    num_one = 13
    num_two = 22
    total = num_one + num_two 
    return total
print(add_two_num())            # 35
print('\n')



#### Function with Parameters
  # In Function we can pass different data type(number,string,boolean,list,tuple,dictionary or set) as a parameter 

### Single Parameter : If our function take a paramter we should call our function wiht an argument

  # syntax
  # Declaring a function
        #   def function_name(parameter):
        #     codes
        #     codes
        #   # Calling function
        #   print(function_name(argument))

def greetings(name):
    message = name + ', welcome to python for Everyone!'
    return message

print(greetings('Sharim'))    # Sharim, welcome to python for Everyone!


def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))    # 100


def square_num(x):
    return x * x
print(square_num(2))    # 4


def area_of_circle(r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(3))   # 28.26


def sum_of_num(n):
    total = 0
    for i in range(n+1):
        total = total + i
    print(total)
print(sum_of_num(10))   # 55
print(sum_of_num(100))  # 5050
print('\n')



#### Two Parameter : A function may also have two or more parameters
  # syntax
  # Declaring a function
        #   def function_name(para1, para2):
        #     codes
        #     codes
        #   # Calling function
        #   print(function_name(arg1, arg2))

def generate_full_name (first_name ,last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Sharim','Shaikh'))    # Full Name:  Sharim Shaikh


def sum_two_num(num_one, num_two):
    sum = num_one + num_two 
    return sum
print('sum of two number ', sum_two_num(3,2))    # sum of two number  5


def calculate_age(current_year, birth_year):
    age = current_year - birth_year 
    return age
print('Age',calculate_age(2024, 2002))  # Age 22

def weight_of_object(mass, gravity):
    weight = str(mass * gravity)+ 'N'    # # the value has to be changed to a string first
    return weight
print('weight of an object in newtons: ',weight_of_object(100,9.81))    # weight of an object in newtons:  981.0N


#### Passing argument with key and value
#If we pass the arguments with key and value, the order of the arguments does not matter.

# syntax
# Declaring a function
        # def function_name(para1, para2):
        #     codes
        #     codes
        # # Calling function
        # print(function_name(para1 = 'John', para2 = 'Doe')) # the order of arguments does not matter here

def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print(print_fullname(firstname = 'Maxwell', lastname = 'glean'))

def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total)
print(add_two_numbers(num2 = 3, num1 = 2)) # Order does not matter
print('\n')


#### Function Returning a Value - Part 2

def print_name(firstname):
    return firstname
print(print_name('David'))   # David

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname + space + lastname
    return full_name
print(print_full_name(firstname='David' , lastname='Miller'))   # David Miller
print('\n')



#### Returning a Number 
def add_two_numbers( num1,num2):
    total = num1 + num2
    return total
print(add_two_numbers(2,3))    # 5


def calculate_age(current_year , birth_date):
    age = current_year - birth_date
    return age
print(calculate_age(2024 , 2002))   #22 
print('\n')


#### Returning a  Boolean 
def is_even(n):
    if n % 2 == 0:
        return True
    return False
print(is_even(10))   # True
print(is_even(3))    # False
print('\n')


#### Returning a list 
def find_even_numbers(n):
    even = []
    for i in range(n + 1):
        if i % 2 == 0:
            even.append(i)
    return even
print(find_even_numbers(10))  #[0,2,4,6,8,10]
print('\n')



#### Fuction with Default parameters
# syntax
# Declaring a function
                # def function_name(param = value):
                #     codes
                #     codes
                # # Calling function
                # function_name()
                # function_name(arg)

def greetings(name = 'Sharim'):
    n = name + ' welcome to python '
    return n
print(greetings())    # Sharim Welcome to the python

def generate_full_name (firstname ='Sharim',lastname = 'Shaikh'):
    space = ' '
    full_name = firstname + space + lastname
    return full_name
print(generate_full_name())    # Sharim Shaikh

def calculate_year(birth_year , current_year = 2024):
    age = current_year - birth_year
    return age
print(calculate_year(2002))   # 22
print('\n')

#### Arbitrary Number of Arguments
# syntax
# Declaring a function
        # def function_name(*args):
        #     codes
        #     codes
        # # Calling function
        # function_name(param1, param2, param3,..)
        
def sum_all_nums(*nums):
    total = 0
    for i in nums:
        total += i
    return total
print(sum_all_nums(2,3,4,5))  # 14


#### Default and Arbitrary Number of Parameters in Functions
def generate_groups(team,*args):
    for i in args:
        print(i)
print(generate_groups('team-1','Brook','dravid','maxwell','miller'))
print('\n')


#### Function as a Parameter of Another Function
def square_number (n):
    return n * n
def do_something(f,x):
    return f(x)
print(do_something(square_number,3))  # 9