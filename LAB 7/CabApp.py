# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 13:55:06 2021

@author: M. Berkan Yıkılmaz
"""
from Cab import Cab, Sedan, Hatchback

def find_greater(CabList, cab):
    """
    Parameters
    ----------
    CabList (list): List of the all cabs
    cab (object): Cab object which will be compared with the objects in the list

    Returns
    -------
    num (int): number of cabs in the list with the same type as cab and whose number of 
    kilometers is more than the kilometers of the cab
    """
    num = 0
    for c in CabList:
        if c > cab:
            num += 1
    return num

def read_line(filename):
    """
    Parameters
    ----------
    filename (str): Name of the file that will be read.

    Returns
    -------
    cabList (list): list which contains sedan and hatchback class objects

    """
    cabList = []
    fileHandle = open(filename, 'r')
    for i in fileHandle:
        line = i.split(';')
        if line[0] == 'Sedan':
            cabList.append(Sedan(line[0], int(line[1]), int(line[2])))
        if line[0] == 'Hatchback':
            cabList.append(Hatchback(line[0], int(line[1]), int(line[2])))
    return cabList
            
cablist = read_line('cabs.txt')

sedan = 1
for cab in cablist:
    if cab.get_type() == 'Sedan':
        print(cab, str(sedan), 'will pay', cab.calculate_fare(), 'TL')
        sedan += 1

print()
print('There are', find_greater(cablist, Cab('Sedan', 0, 2015)), 'Sedan cars newer than 2015\n')

kms = 0
compare = Cab('Hatchback', 0, 2020)
for cab in cablist:
    if cab == compare:
        kms += cab.get_kms()
        
print('All Hatchback cars of year 2020 have travelled', kms, 'kms')
    



    


        
    