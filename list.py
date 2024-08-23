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

