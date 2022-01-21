# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 13:43:26 2021

@author: M. Berkan Yıkılmaz
"""

def load_movies(pointer):
    movies = {}
    file = open(pointer, 'r')
    for line in file:
        splitted_line = line.split(',')
        if not int(splitted_line[0]) in movies.keys():
            movies[int(splitted_line[0])] = [splitted_line[1].strip()]
        else:
            movies[int(splitted_line[0])].append(splitted_line[1].strip())
    file.close()
    return movies


def get_movies_by_year(movies, year):
    if year in movies.keys():
        return movies[year]
    else:
        return []
    

def get_movies_by_keywords(movies, keyword):
    movie_list = []
    for key in movies.keys():
        for value in movies[key]:
            if value.find(keyword) != -1:
                movie_list.append((key, value))
    return movie_list
            

def print_list(l):
    for element in l:
        print(element)




