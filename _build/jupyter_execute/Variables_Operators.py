#!/usr/bin/env python
# coding: utf-8

# ## Variables

# In programming variables refers to a "name" for a value. This "name" can have different values over the course of program and hence it is referred as a variable. 
# The concept of variable in programming is similar to some of terms used in natural languages to refer to different things. For instance, in a classroom there are students with different _names_. Here the word _name_ is a variable which has differnt _value_ for each student i.e. their name.

# In[1]:


a = 2


# The above statement initializes a variable named 'a' with a numeric value of 2 and it is refered to as an **Assignment Statement**. Similarly, the statement below initializes a variable with name 'test' and assigns a string value of 'Happy'

# In[2]:


test = 'Happy'


# We can print the value of a variable using the `print` command i.e.

# In[4]:


print(a)


# In[6]:


print(test)


# The value assigned to a variable can be changed within the program. This feautre make variable very useful and are extensively used in progamming. A variable, for example, can be used to store user input. 

# Each variable in Python has 6 properties associated with it. For now only first three are required since the last three are for advanced programmers. These properties are
# 1. Name
# 2. Value
# 3. Type
# 4. Scope
# 5. Life time
# 6. Memory location
# 
# The firt two properties i.e. name and value we have already seen above. Type for a variable refers to it's data type i.e. whether the variable is an integer, float, string, boolean etc. 

# In Python, the type for a variable is decided at the time of initialization. This behaviour is different from languages like C where the type of the variable has to be declared explicitly. In the example above, we can change the variable 'a' to a non numeric value. To check the type for a particular variable, `type()` function can be used as follows.
# 

# In[3]:


print(type(a))
print(type(test))


# In[ ]:


x = 7
y = 7.0
print(type(x))
print(type(y))


# Variable names are case sensitive, e.g. in the code below there are four different variables such that their name differ only in the case used for the letters.
# 

# In[12]:


bat = 4
BAT = 5
Bat = 6
bAT = 7
print (bat)
print (BAT)
print (Bat)
print (bAT)


# ## Operators

# An operator is a special symbol that instructs the compiler/interpreter to execute specific mathematical or logical operations. These symbols _operate_ on set of variable or scaler or both. Operand refers to the value that operator operates on. E.g., in the equation 2+3 '+' is an operator and 2 and 3 are operands. 

# In Python there are 6 different classes of operators. These are:
# 1. Arithmetic operators
# 2. Comparison operators
# 3. Logical operators
# 4. Assignment operators
# 5. Bitwise operators
# 6. Special operators
# 
# Let's understand each of these classes through some examples

# ### Arithmetic operators
# As the name suggests this class of operators are used to perform mathematical operation on the operands. Following is the list of arithemetic operators available in Python.

# | Operator Symbol | Meaning | Example |
# | :---: | --- | --- | 
# | + | Addition | 2 + 2 = 4 | 
# | - | Subtraction | 5 - 2 = 3 |
# | * | Multiplication | 2 * 3 = 6 |
# | / | Division | 4 / 2 = 2|
# | % | Modulus | 4 % 2 = 0 |
# | // | Floor division | 5 // 2 = 2 |
# | ** | Exponent | 2 ** 3 = 8 | 

# In[4]:


x = 4
y = 5

print (x+y+2)
print (x-y+2)


# ### Comparison operator
# These operators are used to compare operands and the output from their operation is a boolean value i.e. either `True` or `False` or equivalently `1` or `0`.

# Following is the list of arithemetic operators available in Python.
# 
# | Operator Symbol | Meaning | Example |
# | :---: | --- | --- | 
# | > | Greater than | 3 > 2 is `True` | 
# | < | Less than | 3 < 2 is `False` |
# | == | Equal to | 2 == 3 is `False` |
# | != | Not equal to | 2 != 3 is `True` |
# | >= | Greater than or equal to | 4 >= 2 is `True` |
# | <= | Less than or equal to | 5 <= 2 is `False` |

# In[5]:


x = 4
y = 5
print (x+y > 10)


# ### Logical operators

# There are 3 logical operators `and`, `or`, and `not`.
# 
# | Operator Symbol | Meaning |
# | :---: | --- |
# | and | True if both operands are true |
# | or | True if either of the operands is true |
# | not | True if operands are false |
# 

# In[14]:


x = True
y = False
print (x and y)
print (x or y)
print (not x)


# In[9]:


x=5
y=6
z=7
print (x<y and y<z)


# ### Assignment operators
# Operators in this class are used to `assign` values to variables. The syntax for using these operators is variable name followed by operator followed by the value that is to be assigned. Some of the assignment operator behave equivalent to the mathematical operation performed by arithmetic operators.

# Following is the list of assignment operators available in Python.
# 
# | Operator Symbol | Meaning | Example |
# | :---: | --- | --- | 
# | = | Assign value on the right to variable on the left | x = 5 | 
# | += | Increment value of the variable by value on the right | x += 5 (x = x + 5) |
# | -= | Decrement value of the variable by value on the right | x -= 5 (x = x - 5) |
# | *= | Multiple value of the variable by value on the right | x *= 5 (x = x * 5) |
# | /= | Divide value of the variable by value on the right | x /= 5 (x = x / 5) |
# | %= | Modulus for the value of the variable by value on the right | x %= 5 (x = x % 5) |
# | //= | Floor division of value of the variable by value on the right | x //= 5 (x = x // 5) |
# | **= | Exponent value of the variable by value on the right | x &ast;&ast;= 5 (x = x &ast;&ast; 5) |
# 

# In[6]:


x = 6
y = 5
x *= 2
y **= 2
print (x)
print (y)


# In[8]:


x = False
print(type(x))

