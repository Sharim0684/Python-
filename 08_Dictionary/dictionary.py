# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.


#### Creating a Dictionary
   # To create a dictionary we use curly brackets, {} or the dict() built-in function.

# Syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1','key2':'value2','key3':'values3','key4':'value4'}
print(dct)   # {'key1': 'value1', 'key2': 'value2', 'key3': 'values3', 'key4': 'value4'}


#### Dictionary Length
   # If check the number of key:value pairs in the dictionary


dct = {'Key1':'value1','Key2':'value2','key3':'value3','key4':'value4'}
print(len(dct))  # 4


person = {
    'first_name':'Sharim',
    'last_name': 'Shaikh',
    'age' : 22,
    'country' : 'India',
    'skills' : ['C','C++','Python','HTML5','CSS','Js'],
    'address':{
        'street':'space street'
    }
}
# The dictionary above shows that a value could be any data types : string, boolean, list,tuple,set or dictionary.
print(len(person))   # 6


### Accessing Dictionary items
  # we can access Dictionary items by referring to its key name


dct = {'key1':'value1','Key2':'value2','key3':'value3','key4':'value4'}
print(dct)   # {'Key1': 'value1', 'Key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(dct['key1'])   # value1
print(dct['key4'])   # value4
print('\n')

person = {
    'first_name':'Sharim',
    'last_name': 'Shaikh',
    'age' : 22,
    'country' : 'India',
    'skills' : ['C','C++','Python','HTML5','CSS','Js'],
    'address':{
        'street':'space street'
    }
}

print(person['first_name'])  # Sharim
print(person['country'])   # India
print(person['skills'])     # ['C', 'C++', 'Python', 'HTML5', 'CSS', 'Js']
print(person['skills'][0])   # c
print(person['skills'][1])   # c++
print(person['address']['street'])   # Space Street
print('\n')


person = {
    'first_name':'Sharim',
    'last_name': 'Shaikh',
    'age' : 22,
    'country' : 'India',
    'skills' : ['C','C++','Python','HTML5','CSS','Js'],
    'address':{
        'street':'space street'
    }
}
print(person.get('first_name'))  #Sharim
print(person.get('last_name'))   #Shaikh
print(person.get('skills'))      #['C', 'C++', 'Python', 'HTML5', 'CSS', 'Js']
print(person.get('age'))         # 22
print('\n')


#### Adding items to a dictionary
      # we can add new key and value pair to a dictionary

dct = {'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
dct['key5'] = 'value5'
print(dct)      #{'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5'}
print('\n')


person = {
    'first_name':'Sharim',
    'last_name': 'Shaikh',
    'age' : 22,
    'country' : 'India',
    'skills' : ['C','C++','Python','HTML5','CSS','Js'],
    'address':{
        'street':'space street'
    }
}
person['job_title'] = 'Python Developer'
person['skills'].append('HTML')
print(person)    # {'first_name': 'Sharim', 'last_name': 'Shaikh', 'age': 22, 'country': 'India', 'skills': ['C', 'C++', 'Python', 'HTML5', 'CSS', 'Js', 'HTML'], 'address': {'street': 'space street'}, 'job_title': 'Python Developer'}
print('\n')


#### Modifying Items in a Dictionary
    # we can modify items in a dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'
print(dct)           # {'key1': 'value-one', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print('\n')


person = {
    'first_name':'Sharim',
    'last_name': 'Shaikh',
    'age' : 22,
    'country' : 'India',
    'skills' : ['C','C++','Python','HTML5','CSS','Js'],
    'address':{
        'street':'space street'
    }
}
person['first_name'] = 'Sarim',
print(person)          # {'first_name': ('Sarim',), 'last_name': 'Shaikh', 'age': 22, 'country': 'India', 'skills': ['C', 'C++', 'Python', 'HTML5', 'CSS', 'Js'], 'address': {'street': 'space street'}}
print('\n')

#### Checking Key in a Dictionary

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct)  #True
print('key5' in dct)  #False
print('\n')



#####  Removing Key and Value Pairs from a Dictionary
    # pop(key): removes the item with the specified key name:
    # popitem(): removes the last item
    # del: removes an item with specified key name

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1')    # remove key1 item
print(dct)         #{'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}  
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem()       # removes the last item
print(dct)          #{'key1': 'value1', 'key2': 'value2', 'key3': 'value3'} 
del dct['key2']     # remove key2 item
print(dct)          # {'key1': 'value1', 'key3': 'value3'}
print('\n')

person = {
    'first_name':'Sharim',
    'last_name': 'Shaikh',
    'age' : 22,
    'country' : 'India',
    'skills' : ['C','C++','Python','HTML5','CSS','Js'],
    'address':{
        'street':'space street'
    }
}
person.pop('address')
print(person)      # {'first_name': 'Sharim', 'last_name': 'Shaikh', 'age': 22, 'country': 'India', 'skills': ['C', 'C++', 'Python', 'HTML5', 'CSS', 'Js']}
person.popitem()   # remove the last item
print(person)      #{'first_name': 'Sharim', 'last_name': 'Shaikh', 'age': 22, 'country': 'India'}
del person['country']
print(person)       # {'first_name': 'Sharim', 'last_name': 'Shaikh', 'age': 22}
print('\n')


#### Changing Dictionary to a List of items
       # items() method changes dictionary to a list of tuple

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items())   # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
print('\n')


#### Clearing a Dictionary
  # if we don't want the items in a dictionary we can clear them usign clear() method

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None


#### Deleting a Dictionary
  # if we do not use the dictionary we can delete it complately

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct
# print(dct)   # NameError: name 'dct' is not defined. 


# #### Copy a Dictionary
    # We can copy a dictionary using a copy() method. Using copy we can avoid mutation of the original dictionary.

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy()
print(dct_copy)  #{'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print('\n')


#####  Getting Dictionary Keys as a List
    # The keys() method gives us all the keys of a a dictionary as a list.

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)   #dict_keys(['key1', 'key2', 'key3', 'key4'])


#### Getting Dictionary Values as a List
# The values method gives us all the values of a a dictionary as a list.

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values =dct.values()
print(values)   # dict_values(['value1', 'value2', 'value3', 'value4'])  
