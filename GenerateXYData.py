#!/usr/bin/env python3

import pandas as PD
import numpy as NP
import ast

data = PD.read_csv("data/emails.csv")
file = open("vocabulary.txt", 'r')
content = file.read()
vocabulary = ast.literal_eval(content)

X = NP.zeros((data.shape[0], len(vocabulary)))
Y = NP.zeros((data.shape[0]))

for i in range(data.shape[0]):
    email = data.iloc[i, :][0].split()

    for email_word in email:
        if email_word.lower() in vocabulary:
            X[i, vocabulary[email_word]] += 1
            Y[i] = data.iloc[i, 1]

NP.save('data/X.npy', X)
NP.save('data/Y.npy', Y)
