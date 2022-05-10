# Naive Bayes Email Spam Detection

## Abstract
This project is an example of using a [Naive Bayes algortihm](https://en.wikipedia.org/wiki/Naive_Bayes_classifier) to train a program to detect and filter out spam emails.

## Files and Directories
* `data/`: which holds the emails files and outputed data 
* `BuildVocab.py`: which builds a list of all the words in the emails that are actually words.
* `GenerateXYDate.py`: which is a program to generate the data for the Bayes Algorthim to interpret.
* `naiveBayes.py`: Essentailly our main file that runs the spam filter with the outputted data.
* `main.py`: TBD.

## How to Run
1. Simply either [download](https://www.kaggle.com/datasets/balaka18/email-spam-classification-dataset-csv) the test file `emails.csv` in the data folder or create your own in a similar fashion.
2. In `BuildVocab.py`, import the proper file and run **./buildVocab** to create/update the vocabulary.txt in the program folder.
3. After vocabulary.txt is create, then run GeneratXYData. After inputting the proper vocabulary.txt location and spam email file on GenerateXYDate, the can be run.
4. Two data files `X.npy` and `Y.npy` should have been created in the **data/** folder or any predefined destination directory.
5. Finally, you can run the `naiveBayes.py` file using **./naiveBayes.py** and watch the program compute the amount of spam emails in the folder.
