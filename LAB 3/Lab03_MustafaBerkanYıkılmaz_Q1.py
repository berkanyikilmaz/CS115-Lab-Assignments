# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 13:32:25 2021

@author: M. Berkan Yıkılmaz
"""
def is_neat_reversible(s):
    """
    Finds whether or not the string is 'neat reversible'. If a string is the same as the original string
    after moving its first character to the end and reversing it, it is neat reversible.
    
    Parameters
    ----------
    s (string): string which will be checked if it is neat reversible or not

    Returns
    -------
    bool: True if string is neat reversible
          False if string is not neat reversible

    """
    if s == '':
        return False
    else: 
        empty = ''
        
        empty += s[0]
        
        for i in s[:-len(s):-1]:
            empty += i
        
        if s == empty:
            return True
        else:
            return False
        
def uppercase_word_at(s, index):
    """
    Returns a string which is identical to the string given except the letters in string starting
    from the index that is inputted up to the first space.

    Parameters
    ----------
    s (string): String that some of the letters starting from index will be capitalized until the first space.
    index : The index that the letters starting from this index will be capitalized until the first space

    Returns
    -------
    string: return new_string: A new string whose letters starting from index until 
    the first space are capitalized

    """
    new_string = ""
    space_index = 0
    
    new_string += s[:index]
    
    for i in range(index, len(s)): #if index starts from space?
        if s[i] == ' ':
            space_index = i
            break
        else:
            new_string += s[i].upper() #can i use this method

    if space_index != 0:
        new_string += s[space_index: len(s)]
    
    return new_string


def capitalize_neat_reversibles(s):
    """
    Capitalizes all the neat revesible words in the string.

    Parameters
    ----------
    s (string): String that all of the neat reversible words will be capitalized.

    Returns
    -------
    string: return new_string: A new string whose neat reversible words are capitalized

    """
    index = 0
    new_string = ''
    
    for i in range(len(s)):
        if s[i] == ' ':
            if is_neat_reversible(s[index: i]):
                new_string += uppercase_word_at(s[index: i + 1], 0)
            else:
                new_string += s[index: i + 1]
            index = i + 1
    
    if is_neat_reversible(s[index: len(s)]):
        new_string += uppercase_word_at(s[index: len(s)], 0)
    else:
        new_string += s[index: len(s)]
        
    return new_string

s = input('Enter a sentence: ')

while s:
    print('neat reversibles capitalized:')
    print(capitalize_neat_reversibles(s))
    
    s = input('Enter a sentence: ')
    
print('bye!')
            



     