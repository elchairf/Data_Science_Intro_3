# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 20:27:46 2022

@author: Elchai Refoua
"""


import os
# Task 1



def read_line(n=None, file=None):
    try:
        n = int(n)
    except:
        print("invalid input detected")
        return
    try:
        f = open(file,"r")
    except:
        print("file not found")
        return
    count =0
    for index,line in enumerate (f):
        count += 1
        if index ==n-1:
            print(line.rstrip())
    if count <=n:
        str(n)
        print("line",n,"doesn't exist")


#read_line(4, ex3_text.txt) 
#should return: " There is much more to black holes than meets the eye. In fact,".
#read_line(9, ex3_text.txt) 
#should return: " ".
#read_line(29, ex3_text.txt) 
#should return: "line 29 doesn't exist". 
#read_line("c", ex3_text.txt) 
#should return: "invalid input detected".
#read_line(9, ex4_text.txt) 
#should return: "file not found".





# Task 2


def longest_words(file=None):
    try:
        f = open(file,"r")
    except:
        print("file not found")
        return
    biggest_words = ["","","","",""]
    for line in f:
        sentense = line.split()
        for word in sentense:
            biggest_words = top_five(word,biggest_words)
    print(biggest_words)
def top_five(word,list):
    for index,w in enumerate(list):
        if len(w)<len(word):
            list.insert(index,word)
            list.pop(5)
            return list
    return list

# print(longest_words("ex4_text.txt"))
#longest_words('ex3_text.txt')
#longest_words(ex4_text.txt) 





















