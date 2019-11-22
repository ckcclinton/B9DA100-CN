# -*- coding: utf-8 -*-
# glob.glob
# to begin we start with a list of words in a file called spell.words
# we read the file and strip out the file endings

import os
for file in os.listdir("C:/Users/clintonngan/.spyder-py3"):
    if file.endswith(".txt"):
        print(os.path.join("C:/Users/clintonngan/.spyder-py3", file))
        
def load_files(file_names):
    lines = 
        

def load_file(file_name):
    # assign a variable called words
    words = open(file_name).readlines()
    return list(map(lambda x: x.strip(), words))

def check_word(words, word):
    return word in words

def check_words(words, sentence):
    words_to_check = sentence.split(' ')
    for word in words_to_check:
        if not check_word(words, word):
            print('Word is misspelt : ' + word)
            return False
    return True

# Ignore above, redundant
# Any time you use class, always have first letter as capital 
# in every starting word, you need to add "self" to all variables under
# this class

class SpellChecker(object):
    def __init__(self):
        self.words = []

# returning a list full of words lower case, strips
    def load_file(self, file_name):
        lines = open(file_name).readlines()
        return list(map(lambda x: x.strip().lower(), lines))
    
# putting output of above function into self.words
    def load_words(self, file_name):
        self.words = self.load_file(file_name)

# check for "fuck","shit" and ignore them, then return rest
    def check_profanities(self, word):
        return word not in ['fuck', 'shit']

# stripping all symbols plus lower case
    def check_word(self, word):
        return word.lower().strip('.,?\"') in self.words

    def check_words(self, sentence, index=0):
        failed_words = []
        words_to_check = sentence.split(' ')
        caret_position = 0
        
        # loop thru words 1 by 1 
        for word in words_to_check:
            # Call the check_word func and check against dict
            # If check fails, store dict into list
            if not self.check_word(word):
                failed_words.append(
                    {'word':word, 'line':index+1,
                        'pos':caret_position+1, 'type': 'spelling'})
            # same shit as above but checking for profanity now
            if not self.check_profanities(word):
                failed_words.append(
                    {'word':word, 'line':index+1,
                        'pos':caret_position+1, 'type': 'profanity'})
            caret_position += len(word) + 1
        # return list of dictionary
        return failed_words

    def check_document(self, file_name):
        # empty list created to store failed words in sentences
        failed_words_in_sentences = []
        self.sentences = self.load_file(file_name)
        for index, sentence in enumerate(self.sentences):
            failed_words_in_sentences.extend(
                self.check_words(sentence, index))
        return failed_words_in_sentences

# code now runs here
if __name__ == '__main__':
 
    words = load_file('spell.words')
    # now check if the word zygotic is a word
    print(check_word(words, 'zygotic'))
    print(check_word(words, 'mistasdas'))
    print(check_words(words, 'zygotic mistasdas elementary'))
    
    spell_checker = SpellChecker()
    spell_checker.load_words('spell.words')
    # now check if the word zygotic is a word
    print(spell_checker.check_word('zygotic'))
    print(spell_checker.check_word('mistasdas'))
    print(spell_checker.check_words('zygotic mistasdas elementary'))
