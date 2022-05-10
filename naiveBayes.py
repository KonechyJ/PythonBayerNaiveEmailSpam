#!/usr/bin/env python3

import numpy as NP

class naiveBayes():
    def __init__(self, x, y):
        self.num_examples, self.num_features = x.shape
        self.num_classes = len(NP.unique(y)) # finds unique numbers and gives the length
        self.eps = 1e-6

    def fit(self, x, y):
        self.classes_mean = {}
        self.classes_variance = {}
        self.classes_prior = {}

        for i in range(self.num_classes): # iterate through all the classes
            x_i = x[y==i]

            self.classes_mean[str(i)] = NP.mean(x_i, axis=0)
            self.classes_variance[str(i)] = NP.var(x_i, axis=0)
            self.classes_prior[str(i)] = x_i.shape[0]/self.num_examples


    def predict(self, x):
        probs = NP.zeros((self.num_examples, self.num_classes))
        for j in range(self.num_classes):
            prior = self.classes_prior[str(j)]
            probs_j = self.density_func(x, self.classes_mean[str(j)], self.classes_variance[str(j)])
            probs[:, j] = probs_j + NP.log(prior)
        return NP.argmax(probs, 1)


    def density_func(self,x, mean, sigma):
        #cal the prob using gaussian
        constant = -self.num_features/2 * NP.log(2 * NP.pi) - 0.5 * NP.sum(NP.log(sigma+self.eps))
        probability = 0.5 * NP.sum(NP.power(x - mean, 2)/(sigma + self.eps), 1)
        return constant - probability


if __name__ == '__main__':
    # X = NP.loadtxt('test_data/data.txt', delimiter=',')
    # Y = NP.loadtxt('test_data/targets.txt')-1


    X = NP.load("data/X.npy")
    Y = NP.load("data/Y.npy")
    print("Here lets print the basic data that is present from the x.npy and y.npy files.")
    print("First from X.shape we have ~ 5728 training examples or points and ~12,000 features")
    print(X.shape)
    print("First from Y.shape we have ~ 5728 training points ")
    print(Y.shape)
    print("The percent of accuracy in detecting spam emails is: ")
    NB = naiveBayes(X, Y)
    NB.fit(X, Y) #training the program
    y_Predict = NB.predict(X) # predicting the outcomes

    print(sum(y_Predict == Y)/X.shape[0])
    print("The percent of spam emails in this file is: ")
    print(sum(Y)/Y.shape[0])

    print("preview an email: ")
    print(y_Predict)
    #print(data.iloc[2,0])
