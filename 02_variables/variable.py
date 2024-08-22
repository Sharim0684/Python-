
# Variables in Python

first_name = 'Sharim'
last_name = 'Shaikh'
country = 'India'
city = 'Pune'
age = 22
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Sharim', 
    'lastname':'Shaikh', 
    'country':'India',
    'city':'Pune'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age= 'Sharim', 'Shaikh', 'India', 22

print(first_name, last_name, country, age)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)