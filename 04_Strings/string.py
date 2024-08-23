# Single line comment

letter = 'P'
print(letter)   # p
print(len(letter)) # 1
greeting = 'Hello, World!' # String could be a single or Double quote, "Hello, World!"
print(greeting)    # Hello, World!
print(len(greeting)) # 13
sentence = "I hope Python is easy programming language"
print(sentence)  #I hope Python is easy programming language
print('\n')
# multiple string

multiline_string = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(multiline_string)
print('\n')

# Another way of doing the same thing
multiline_string = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(multiline_string)
print('\n')


# String Concatenation
first_name = 'Sharim'
last_name = 'Shaikh'
space = ' '
full_name = first_name + space + last_name
print(full_name)  # Sharim Shaikh

# checking length of a string using len() built in function

print(len(first_name))  # 6
print(len(last_name))   # 6 
print(len(first_name) >= len(last_name))  # True
print(len(full_name))   # 13

# Unpacking Characters
print('\n')
language = 'Python'
a,b,c,d,e,f = language   # unpacking sequence character into variables
print(a)  # p
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n


# Accessing character in string by index

print('\n')
language = 'Python'
first_letter = language[0]
print(first_letter)  # p
second_letter = language[1]
print(second_letter)  # y
third_letter = language[2]
print(third_letter)  # t
last_index = len(language) - 1  # print(last_index)---> 5
last_letter = language[last_index]
print(last_letter)  # n
print('\n')


# if we want to start from right end we can use negative indexing. -1 is the last index

language = 'python'
last_letter = language[-1]
print(last_letter)  # n

second_last = language[-2]
print(second_last)   # o

third_last = language[-3]
print(third_last)   # h
print('\n')   


# Slicing

language = 'Python'
first_three = language[0:3] # Start at zero index and up to 3 but not include 3
print(first_three)  # pyt
last_three = language[3:6]  # start at three and up to 6 but not include 6
print(last_three)  # hon
# Another way
last_three = language[-3:]
print(last_three)  # hon
# Another way
last_three = language[3:]
print(last_three)  # hon
print('\n')

# Skipping character while spliting python strings
language = 'Python'
pto = language[0:6:2] 
print(pto)  # pto
print('\n')

# Escape Sequence 
print('We are the so-called "Vikings"\nfrom the north.')  # line break
print('We are the\tso-called\t "Vikings" \tfrom the north.')
print('Day 1\t3\t5')   # Day 1   3       5
print('Day 2\t3\t5')   # Day 2   3       5
print('Day 3\t3\t5')   # Day 3   3       5
print('Day 4\t3\t5')   # Day 4   3       5
print('This is a back slash symbol (\\)') # To write a black slash
print('In every programming language it starts with \"Hello, World!\"')
print('\n')


#### STRING METHODS
## capitalize() : converts the first character the string to capital letter 
challenge = "thirty days of Python"
print(challenge.capitalize())  # Thirty days of python


#### Count() : return occurrences of substring  in string , count(substring, start = .., end=..)
challenge = 'thirty days of python'
print(challenge.count('y'))   # 3
print(challenge.count('y',7,14))  # 1 , 7 and 14 is starting and ending index
print(challenge.count('th'))  # 2
print('\n')

#### endwith() : check if a string ends with a specified ending
challenge = 'thirty days of python'
print(challenge.endswith('on'))  # True
print(challenge.endswith('tion'))  # false
print('\n')

#### expantabs(): Replace ta character with  spaces, default tab size is 8. It takes tab size argument

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs()) # thirty  days    of      python
print(challenge.expandtabs(10)) #thirty    days      of        python
print('\n')

#### Find(): Return the index of first occurrence of substring
challenge = 'thirty days of Python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0
print(challenge.find('o'))  # 12 
print('\n')

#### format() formats string into nicer output
first_name = 'Sharim'
last_name  = 'Shaikh'
country =  'India'
sentence = ' I am {} {}. I live in {}'.format(first_name,last_name,country)
print(sentence) # I am Sharim Shaikh. I live in India

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of circle with {} is {}'.format(str(radius),str(area))
print(result)  # The area of circle with 10 is 314.0
print('\n')


#### index() : return the index of substring
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th'))  # 0
print('\n')


# isalnum() : checks alphanumeric character or if space occured it give an false value
challenge = 'thirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum())  #True

challenge = 'thirty days of python 2019'
print(challenge.isalnum())  #False

challenge = 'thirtydays of python' 
print(challenge.isalnum())  # False
print('\n')

#### isalpha(): checks if all character are alphabets like abcdef......
challenge  = 'abcd'
print(challenge.isalpha())  #True
challenge = 'thirty days of python'
print(challenge.isalpha())  #False
num = '123'
print(num.isalpha())  # False
print('\n')

### isdecimal(): check decimal character
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th'))  # 0
print('\n')


### isdigit() : check digit character
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit()) # True
print('\n')


### isdecimal() : check decimal character

num = '10'
print(num.isdecimal()) # True
num = '10.5'
print(num.isdecimal()) # False



