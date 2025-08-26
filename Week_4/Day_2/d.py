
# Import the whole module

import math
# print(math.sqrt())  # This will give type error due to value not included
print(math.sqrt(5))

# import as an alias
import math as m 
print(m.sqrt(4))  #  using m shortens the module name

# Import specific functions or variables
from math import sqrt, pi

print(sqrt(3))
print(pi)


# - import * ( import everything from the module) This is usually not recommended because it can cause name conflits if two modules have functions with the same name
from math import *
print(sqrt(49))
print(pi)


