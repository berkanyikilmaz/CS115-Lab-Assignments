# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 14:07:58 2021

@author: M. Berkan Yıkılmaz
"""

from Lab5_MustafaBerkanYıkılmaz_Functions import load_movies, get_movies_by_keywords, get_movies_by_year, print_list

movie_dictionary = load_movies('movie_data.csv')

year = int(input('Enter year to search: '))
result = get_movies_by_year(movie_dictionary, year)
if result:
    print('Movies made in ' + str(year) + ":")
    print_list(result)
else:
    print('No movies from ' + str(year) + ' found')

keyword = input('Enter keyword to search: ')
result2 = get_movies_by_keywords(movie_dictionary, keyword)
if result2:
    print_list(result2)
else:
    print('No movies with the keyword "' + keyword + '" found')
