# Sytax 
empty_tuple = ()

# or using the tuple constructor
empty_tuple = tuple()

## Tuple with initial value
tpl = ('item1','item2','item3')
print(tpl)  # ('item1', 'item2', 'item3')
print(len(tpl))  # 3
first_item = tpl[0]
print(first_item)   # item1
second_item = tpl[1]
print(second_item)  # item2
print('\n')


fruits = ('banana', 'orange','mango','lemon')
print(fruits)  # ('banana', 'orange', 'mango', 'lemon')
print(len(fruits)) # 4
first_fruit = fruits[0]
print(first_fruit)  # banana
second_fruit = fruits[1]
print(second_fruit)  # orange
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(last_fruit)   # lemon
print('\n')

# Negative indexing
tpl = ('item1','item2','item3','item4')
first_item = tpl[-4]
print(first_item)  # item1
second_item = tpl[-3]
print(second_item)  #item2
last_item = tpl[-1]
print(last_item)  # item4
print('\n')


fruits = ['banana','orange', 'mango','lemon']
first_fruit = fruits[-4]
print(first_fruit)  # banana

second_fruit = fruits[-3]
print(second_fruit)  # orange

last_fruit = fruits[-1]
print(last_fruit)  # lemon
print('\n')


#### Slicing tuple
tpl = ('item1', 'item2', 'item3','item4')
all_item = tpl[0:] # or all_item = tpl[0:4]
print(all_item) # ('item1', 'item2', 'item3', 'item4')
middle_two_item = tpl[1:3]  # does not include item at index 3
print(middle_two_item) # ('item2', 'item3')


fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
print(all_fruits)           # ('banana', 'orange', 'mango', 'lemon')
all_fruits= fruits[0:]      # all items
print(all_fruits)           # ('banana', 'orange', 'mango', 'lemon')
orange_mango = fruits[1:3]  # doesn't include item at index 3
print(orange_mango)         # ('orange', 'mango')
orange_to_the_rest = fruits[1:]
print(orange_to_the_rest)   # ('orange', 'mango', 'lemon')
print('\n')



#### Range of Negative Indexes

tpl = ('item1', 'item2', 'item3','item4')
all_item = tpl[-4:]
print(all_item)    #('item1', 'item2', 'item3', 'item4')
middle_two_item = tpl[-3:-1]  
print(middle_two_item)     # 'item2', 'item3')

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]    # all items
print(all_fruits)           # ('banana', 'orange', 'mango', 'lemon')
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
print(orange_mango)           # ('orange', 'mango')
orange_to_the_rest = fruits[-3:]
print(orange_to_the_rest)      # ('orange', 'mango', 'lemon')
print('\n')

 #### Changing Tuples to Lists
 # Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)
print(lst)   # ['item1', 'item2', 'item3', 'item4']

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
print(fruits)    # ['banana', 'orange', 'mango', 'lemon']

fruits[0] = 'Apple'
print(fruits)     # ['Apple', 'orange', 'mango', 'lemon']

fruits = tuple(fruits)
print(fruits)   # ('Apple', 'orange', 'mango', 'lemon')
print('\n')

#### Checking an Item in a Tuple
tpl = ('item1', 'item2', 'item3','item4')
print('item2' in tpl)  # True
print('item5' in tpl)  # False

fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True suppose if you give space 'orange ' like this then it give a false value
print('apple' in fruits)  # False
# fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment
print('\n')

#### Joining Tuples
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
print(tpl3)    # ('item1', 'item2', 'item3', 'item4', 'item5', 'item6') 


fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)   # ('banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')



#### Deleting Tuples
tpl1 = ('item1', 'item2', 'item3')
del tpl1
# print(tpl1)  # tpl is deleted it show an error NameError: name 'tpl1' is not defined.

fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
print(fruits)  # fruits is deleted it show an error  NameError: name 'fruits' is not defined