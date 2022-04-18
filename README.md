Naive bayes Email Spam detection.

This project is an example of using a Naive Bayes algortihm to train a program to detect
and filter out spam emails.

The various files in the folder include:

    -data folder: which holds the emails files and outputed data 
    -BuildVocab.py : which builds a list of all the words in the emails that are actually words.
    -GenerateXYDate.py: which is a program to generate the data for the Bayes Algorthim to interpret
    -naiveBayes.py: Essentailly our main file that runs the spam filter with the outputted data.
    -main.py: TBD

To run this Program, first simply either download the test file emails.csv in the data folder or create your own in a simialr fashion.
Website download: https://www.kaggle.com/datasets/balaka18/email-spam-classification-dataset-csv

Then, in buildVocab, import the proper file and run buildVocab which will create or update a vocabulary.txt in the program folder.

After vocabulary.txt is create, then run GeneratXYData. After inputting the proper vocabulary.txt location and spam email file on GenerateXYDate, the can be run.
After it is completed, two data files X.npy and Y.npy should be created in the Data folder or which ever location you have set to create to.

Finally, you can run the naiveBayes file and watch the program determine the amount of spam emails in the folder.
