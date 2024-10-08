empty_list = list() # this is an empty list, no item in the list
print(len(empty_list)) # 0

fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and it length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Number of countries:', len(countries))

# Modifying list

fruits = ['banana', 'orange', 'mango', 'lemon'] 
first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# Accessing items
fruits = ['banana', 'orange', 'mango', 'lemon'] 
last_fruit = fruits[-1]
second_last = fruits[-2]
print(last_fruit)       # lemon
print(second_last)      # mango

#  Slicing items
fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[0:4] # it return all the fruits
# this is also give the same result as the above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the end index
orange_mango_lemon = fruits[1:]
print('\n')
fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[-4:] # it returns all the fruits
# this is also give the same result as the above
orange_and_mango = fruits[-3:-1] # it does not include the end index
orange_mango_lemon = fruits[-3:]

fruits = ['banana', 'orange', 'mango', 'lemon'] 
fruits[0] = 'Avocado'
print(fruits)  # ['avocado', 'orange', 'mango', 'lemon'] 
fruits[1] = 'apple'
print(fruits) # ['avocado', 'apple', 'mango', 'lemon'] 
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)  # ['avocado', 'orange', 'mango', 'lime'] 
print('\n')

#  checking items

fruits = ['banana', 'orange', 'mango', 'lemon']
does_exit = 'banana' in fruits
print(does_exit)  # True
does_exit = 'lime' in fruits 
print(does_exit)  # False
print('\n')

# Append 
fruits = ['banana','orange','mango','lemon']
fruits.append('apple')
print(fruits)  # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')
print(fruits) # ['banana','orange', 'mango', 'lemon' , 'apple', 'lime']
print('\n')


#insert 

fruits = ['banana','orange', 'mango', 'lemon']
fruits.insert(2,'apple') # insert apple between orange and mango
print(fruits)  #['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3,'lime') 
print(fruits) # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print('\n')


# remove
fruits = ['banana','orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)   # ['orange', 'mango', 'lemon']
fruits.remove('lemon')
print(fruits)   #['orange','mango']
print('\n')

# POP
fruits = ['banana','orange', 'mango', 'lemon']
fruits.pop()
print(fruits)   # ['banana','orange', 'mango']

fruits.pop(0)
print(fruits)   # ['orange', 'mango']
print('\n')

#del 
fruits = ['banana','orange','mango','lemon']
del fruits[0]
print(fruits)  # ['orange', 'mango', 'lemon']

del fruits[1]
print(fruits)   # ['orange', 'lemon']

# del fruits
# print(fruits)   # this shoud give nameError i.e name 'fruits' not defined
print('\n')

#### clear

fruits=['banana','orange','mango','lemon']
fruits.clear()
print(fruits)   # []  --> it clear the list and show only empty list
print('\n')

#### copying a list

fruits = ['banana','orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)  # ['banana', 'orange', 'mango', 'lemon']
print('\n')


### join
positive_number = [1,2,3,4,5]
zero = [0]
negative_number = [-5,-4,-3,-2,-1]
integer = negative_number + zero + positive_number
print(integer)     # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)  # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
print('\n')


#### join with extend
num1 = [0,1,2,3]
num2 = [4,5,6]
num1.extend(num2)
print('Numbers:', num1)  # Numbers: [0, 1, 2, 3, 4, 5, 6]
negative_number = [-5,-4,-3,-2,-1]
positive_number = [1,2,3,4,5]
zero = [0]

negative_number.extend(zero)
negative_number.extend(positive_number)
print('Integer:',negative_number)  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

fruits = ['banana', 'orange', 'mango','lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', ' Onion', 'Carrot']
fruits.extend(vegetables)
print('fruits_and_vegetables', fruits)  #fruits_and_vegetables ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', ' Onion', 'Carrot']
print('\n')


#### count 
fruits = ['banana','orange','mango','lemon']
print(fruits.count('orange'))   # 1
ages = [22,19,24,25,26,24,25,24]
print(ages.count(24))  # 3
print('\n')


#### index
fruits = ['banana','orange','mango','lemon']
print(fruits.index('orange'))   # 1
ages = [22,19,24,25,26,25,24]
print(ages.index(24))   # 2
print('\n')


#### Reverse
fruits = ['banana','orange','mango','lemon']
fruits.reverse()
print(fruits)   # ['lemon', 'mango', 'orange', 'banana']
ages = [22,19,24,25,26,25,24]
ages.reverse()
print(ages)  # [24, 25, 26, 25, 24, 19, 22]
print('\n')



#### Sort 
fruits = ['banana','orange','mango','lemon']
fruits.sort()
print(fruits)  # ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse = True)
print(fruits)   # ['orange', 'mango', 'lemon', 'banana']
ages = [22,19,24,25,26,25,24]
ages.sort()
print(ages)   # [19, 22, 24, 24, 25, 25, 26]
ages.sort(reverse = True)
print(ages)   # [26, 25, 25, 24, 24, 22, 19]