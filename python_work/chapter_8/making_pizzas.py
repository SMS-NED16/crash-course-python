
"""
GENERAL IMPORT - Imports all functions defined in pizza
pizza is a .py file in the same directory as this file
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')"""

"""SPECIFIC IMPORT
Importing a specific function defined in pizza
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')"""

"""FUNCTION ALIAS with SPECIFIC IMPORTS"""
"""from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')"""

"""MODULE ALIAS WITH GENERIC IMPORT"""
"""import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms','green peppers', 'extra cheese')
"""

"""Importing all functions in a module"""
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
