#!/usr/bin/env python
# coding: utf-8

# In[6]:


x = float(input('Enter x: '))
y = float(input('Enter y: '))
z = float(input('Enter z: '))

calc = (x + y * z) * (x * y + z) / (x * y * z)

print(f'f({x}, {y}, {z}) = {calc:.2f}')


# In[ ]:




