# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 13:31:12 2021

@author: M. Berkan Yıkılmaz
"""

def district_density(city, f1, f2, filename):
    """
    
    Parameters
    ----------
    city (string): City name
    f1 (file): file containing the city and district names
    f2 (file): file containing the population and area data for the districts in the cities
    filename (string): name of the file to store the results

    Returns
    -------
    boolean: True for city is in f1, False for city is not in f1

    """
    
    city_districts = open(f1, 'r')
    city_values = open(f2, 'r')
    district_den = open(filename, 'w')

    for districts in city_districts:
        pos = districts.lower().find(city)
        line2 = city_values.readline()
        if pos == 0:
            pos1 = districts.find('	')
            district_name = districts[pos1 + 1: len(districts)].strip()
            
            pos2 = line2.find("	")
            
            pop = line2[:pos2]
            comma = pop.find(',')
            if comma != -1:
                pop = pop[0:comma] + pop[comma+1:len(pop)]
            
            area = line2[pos2 + 1:len(line2)].strip()
            comma2 = area.find(',')
            if comma2 != -1:
                area = area[0:comma2] + '.' +area[comma2 + 1:len(area)]

            pop_density = float(pop) / float(area)
            district_den.write(district_name + ',' + f'{pop_density:.1f}' + '\n')
            
    city_districts.close()
    city_values.close()
    district_den.close()

    #checks whether or not city inputted is in the f1 file
    city_districts = open(f1, 'r')
    read1 = city_districts.read()
    is_inside = read1.lower().find(city)
    if is_inside == -1:
        city_districts.close()
        return False
    else:
        city_districts.close()
        return True


def find_districts(max_density, file_name):
    """

    Parameters
    ----------
    max_density (float): Population Density
    file_name (string): File Name 

    Returns
    -------
    string

    """
    
    file = open(file_name, 'r')
    new_string = ''

    for line in file:
        pos = line.find(',')
        district = line[0:pos] 
        density = line[pos+1:len(line)]
        if max_density > float(density):
            new_string += district + '\n'

    file.close()
            
    return new_string