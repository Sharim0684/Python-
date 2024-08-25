# While Loop
 # It is used to execute a block of statements repeatedly until a given condition is satisfied.

        # syntax
        # while condition:
        #     code goes here
count = 0
while count < 5:
    print(count)
    count = count + 1
    # print the number 0,1,2,3,4
print('\n')



### WHILE ELSE 
  # syntax
        # while condition:
        #     code goes here
        # else:
        #     code goes here
count = 0
while count < 5:
    print(count)   
    count = count + 1
else:
    print(count)
    # in that code 1st of all while loop is execute and print 0,1,2,3,4 and then 
    # while loop condition false then else will be execute and print 5 then the outout will
    # be printed on screen is 0,1,2,3,4,5
print('\n')


#### BREAK  - Part 1
      # break: we use break when we like to get out of loop or stop the loop
      # syntax
            # while condition:
            #     code goes here
            #     if another_condition:
            #         break
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
print('\n')
    # In that we use a break condition in that condition we declared a condition when value == 3 then break the loop
    # so output of this code is --> 0,1,2


####  CONTINUE Part - 1
       # continue : with the condition statement we can skip the current iteration and continue with the next
         # syntax
            # while condition:
            #     code goes here
            #     if another_condition:
            #         continue
count = 0
while count < 5:
    print(count)
    count = count + 1
    if(count == 2):
        continue 
    # o/p ---> 0 1 2 3 4
print('\n')

count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1
print('\n')
    # The above while loop only prints 0, 1, 2 and 4 (skips 3).



#### For Loop with list
  # syntax
        # for iterator in lst:
        #     code goes here
numbers = [0,1,2,3,4,5]
for number in numbers:   # # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)        # # the numbers will be printed line by line, from 0 to 5
print('\n')


#### For loop witg string
   # syntax
        # for iterator in string:
        #     code goes here
language = 'Python'
for letter in language:
    print(letter)  # o/p --> p y t h o n
print('\n')

for i in range(len(language)):
    print(language[i])    # p y t h o n
print('\n')


#### For loop with tuple
  # syntax
        # for iterator in tpl:
        #     code goes here
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)  # o/p --> 0 1 2 3 4 5
print('\n')


####  For loop with Dictionary
  # syntax
        # for iterator in dct:
        #     code goes here
person = {
    'first_name':'Sharim',
    'last_name' : 'Shaikh',
    'age':22,
    'Country':'India',
    'skills' : ['C','C++','Python','HTML','CSS','JS','React'],
    'address':{
        'Street':'Space street'
    }
}
for key in person:
    print(key)  # o/p --> print all keys first_name,last_name,age,country,skills,addrress
print('\n')

for key, value in person.items():
    print(key,value)   # o/p --> # this way we get both keys and values printed out
print('\n')


#### Loops in set
    # syntax
        # for iterator in st:
        #     code goes here
it_companies = {'Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'}
for company in it_companies:
    print(company)  # it print all IT companies
print('\n')


####   BREAK PART - 2
  # syntax
        # for iterator in sequence:
        #     code goes here
        #     if condition:
        #         break
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)   
    if number == 3:  
        break      # o/p ---> 0 1 2 3
print('\n') 



#### CONTINUE PART - 2
  # syntax
        # for iterator in sequence:
        #     code goes here
        #     if condition:
        #         continue
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('next number should be',number + 1) if number != 5 else print('loop end')
print('outside the loop')
print('\n')


#### The Range Function

'''The range() function is used list of numbers. The range(start, end, step) takes three parameters: starting, ending and increment. 
By default it starts from 0 and the increment is 1. The range sequence needs at least 1 argument (end).
 Creating sequences using range'''

lst = list(range(11))
print(lst)      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1,11))   # 2 argument that 1 and 11 i.e 1 indiacte that stating sequence and 11 indicate that ending sequence
print(st)       # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst)      # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st)       # {0, 2, 4, 6, 8, 10}
print('\n')


### Syntax 
   # For iteractor in range(start,end,step)

for number in range(11):
    print(number)   # print 0 to 10 not including 11
print('\n')


#### Nested For Loop
# we can write loop inside a loop
    #syntax
        # for x in y:
        #     for t in x:
        #         print(t)


person = {
    'first_name':'Sharim',
    'last_name' : 'Shaikh',
    'age':22,
    'Country':'India',
    'skills' : ['C','C++','Python','HTML','CSS','JS','React'],
    'address':{
        'Street':'Space street'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)   # o/p --> c,c++,python,HTML,CSS,JS
print('\n')



#### For Else
  # syntax
        # for iterator in range(start, end, step):
        #     do something
        # else:
        #     print('The loop ended')
for number in range(11):
    print(number)   
    print('The loop stops at', number)   
print('\n')
# 0
# The loop stops at 0
# 1
# The loop stops at 1
# 2
# The loop stops at 2
# 3
# The loop stops at 3
# 4
# The loop stops at 4
# 5
# The loop stops at 5
# 6
# The loop stops at 6
# 7
# The loop stops at 7
# 8
# The loop stops at 8
# 9
# The loop stops at 9
# 10
# The loop stops at 10



#### PASS
for number in range(6):
    pass