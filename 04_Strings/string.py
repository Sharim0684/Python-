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