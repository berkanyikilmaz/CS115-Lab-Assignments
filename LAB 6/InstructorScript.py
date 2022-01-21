# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 15:04:58 2021

@author: M. Berkan Yıkılmaz
"""
from Instructor import Instructor

def read_file(filename):
    """
    
    Parameters
    ----------
    filename (str): Name of the file that will be read.

    Returns
    -------
    new_dict (dict): dictionary which takes id as key and instructor object as value

    """
    new_dict = {}
    fileHandle = open(filename, 'r')
    for i in fileHandle:
        line = i.split(';')
        new_dict[int(line[0])] = Instructor(int(line[0]), line[1], line[2], int(line[3]))
    fileHandle.close()
    return new_dict

d = read_file('instructor.txt')

idinput = int(input('Enter instructor id: '))
print(d[idinput])

status = input('Enter status (F - Full-time / P - Part-time): ')
inst_list = []
for key in d.keys():
    if d[key].get_status().lower() == status.lower():
        inst_list.append(d[key])
if status.lower() == 'p':
    print('Part-time Instructors:')
else:
    print('Full-time Instructors:')
print(inst_list)
    
