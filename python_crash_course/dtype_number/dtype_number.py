# variable creation
import math
from decimal import Decimal as D

my_var = 12
my_var2 = 12.2

# checking data type
print(type(my_var))
print(type(my_var2))

# adding int type with a float type
my_var3 = (my_var + my_var2)

print(my_var3)
print(type(my_var3))

# Python order of operation
print((1+2)*3)
print(2**3)
print(5 % 2)
print(4 % 2)
print(7 % 3)
print((1.1+2.2) == 3.3)
print(1.1 + 2.2)


# using decimal module
print(D('1.1') + D('2.2') == D('3.3'))
print(type(D('1.1')))


# using math module
print(math.pi)
print(math.sqrt(9))
