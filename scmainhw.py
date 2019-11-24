# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 14:48:23 2019

@author: clintonngan
"""


import os
from spellchecker import SpellChecker
sc = SpellChecker()

def dir_files(directory):
    file_names = []
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            file_names.append(file)
    
    return file_names

def load_dir_files(file_names):
    lines_dir = open(file_names).readlines()
    return list(map(lambda x: x.strip().lower(), lines_dir))

file_names = dir_files("C:/Users/clintonngan/.spyder-py3")

# contents = load_dir_files(file_names)
for item in file_names:
    contents = load_dir_files(item)
    for index, line in enumerate(contents):
        # print(f"Line {index}: {line} {item}")
        # print()
        print('index {0}, Line: {1}, File Name: {2}'.format(index, line, item))
    print()
    
#print(load_dir_files(file_names[0]), "\n")
    

    sc.load_words('spell.words')
    for index, line in enumerate(contents):
        word_list = sc.check_words(line, index)
        if(len(word_list) != 0):
            print(word_list)