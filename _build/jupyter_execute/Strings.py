#!/usr/bin/env python
# coding: utf-8

# ## Strings

# In programming string refers to a sequence of characters that can act as a variable or constant. This is the most popular data type in Python. In fact the increasingly strong prevelance of Python in Bioinformatics is primarily due to its ability to easily perform different operations of strings. A string variable can be assigned using single or double quotes.

# In[1]:


var1 = 'String A'
var2 = "String B"
print (var1)
print (var2)


# Value for a string variable can be changed simple by reassigning with a new value.

# In[2]:


var1 = 'String number two'
print (var1)
print("Another string")


# Length of the string can be determined using the `len` function.

# In[3]:


len(var2)


# In[4]:


var1 = 'Hello'
var2 = 'World'
print(var1+var2)


# ### String concatenation
# The arithmetic operator + and * can be used directly with string to concatenate (addition) or repeat (multiplication).

# In[ ]:


"Hello"+"World"


# In[ ]:


var1 = "Hello"
var2 = "World!"
print (var1+var2)


# In[5]:


var3 = var1*3
print(var3)

5*3
5+5+5


# ### Slice of a string
# Slice is another very useful operator that can be used to manipulate strings. The slice operator `[]` gives the character within the start and end positions separated by a colon. The numbering of characters within a string start from 0. Note that the start position character is included in the output but the end position character is not. Slicing effectively return the substring of a given string. The general syntax for slicing a string is as follows:
string[start:end]
string[start:]
string[:end]
string[start:end:step]
string[:]
# In[6]:


var4 = "ABCDEFG"
var4[1:5]


# In case no value is specified before or after the colon then the slicing would occur from begining or till end respectively.

# In[8]:


print(var3)


# In[7]:


var3[:7]


# In[9]:


var3[3:]


# In[13]:


print(var3)
var3[2::2]


# To get just one character within a string use the index of that character within the slice operator.

# In[ ]:


var3


# In[14]:


##Exercise 
## write a command that outputs 'HHH' given a string 'HelloHelloHello'
## Solution goes below

print(var3[::5])


# To declare a variable whose value is a long string that spans multiple lines tripple quotes can be used. Conceptually, tripple quotes allows newline and tabs to be incorporated verbatim.

# In[15]:


var4 = """This is an example of
a long string that spans 
three lines."""
print (var4)


# ### String comparison
# One of the frequently required tasks in programming is string comparison. In Python comparison operator can be used to compare two strings. 

# In[16]:


var1 = 'Hello' 
var2 = 'Hello'
var3 = 'Hi'
print(var1 == var2)
print(var1 == var3)


# String comparison is case sensitive.

# In[ ]:


var3 = 'hello'
print(var1 == var3)


# ### String are immutable
# In Python the strings are immutable i.e. their value cannot be changed once it has been assigned. The values can however be reassigned. The variable or label for a string can change but the data contained within the variable can`t be changed

# In[ ]:


var1 = 'Hi'
var2 = var1
var1 = var1*3
print(var1)
print(var2)
var2 = 'Hello'
print(var2)


# In[ ]:





# ### Spliting string
# Sometimes there is a need to split a string based on certain delimiters, the `split` function is designed for that task. Python String types have `split` function associated with them that return a list of elements after spliting the string as per the delimiter (default is space).

# In[17]:


s1 = "This is a sentence."
words1 = s1.split()
print(words1)

s2 = "This is an another sentence, a longer one."
words2 = s2.split(',')
print(words2)


# In[ ]:


##Exercise - what would be the output when "is" is used as delimiter for spliting the above sentence. 


# Python strings have methods `upper` and `lower` to change the case of the string. These methods acts on the string and returns a new string after changing the case.

# In[18]:


s1 = 'apple'
#print(s1)
new_s1 = s1.upper()
print(s1)
print(new_s1)
#s2 = new_s1.lower()
#print(s2)


# In[ ]:


a = (3,4,4)
print(type(a))
b = [2,3,4]
print(type(b))


# In[ ]:


print(not(3>4))


# In[ ]:


print(22.0/7)


# In[ ]:


print((3>4) and (3>5))


# ## User input
# 
# The input functions are different in 2.x and 3.x with former having `raw_input()` while the later has `input()`.

# In[19]:


name = input("Please enter your name: ")
print("The name entered is ", name)


# In[23]:


a = "2"
print(a)
print(type(a))


# In[21]:


number1 = input("Please enter a number: ")
#print(number1+1)
number2 = int(number1)
print(number2+1)


# ### Write a program that takes two numbers as input and prints the result of their comparison

# In[ ]:


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if(num1<num2):
    print("First number is less than the second number")
elif(num1>num2):
    print("First number is greater than the second number")
else:
    print("Both numbers are equal")


# ### Substring in a string
# Slicing can be used to get a substring of a string. To get the index of a substring in a string, `find()` can used. 

# In[ ]:


##find(substr,start,end)
str1 = "What is your name?"
#str1 = "This is a string"
index1 = str1.find("is")
print(index1)


# Get index for all occurence of a substring. Conditionals and loops...
# 

# In[ ]:


i = 0 
str2 = "This is a string"
for x in range(len(str2)):
    ind1 = str2.find("is",i)
    if(ind1==-1):
        continue
    else:
        print(ind1)
        i = ind1+1


# ### Using `re` library

# In[ ]:


import re
str3 = "This is another sring"
all_indicies = re.finditer("is",str3)
##finditer returns match object
for x in all_indicies:
    print(x.start())


# In[ ]:


import numpy
H_all = []
W_all = []
students_data = {"Pooja":(155,55), "Preeti":(160,60), "Smita":(165,65)}
for k1,v1 in students_data.items():
    H_all.append(v1[0])
    W_all.append(v1[1])
print(H_all)
print(W_all)
print (numpy.mean(H_all))
print (numpy.mean(W_all))

sum1=0
for x in H_all:
    sum1 += x
print(sum1/len(H_all))

sum2 = 0
for y in W_all:
    sum2 += y
print(sum2/len(W_all))


# In[ ]:




