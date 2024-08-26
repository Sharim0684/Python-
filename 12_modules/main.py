import mymodule 
print(mymodule.generate_full_name('Sharim','Shaikh'))   # Sharim Shaikh

print(mymodule.sum_of_two(13,22))   # 35

print(mymodule.weight_of_object(100,9.81))  # 981.0

print(mymodule.person['firstname'])
print(mymodule.person['lastname'])
print(mymodule.person['city'])

import statistics
mean_age = statistics.mean(mymodule.age)
print(mean_age)


#### Math module
import math
print(math.pi)    #3.141592653589793
print(math.sqrt(3))  #1.7320508075688772
print(math.floor(9.81))  # 9
print(math.ceil(9.81))   # 10
print(math.log10(100))   # 2

from math import pi
print(pi)


from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2


from math import *
print(pi)                  # 3.141592653589793, pi constant
print(sqrt(2))             # 1.4142135623730951, square root
print(pow(2, 3))           # 8.0, exponential
print(floor(9.81))         # 9, rounding to the lowest
print(ceil(9.81))          # 10, rounding to the highest
print(math.log10(100))     # 2

from math import pi as  PI
print(PI) # 3.141592653589793


#### String module
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


#### Random Module
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive