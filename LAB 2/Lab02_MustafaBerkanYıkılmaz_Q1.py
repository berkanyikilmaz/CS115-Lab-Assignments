# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 13:32:19 2021

@author: M. Berkan Yıkılmaz
"""

num = int(input('Enter an int: '))
print(f'Factors of {num}:')
for i in range(1,num):
    if num % i == 0:
        print(i,",", end=' ')
print(num)



