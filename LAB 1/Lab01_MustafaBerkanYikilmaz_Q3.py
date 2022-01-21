#!/usr/bin/env python
# coding: utf-8

# In[35]:


first_name = input("Enter first name: ")
second_name = input("Enter second name: ")
third_name = input("Enter third name: ")

longest = first_name
tie = 0

if len(second_name) > len(longest):
    longest = second_name
elif len(second_name) == len(longest):
    tie = 1
    
if len(third_name) > len(longest):
    longest = third_name
    tie = 0 #tie situation is no longer exist.
elif len(third_name) == len(longest):
    tie = 1
    
if tie == 0:
    print(longest, "'s name is longest")
else: 
    print(longest, "'s name is the longest, but there is a tie!")


# In[ ]:





# In[ ]:




