import BuildVocab
import GenerateXYData
import naiveBayes
import os.path 
import time
import contextlib

if __name__ == '__main__':
    print("Hello, first we need to build a vocab file.")
    if(os.path.exists("vocabulary.txt")):
        print("Since the file is exist in your folder, you don't need to run it")
    else:
        with contextlib.redirect_stdout(None):
            exec(open("BuildVocab.py").read())

    time.sleep(5)
    if(os.path.exists("data/X.npy") and os.path.exists("data/Y.npy")):
        print("The file already exist!")
    else:
        print("Now we will generate the X and Y Data")
        print("This process will take sometime...")
        exec(open("GenerateXYData.py").read())

    time.sleep(5)
    print("Now we will generate the X and Y Data using Baye Naive")
    exec(open("naiveBayes.py").read())
