### IF Condition

                    #syntax
                    # if condition:
                    #     this part of code run for true condition

a = 3
if a > 0:
    print('A is a Positive Number')  # A is a positive Number


#### IF ELSE
#syntax
  # if condition:
       # this part of code run for true condition
  # else:
       # this part of code runs for false condition

a = 3
if a<0:
    print('A is Nagative number')
else:
    print('A is positive number')   # A is positive number


#### IF ELIF ELSE
        # syntax
        # if condition:
        #     code
        # elif condition:
        #     code
        # else:
        #     code

a = 0
if a > 0:
    print('A is a positive number ')
elif a < 0:
    print('A is a negative number')
else: 
    print('A is Zero')   # A is zero


#### SHORT HAND
        # syntax
        # code if condition else code

a = 3
print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed


#### Nested Conditions
     # syntax
        # if condition:
        #     code
        #     if condition:
        #     code

a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even number')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')   # A is zero
else:
    print('A is a negative number')



### If Condition and Logical Operators

        # syntax
        # if condition and condition:
        #     code

a = 0
if a > 0 and a % 2 == 0:
    print('A is an even and positive integer')
elif a > 0 and a % 2 != 0:
    print('A is a positive interger')
elif a == 0:
    print('A is zero')  # A is zero
else:
    print('A is negative')



#### If and Or Logical Operators
            # syntax
            # if condition or condition:
            #     code

user = 'james'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Access Granted')
else:
    print('Access denied')   # Access denied