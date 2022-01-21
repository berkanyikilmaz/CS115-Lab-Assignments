# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 13:31:13 2021

@author: M. Berkan Yıkılmaz
"""

from Country import Country

l = []

def selectionSort(l):
    start = 0
    while start != len(l):
        for i in range(start, len(l)):
            if l[i].getContinent() < l[start].getContinent():
                l[start], l[i] = l[i], l[start]
            elif l[i].getContinent() == l[start].getContinent():
                if l[i].getCountry() < l[start].getCountry():
                    l[start], l[i] = l[i], l[start]
        start += 1
        
                
def searchCountries(l, continent, index):
    if index == 1:
        if l[index - 1].getContinent() == continent:
            return [l[index - 1]]
        else:
            return []
    else:
        prev = searchCountries(l, continent, index - 1)
        if l[index - 1].getContinent() == continent:
            return prev + [l[index - 1]]
        else:
            return prev
            

def readCountries(l, fileName):
    fileHandle = open(fileName, 'r')
    for line in fileHandle:
        splitted = line.split(',')
        country = Country(splitted[0],splitted[1],splitted[2],splitted[3])
        l.append(country)
    fileHandle.close()
    

readCountries(l, 'country.txt')

continent = input("Enter continent to search: ")

new_list = searchCountries(l, continent, len(l))

if new_list != []:
    for i in range(len(new_list)):
        print(new_list[i])
else:
    print("No country is found.")
    
cName = input("Enter country name: ")
Cont = input("Enter continent name: ")
lifeexpM = input("Enter life expectancy for men: ")
lifeexpF = input("Enter life expectancy for women: ")
compare = Country(cName, Cont, lifeexpM, lifeexpF)

is_exist = False
for i in range(len(l)):
    if l[i] == compare:
        is_exist = True
        
if not is_exist:
    l.append(compare)
    print("New Country added\n")
    
print("Countries by Continent and Name: ")
    
selectionSort(l)

print(l)





    
    
    