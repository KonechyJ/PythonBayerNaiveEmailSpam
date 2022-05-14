# Naive Bayes Email Spam Detection

## Abstract
This project uses the [Naive Bayes Algorithm](https://en.wikipedia.org/wiki/Naive_Bayes_classifier) to train a program to detect and filter out spam emails.

## Software Description
- Our program is written in the [Python Programming Language](https://en.wikipedia.org/wiki/Python_(programming_language)).
- Additionally, we used the following libraries in our implementation:
    * [NLTK](https://pypi.org/project/nltk/)
    * [NumPy](https://pypi.org/project/numpy/)
    * [Pandas](https://pypi.org/project/pandas/)
    * [MatPlotLib](https://pypi.org/project/matplotlib/)
    * [Flask](https://pypi.org/project/Flask/)

## Files and Directories
* `LICENSE` - allows other developers to freely use, change, and distribute this software.
* `README.md` - contains all information for knowledge and useability.
* `data/emails.csv` - holds the list of email messages.
* `data/output.ipynb` - jupyter notebook containing the program results.
* `test_data/data.txt` -  test folder and test data used in place of an emails.csv to run the program using text files.
* `test_data/target.txt` -  contains all the target data separated into three classes to classify the emails.
* `vocabulary.txt` - contains all syntactically accurate vocab words in the **.csv** file as an instance of the main procedure.
* `requirements.txt` - contains the necessary python packages to run the program in an environment.
* `BuildVocab.py` - builds a list of all the words in the emails that are words.
* `Flask.py` -  creates a simple server on an empty port to use this app on a local website.
* `GenerateXYDate.py` - the program to generate the data for the _Naive Bayes Algorithm_ to interpret.
* `naiveBayes.py` - the main file to run the spam filter with the outputted data.
* `main.py` - the main file that runs the user interface coordinates all the other file functions in conjunction with the user's commands.

## How to Run
1. Either [download](https://www.kaggle.com/datasets/balaka18/email-spam-classification-dataset-csv) the test file `emails.csv` in the data folder or similarly create your own.
2. Navigate to the `main.py` file in the project folder and type the command **./main.py** to run the whole program as intended. (or whichever command allows you to run the main.py file)

Or alternatively

1. Either [download](https://www.kaggle.com/datasets/balaka18/email-spam-classification-dataset-csv) the test file `emails.csv` in the data folder or similarly create your own.
3. In `BuildVocab.py`, import the proper file and run **./buildVocab** to create/update the vocabulary.txt in the program folder.
4. After `vocabulary.txt` is created, run **./GenerateXYData**.
    - This can be run after feeding the _vocabulary.txt_ and spam email file as input onto _GenerateXYData.py_.
5. Two data files, `X.npy` and `Y.npy`, should have been created in the **data/** folder or any predefined destination directory.
6. Finally, run the `naiveBayes.py` file using **./naiveBayes.py** and watch the program compute the number of spam emails in the folder.


## Group Members
Danny Diep, Jason Duong, Joshua Konechy
