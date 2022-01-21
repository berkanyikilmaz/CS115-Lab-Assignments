#!/usr/bin/env python
# coding: utf-8

# In[5]:





# In[6]:





# In[7]:


first = int(input('Enter first integer: '))
second = int(input('Enter second integer: '))
third = int(input('Enter third integer: '))

sum = 0
evenmax = 0 #to make sure that it is smaller than the input values

if (first % 2 != 0) and (second % 2 != 0 ) and (third % 2 != 0):
    print("No even integer is entered")
else:
    if first % 2 == 0:
        sum += first
        if first > evenmax:
            evenmax = first
    if second % 2 == 0:
        sum += second
        if second > evenmax:
            evenmax = second
    if third % 2 == 0:
        sum += third
        if third > evenmax:
            evenmax = third
        
    print("sum of evens is", sum)
    print("even max is", evenmax)


# In[ ]:





# In[ ]:




