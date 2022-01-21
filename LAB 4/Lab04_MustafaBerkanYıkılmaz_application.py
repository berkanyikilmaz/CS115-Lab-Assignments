# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 14:49:18 2021

@author: M. Berkan Yıkılmaz
"""
from Lab04_MustafaBerkanYıkılmaz_module import district_density, find_districts

searchcity = input('Enter city to search ("quit" to exit): ')
searchcity_lower = searchcity.lower()

while searchcity.lower() != 'quit':
    search_density = district_density(searchcity_lower, 'city_districts.txt', 'city_values.txt', 'searchcity_density.txt')
    if search_density:
        max_density = float(input('Enter maximum density: '))
        below_density = find_districts(max_density, 'searchcity_density.txt')                                                                      
        if below_density:
            #the reason why i wrote searchcity_lower.capitalize() is that output will be the city name with first letter capitalized even if city is inputted like 'aNkArA'
            print('Districts in', searchcity_lower.capitalize(), 'with population density below', max_density, ":")
            print(below_density, end='')
        else:
            print('No districts in', searchcity, 'with population density below', max_density)
    else:
        print(searchcity_lower.capitalize(), 'not found...')
    
    searchcity = input('Enter city to search ("quit" to exit): ')
    searchcity_lower = searchcity.lower()
        
print('Thank you - Goodbye')