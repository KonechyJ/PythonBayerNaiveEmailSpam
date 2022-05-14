import BuildVocab
import GenerateXYData
import naiveBayes
import os.path
import time
import contextlib
from matplotlib import pyplot as plt
import numpy as NP

if __name__ == '__main__':
    print("Hello and Welcome to the Email Spam Detection Program.")
    print("Here, we can check how much of your emails are spam.")
    yourAnswer = input("Would you like to run the program? y/n: ")

    while yourAnswer == "y":
        print("First we need to build a vocab file. This is a list of all the English words found in the emails.csv")
        if os.path.exists("vocabulary.txt"):
            print("Since the file is exist in your folder, you don't need to run it")
        else:
            with contextlib.redirect_stdout(None):
                exec(open("BuildVocab.py").read())

        print("Now we will generate the X and Y Data")

        time.sleep(5)
        if os.path.exists("data/X.npy") and os.path.exists("data/Y.npy"):
            print("The file already exist!")
        else:
            print("Since there is no data, we will need to create it.")
            print("This process will take sometime...")
            exec(open("GenerateXYData.py").read())

        yourSecondAnswer = input("Would you like to See the date in graph form? y/n: ")
        if yourSecondAnswer == 'y':
            XPlot = NP.load('data/X.npy')
            plt.imshow(XPlot, cmap='gray')
            plt.show()
        else:
            print("Okay, moving on then.")
        time.sleep(5)
        print(".")
        print("..")
        print("...")
        print("Now we will Interpret the X and Y Data using Bayes Naive")
        exec(open("naiveBayes.py").read())
        yourAnswer = input("Would you like to run the program again? y/n: ")