       # 1.Creating variables and assigning values to them
# To create a variable in Python, all you need to do is specify the variable name, and then assign a value to it.

# <variable name> = <value>

# Python uses = to assign values to variables. There's no need to declare a variable in advance (or to assign a data
# type to it), assigning a value to a variable itself declares and initializes the variable with that value. There's no way to
# declare a variable without assigning it an initial value.
# # Integer
a = 2
print(a)
# Output: 2
# Integer    
b = 9223372036854775807
print(b)
# Output: 9223372036854775807
# Floating point
pi = 3.14
print(pi)
# Output: 3.14
# String
c = 'A'
print(c)
# Output: A
# String    
name = 'John Doe'
print(name)
# Output: John Doe
# Boolean    
q = True
print(q)
# Output: True
# Empty value or null data type
x = None
print(x)
# Output: None


#you can not use python's keywords as a valid variable name. You can see the list of keyword by:
import keyword
print(keyword.kwlist) # Output: ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


# Rules for variable naming:
# Variables names must start with a letter or an underscore.1.
x  = True   # valid
_y = True   # valid
# 9x = False  # starts with numeral
 # => SyntaxError: invalid syntax  
 # $y = False #  starts with symbol
 # => SyntaxError: invalid syntax
 
# The remainder of your variable name may consist of letters, numbers and underscores.2.
has_0_in_it = "Still Valid"


# Names are case sensitive.3.
x = 9  
y = X*5  #  =>NameError: name 'X' is not defined

# Even though there's no need to specify a data type when declaring a variable in Python, while allocating the
# necessary area in memory for the variable, the Python interpreter automatically picks the most suitable built-in
# type for it:
a = 2
print(type(a))
# Output: <type 'int'>
b = 9223372036854775807
print(type(b))
# Output: <type 'int'>
pi = 3.14
print(type(pi))
# Output: <type 'float'>
c = 'A'
print(type(c))
# Output: <type 'str'>
name = 'John Doe'
print(type(name))
# Output: <type 'str'>
q = True
print(type(q))
