# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 13:25:51 2021

@author: M. Berkan Yıkılmaz
"""
twod_list = [['This', 'is', 'lab', 'Script'], ['We', 'should', 'finish', 'it'], ['we', 'solve', 'some', 'questions']]

def formSentence(inList, searchChr):
    """

    Parameters
    ----------
    inList (list): two dimensional list that contains words
    searchChr (str): this will be used to check whether or not the words in inList starts with this character.
        
    Returns
    -------
    sentence (str): Sentence which is created with the words in inList starting with searchChr

    """
    sentence = ''
    word_list = []
    for i in inList:
        for j in i:
            if j[0].lower() == searchChr.lower():
                word_list.append(j)
                
    if word_list:
        for i in range(len(word_list) - 1):
            sentence += word_list[i] + ' '
        sentence += word_list[-1]
        
    return sentence

sentence = formSentence(twod_list, 's')
print('Two Dimensional List:')
for row in twod_list:
    print(row)
print('Sentence: ' + sentence)
            