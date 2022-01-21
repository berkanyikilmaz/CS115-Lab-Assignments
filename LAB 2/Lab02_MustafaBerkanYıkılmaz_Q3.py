# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 13:57:08 2021

@author: M. Berkan Yıkılmaz
"""
import random

desired_sum = int(input('Desired dice sum: '))
total_rolls = 0 

while desired_sum != 0:
    if desired_sum <= 1 or desired_sum > 12:
            print('Invalid dice sum, try again...')
    else:
        roll = random.randint(2, 12)
        total_rolls += 1
        
        while roll != desired_sum:
            roll = random.randint(2, 12)
            total_rolls += 1
            
        print(total_rolls, 'rolls')
        
    desired_sum = int(input('Desired dice sum: '))
    total_rolls = 0

print('bye!')

        