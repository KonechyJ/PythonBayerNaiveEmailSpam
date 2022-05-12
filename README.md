# Naive Bayes Email Spam Detection

## Abstract
This project is an example of using a [Naive Bayes Algorithm](https://en.wikipedia.org/wiki/Naive_Bayes_classifier) to train a program to detect and filter out spam emails.

## Files and Directories
* `data/` - holds the emails files and output data 
* `BuildVocab.py` - builds a list of all the words in the emails that are words.
* `GenerateXYDate.py` - the program to generate the data for the _Naive Bayes Algorithm_ to interpret.
* `naiveBayes.py` - Our main file runs the spam filter with the outputted data.
* `main.py` - TBD.

## How to Run
1. Either [download](https://www.kaggle.com/datasets/balaka18/email-spam-classification-dataset-csv) the test file `emails.csv` in the data folder or similarly create your own.
2. In `BuildVocab.py`, import the proper file and run **./buildVocab** to create/update the vocabulary.txt in the program folder.
3. After `vocabulary.txt` is created, then run **./GenerateXYData**.
    - This can be run after after feeding the _vocabulary.txt_ and spam email file as input onto _GenerateXYData.py_.
4. Two data files, `X.npy` and `Y.npy`, should have been created in the **data/** folder or any predefined destination directory.
5. Finally, you can run the `naiveBayes.py` file using **./naiveBayes.py** and watch the program compute the number of spam emails in the folder.
