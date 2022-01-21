# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 13:42:15 2021

@author: M. Berkan Yıkılmaz
"""
# ask the input "baby bear happy :-)"
text = input('Enter a string: ')

while text != '':
    even_chars=""
    odd_chars=""
    
    for i in range(len(text)):
        if i % 2 == 0:
            even_chars += text[i]
        else:
            odd_chars += text[i]
    
    last_text = even_chars + odd_chars
    print('new string is', last_text)
        
    text = input('Enter a string: ')
    
print('done!')
