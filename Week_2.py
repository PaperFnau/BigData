# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 19:26:44 2017

@author: 
"""
"""
Exercise 2.1
"""

def lists_of_bit_strings(N):
    #Check N is correct type
    if type(N) != int:
        print('N must be an integer')
    elif N < 0:
        print('N must be an integer')
    #Make lists using recursion
    elif N == 0:
        return [''] 
    else:
        return [i + '0' for i in lists_of_bit_strings(N-1)] + \
               [i + '1' for i in lists_of_bit_strings(N-1)]

"""
Exercise 2.2
"""
#Import json soo we can open file
import json
#Import re soo we can remove non letter chars later
import re

#Open the file and load the data into the variable data
with open('pizza-train.json') as data_file:
    data = json.load(data_file)
    
"""
Lets start by making a list of the distinc words in the json file
"""
#Here we will store the words
distinct_words = []
#There are as many 'request_text' as there are entries in 'data'
for i in range(len(data)):
    words = data[i]['request_text']
    #Make the text lowercase
    words = words.lower()
    #Now remove all non letters except spaces and numbers:
    #\W are numbers and the letters 'a-z' the '+ ' is to preserve spaces
    words = re.sub(r'\W+ ', '', words)
    #Split every word into an entry in a list
    words = words.split()
    #Now lets take all the words here not in the distinct_words list and 
    #append them into the list
    #We can add two lists together in order to append them
    #set(a)-set(b) are all the elements in a that are not in b
    distinct_words = distinct_words + list(set(words)-set(distinct_words))
    
"""
Now we have the distinct words we can make the matrix we need,
it'll be len(data) X len(distinct_words). Lets allocate the space
"""
matrix = [[0 for x in range(len(distinct_words))] for y in range(len(data))]

"""
Now we loop over the words lists again, 
this time making the bag of words matrix.
"""
for k in range(len(data)):
    words = data[k]['request_text']
    words = words.lower()
    words = re.sub(r'\W+ ', '', words)
    words = words.split()
    #Find the index of each word in the distinct_words lists
    #add 1 to the bag of words matrix in the correct place
    for word in words:
        j = distinct_words.index(word)
        matrix[k][j] += 1
              

"""
Exercise 2.3
"""
#Set up a dict with the amount of animals
animals = {'cats': 41, 'dogs':32, 'rats':1}
#Someone adopts 3 cats
animals['cats'] -= 3
#A dog has 8 puppies
animals['dogs'] += 8
#You no longer keep rats
del animals['rats']
#Overbview of shelter
print(animals)
        