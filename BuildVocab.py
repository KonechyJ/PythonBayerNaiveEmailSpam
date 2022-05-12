#!/usr/bin/env python3

import pandas as PD
import nltk
from nltk.corpus import words

vocabulary = {}
data = PD.read_csv("data/emails.csv")
nltk.download('words')
set_words = set(words.words())

def build_vocab(current_email):
    index = len(vocabulary)

    for word in current_email:
        if word.lower() not in vocabulary and word.lower() in set_words:
            vocabulary[word] = index
            index += 1

if __name__ == '__main__':
    for i in range(data.shape[0]):
        current_email = data.iloc[i, :][0].split()
        print(f'Currennt email is {i}/{data.shape[0]} and the /length of the vocab in {len(vocabulary)}')

        build_vocab(current_email)

    file = open("vocabulary.txt", "w")
    file.write(str(vocabulary))
    file.close()