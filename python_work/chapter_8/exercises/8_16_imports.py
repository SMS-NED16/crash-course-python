"""IMPORT METHOD 1
import entire module
print(math_operations.square(13))
"""

"""IMPORT METHOD 2
#import a specific function from module
from math_operations import square
print(square(13))
"""

"""IMPORT METHOD 3
#import a specific function from module using alias
from math_operations import square as sq
print(sq(13))"""

"""IMPORT METHOD 4
#import an entire module using an alias
import math_operations as math
print(math.square(13))"""

"""IMPORT METHOD 5
#import all functions in a module
from math_operations import *
print(square(13))"""