
## **Welcome to the first mini-project!** 

Here's what to expect:

* you'll download the project starter files (one time only)
* you'll run a startup script
* near the end of each lesson, there will be a video and/or reading node telling you about the mini-project for that lesson
* then, a series of reading nodes at the end of the lesson will walk you through what you should do for that mini-project, and give you a chance to enter the answers that you get as you work through the tasks (these will look like quizzes)
* you'll develop the code on your own computer based on the instructions in the reading nodes
* the code you write will enable you to answer the quiz questions

So, what now?
* if you know git, you can clone the starter files: git clone https://github.com/udacity/ud120-projects.git
* If you don't know git, Udacity has a great (and short) course that can get you started

A couple of years ago, J.K. Rowling (of Harry Potter fame) tried something interesting. She wrote a book, “The Cuckoo’s Calling,” under the name Robert Galbraith. The book received some good reviews, but no one paid much attention to it--until an anonymous tipster on Twitter said it was J.K. Rowling. The London Sunday Times enlisted two experts to compare the linguistic patterns of “Cuckoo” to Rowling’s “The Casual Vacancy,” as well as to books by several other authors. After the results of their analysis pointed strongly toward Rowling as the author, the Times directly asked the publisher if they were the same person, and the publisher confirmed. The book exploded in popularity overnight.

We’ll do something very similar in this project. We have a set of emails, half of which were written by one person and the other half by another person at the same company . Our objective is to classify the emails as written by one person or the other based only on the text of the email. We will start with Naive Bayes in this mini-project, and then expand in later projects to other algorithms.

We will start by giving you a list of strings. Each string is the text of an email, which has undergone some basic preprocessing; we will then provide the code to split the dataset into training and testing sets. (In the next lessons you’ll learn how to do this preprocessing and splitting yourself, but for now we’ll give the code to you).

One particular feature of Naive Bayes is that it’s a good algorithm for working with text classification. When dealing with text, it’s very common to treat each unique word as a feature, and since the typical person’s vocabulary is many thousands of words, this makes for a large number of features. The relative simplicity of the algorithm and the independent features assumption of Naive Bayes make it a strong performer for classifying texts. In this mini-project, you will download and install sklearn on your computer and use Naive Bayes to classify emails by author.

* Check that you have a working python installation, preferably version 2.6 or 2.7 (that’s the version that we use--other versions may work, but we can’t guarantee it) We will use pip to install some packages. First get and install pip from here.
* Using pip, install a bunch of python packages:
* go to your terminal line (don’t open python, just the command prompt)
* install sklearn: **pip install scikit-learn**
* for your reference, here’s the sklearn installation instructions
* install natural language toolkit: **pip install nltk**
* Get the Intro to Machine Learning source code. You will need git to clone the repository: **git clone https://github.com/udacity/ud120-projects.git**

You only have to do this once, the code base contains the starter code for all the mini-projects. Go into the tools/ directory, and run startup.py. It will first check for the python modules, then download and unzip a large dataset that we will use heavily later. The download/unzipping can take a while, but you don’t have to wait for it to finish in order to get started on Part 1.

Create and train a Naive Bayes classifier in naive_bayes/nb_author_id.py. Use it to make predictions for the test set. What is the accuracy?

When training you may see the following error: UserWarning: Duplicate scores. Result may depend on feature ordering.There are probably duplicate features, or you used a classification score for a regression task. warn("Duplicate scores. Result may depend on feature ordering.")

This is a warning that two or more words happen to have the same usage patterns in the emails--as far as the algorithm is concerned, this means that two features are the same. Some algorithms will actually break (mathematically won’t work) or give multiple different answers (depending on feature ordering) when there are duplicate features and sklearn is giving us a warning. Good information, but not something we have to worry about.

Quiz: Author ID Accuracy
Some students have encountered memory problems when executing the code for this problem. To reduce the chance of seeing a memory error while running the code, we recommend that you use a computer with at least 2GB of RAM. If you find that the code is causing memory errors, you can also try setting test_size = 0.5 in the email_preprocess.py file.


```python
#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
import os
from time import time
os.chdir("${HOME}/Udacity/Intro_Machine_Learning/ud120-projects/naive_bayes")
sys.path.append("../tools/")
from email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

### your code goes here ###
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()

t0 = time()
clf.fit ( features_train, labels_train )
print "training time:", round ( time() - t0, 3 ), "s"

pred = clf.predict ( features_test )
from sklearn.metrics import accuracy_score
print "Accuracy Score = ", accuracy_score ( pred, labels_test )
```

    no. of Chris training emails: 7936
    no. of Sara training emails: 7884
    training time: 0.763 s
    Accuracy Score =  0.973265073948


An important topic that we didn’t explicitly talk about is the time to train and test our algorithms. Put in two lines of code, above and below the line fitting your classifier, like this:

`t0 = time()
< your clf.fit() line of code >
print "training time:", round(time()-t0, 3), "s"`

Put similar lines of code around the clf.predict() line of code, so you can compare the time to train the classifier and to make predictions with it. What is faster, training or prediction?

We will compare the Naive Bayes timing to a couple other algorithms, so note down the speed and accuracy you get and we’ll revisit this in the next mini-project.

Hopefully it’s becoming clearer what Sebastian meant when he said Naive Bayes is great for text--it’s faster and generally gives better performance than an SVM for this particular problem. Of course, there are plenty of other problems where an SVM might work better. Knowing which one to try when you’re tackling a problem for the first time is part of the art and science of machine learning. In addition to picking your algorithm, depending on which one you try, there are parameter tunes to worry about as well, and the possibility of overfitting (especially if you don’t have lots of training data).

Our general suggestion is to try a few different algorithms for each problem. Tuning the parameters can be a lot of work, but just sit tight for now--toward the end of the class we will introduce you to GridCV, a great sklearn tool that can find an optimal parameter tune almost automatically.

Hopefully it’s becoming clearer what Sebastian meant when he said Naive Bayes is great for text--it’s faster and generally gives better performance than an SVM for this particular problem. Of course, there are plenty of other problems where an SVM might work better. Knowing which one to try when you’re tackling a problem for the first time is part of the art and science of machine learning. In addition to picking your algorithm, depending on which one you try, there are parameter tunes to worry about as well, and the possibility of overfitting (especially if you don’t have lots of training data).

Our general suggestion is to try a few different algorithms for each problem. Tuning the parameters can be a lot of work, but just sit tight for now--toward the end of the class we will introduce you to GridCV, a great sklearn tool that can find an optimal parameter tune almost automatically.
