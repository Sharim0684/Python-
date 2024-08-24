# Set is a collection of items. Let me take you back to your elementary or high school Mathematics lesson. The Mathematics definition of a set can be applied also in Python. Set is a collection of unordered and un-indexed distinct elements. In Python set is used to store unique items, and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.

#### Creating a Set
    # We use the set() built-in function.

    # Creating an empty set

# syntax
st = set()

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
print(st)
# syntax
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits)


# Getting Set's Length
# We use len() method to find the length of a set.

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
print(len(st))  # 4
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits))  # 4


# Checking an Item
# To check if an item exist in a list we use in membership operator
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True
print('\n')


# Adding Items to a Set
# Once a set is created we cannot change any items and we can also add additional items.

# Add one item using add()

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
print(st)   # {'item4', 'item2', 'item1', 'item5', 'item3'}

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
print(fruits)  #{'lemon', 'banana', 'orange', 'lime', 'mango'}
print('\n')


#### add()
# Add multiple items using update() The update() allows to add multiple items to a set. The update() takes a list argument.
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
print(st)    #{'item4', 'item6', 'item3', 'item2', 'item5', 'item1', 'item7'}

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits)   # {'orange', 'carrot', 'onion', 'potato', 'tomato', 'banana', 'mango', 'lemon', 'cabbage'}
print('\n')


#### remove()
# We can remove an item from a set using remove() method. If the item is not found remove() method will raise errors, so it is good to check if the item exist in the given set. However, discard() method doesn't raise any errors.

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
print(st)   # {'item4', 'item3', 'item1'}
print('\n')

#### POP()
  # The pop() methods remove a random item from a list and it returns the removed item.

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set
print(fruits)   #{'mango', 'lemon', 'banana'}

fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop() 
print(removed_item)   # some random fruit is pop and show its name in o/p
print('\n')

#### Clear()
   
   # syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
print(st)  # set() i.e all data is clear only remain set()

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()
print('\n')

#### Delete 
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
del st
# print(st)  # NameError: name 'st' is not defined.


# Converting List to Set
# We can convert list to set and set to list. Converting list to set removes duplicates and only unique items will be reserved

# syntax
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered
print(st)   # {'item1', 'item3', 'item4', 'item2'}

fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}
print(fruits)        # {'lemon', 'banana', 'mango', 'orange'}
print('\n')


#### join()
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print(st3)   # {'item2', 'item7', 'item1', 'item6', 'item5', 'item4', 'item8', 'item3'}


fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
print('\n')


#### update()
  # syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # st2 contents are added to st1
print(st1)  # {'item4', 'item5', 'item8', 'item1', 'item2', 'item6', 'item3', 'item7'}

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
print('\n')


#### Intersection()
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
print(st1.intersection(st2)) # {'item3', 'item2'}
  
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.intersection(even_numbers)) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.intersection(dragon))     # {'o', 'n'}
print('\n')



# Checking Subset and Super Set
# A set can be a subset or super set of other sets:

# Subset: issubset()
# Super set: issuperset

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.issubset(st1)) # True
print(st1.issuperset(st2)) # True


whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.issubset(even_numbers)) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.issubset(dragon))     # False
print('\n')



# Checking the Difference Between Two Sets
# It returns the difference between two sets.
# in that same value will be deleted
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.difference(st1) )# set()
print(st1.difference(st2)) # {'item1', 'item4'} => st1\st2

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.difference(even_numbers) )# {1, 3, 5, 7, 9}

 
python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.difference(dragon))     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
print(dragon.difference(python) )    # {'d', 'r', 'a', 'g'}
print('\n')



#Finding Symmetric Difference Between Two Sets
# syntax In that similar element is remove and all digit order
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
print(st2.symmetric_difference(st1)) # {'item1', 'item4'}

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
print(whole_numbers.symmetric_difference(some_numbers)) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.symmetric_difference(dragon))  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
print('\n')


### joinig set
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.isdisjoint(st1)) # False

even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers)) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.isdisjoint(dragon))  # False, there are common items {'o', 'n'}