# Naive Bayes Email Spam Detection

## Abstract
This project uses the [Naive Bayes Algorithm](https://en.wikipedia.org/wiki/Naive_Bayes_classifier) to train a program to detect and filter out spam emails.

## Software Description
- Our program is written in the [Python Programming Language](https://en.wikipedia.org/wiki/Python_(programming_language).
- Additionally, we used the the following libraries:
    * [NLTK](https://pypi.org/project/nltk/)
    * [NumPy](https://pypi.org/project/numpy/)
    * [Pandas](https://pypi.org/project/pandas/)
    * [MatPlotLib](https://pypi.org/project/matplotlib/)
    * [Flask](https://pypi.org/project/Flask/)
---
- Describe the components of the software.
- Include Diagram illustrating the components and the input/output relationship between them.

## Files and Directories
* `LICENSE` - allows other developers to freely use, change, and distribute this software.
* `README.md` - contains all information for knowledge and useability.
* `data/emails.csv` - holds the list of emails messages.
* `data/output.ipynb` - jupyter notebook containing the results of the program.
* `test_data/data.txt` - TODO
* `test_data/target.txt` - TODO
* `vocabulary.txt` - TODO
* `requirements.txt` - contains the necessary python packages to run the program an environment.
* `BuildVocab.py` - builds a list of all the words in the emails that are words.
* `Flask.py` -  TODO
* `GenerateXYDate.py` - the program to generate the data for the _Naive Bayes Algorithm_ to interpret.
* `naiveBayes.py` - our main file runs the spam filter with the outputted data.
* `main.py` - TODO

## How to Run
1. Either [download](https://www.kaggle.com/datasets/balaka18/email-spam-classification-dataset-csv) the test file `emails.csv` in the data folder or similarly create your own.
2. In `BuildVocab.py`, import the proper file and run **./buildVocab** to create/update the vocabulary.txt in the program folder.
3. After `vocabulary.txt` is created, then run **./GenerateXYData**.
    - This can be run after after feeding the _vocabulary.txt_ and spam email file as input onto _GenerateXYData.py_.
4. Two data files, `X.npy` and `Y.npy`, should have been created in the **data/** folder or any predefined destination directory.
5. Finally, you can run the `naiveBayes.py` file using **./naiveBayes.py** and watch the program compute the number of spam emails in the folder.
