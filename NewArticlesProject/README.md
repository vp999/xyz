### Project Overview

 Problem Statement
You are given references to news pages collected from an web aggregator in the period from 10-March-2014 to 10-August-2014. The resources are grouped into categories that represent pages discussing the same story. News categories included in this dataset include business(b); science and technology(t); entertainment(e); and health(h).

The goal is to predict which class a particular resource belongs to given the title of the resource.

About the dataset
This dataset comes from the UCI Machine Learning Repository. In total there are 422937 resources available in the dataset. The columns included in this dataset are:

ID: the numeric ID of the article
TITLE: the headline of the article
URL: the URL of the article
PUBLISHER: the publisher of the article
CATEGORY: the category of the news item; one of: b:business, t:science and technology, e: entertainment and m:health
STORY: alphanumeric ID of the news story that the article discusses
HOSTNAME: hostname where the article was posted
TIMESTAMP: approximate timestamp of the article's publication, given in Unix time (seconds since midnight on Jan 1, 1970)
Why solve it
Solving it will reinforce the following concepts of text analytics:



### Learnings from the project

 
Preprocess text data with tokenization, stopword removal etc
Vectorize data using Bag-of-words and TF-IDF approaches
Apply classifiers (Logistic and Multinomial Naive Bayes) to perform multi-class classification


### Approach taken to solve the problem

 Preprocessing Instructions
Initialize stopwords as stop with set(stopwords.words('english'))
To retain only alphabets for every instance, use a lambda function in combination with .apply() method that does so. The function that you will be applying to every instance (supposing the instance is row) will be re.sub("[^a-zA-Z]", " ",x). Remember this operation should be carried out on TITLE column only
Next use lambda function and .apply() method to first convert the instances to lowercase (using .lower()) and then tokenize (using .split()). Remember this operation should be carried out on TITLE column only
Now time to remove stopwords from every instance. Again using a combination of lambda function and .apply() method retain only words which are in that instance but not in stop. You can take the help of a list comprehension to achieve it. For ex: [i for i in x if i not in y]. Remember this operation should be carried out on TITLE column only
The steps mentioned above gives a list for every instance across TITLE column. Join the list elements into a single sentence using ' '.join() method of lists. Use both lambda function and .apply() method for it.
Finally split into train and test using train_test_split function where feature is news["TITLE"], target is news["CATEGORY"], test size is 20% and random state is 3. Save the resultant variables as X_train, X_test, Y_train and Y_test


Vectorize with Bag-of-words and TF-IDF approach
After cleaning data its time to vectorize data so that it can be fed into an ML algorithm. You will be doing it with two approaches: Bag-of-words and TF-IDF.

Instructions
Initialize Bag-of-words vectorizer using CountVectorizer() and TF-IDF vectorizer using TfidfVectorizer(ngram_range=(1,3)). Save them as count_vectorizer and tfidf_vectorizer respectively
Next thing to do is fit each vectorizer on training and test features with text data and transform them to vectors.
First fit and transform data with count_vectorizer on X_train using .fit_transform(X_train) method of count_vectorizer and save it as X_train_count
Use this fitted version of count_vectorizer on X_test and transform X_test with .transform(X_test) method of count_vectorizer. Save it as X_test_count
Similarly repeat the previous two steps with tfidf_vectorizer and save the transformed training feature as X_train_tfidf and transformed test feature as X_test_tfidf

Predicting with Multinomial Naive Bayes
Multinomial Naive Bayes is an algorithm that can be used for the purpose of multi-class classification. You will be using it to train and test it on both the versions i.e. Bag-of-words and TF-IDF ones and then checking the accuracy on both of them

Instructions
First initialize two Multinomial Naive Bayes classifiers with MultinomialNB() and save them as nb_1 and nb_2. The reason for initializing two classifiers is because you will be training and testing on both Bag-of-words and TF-IDF transformed training data

Fit nb1onXtraincountandYtrainusing.fit()` method

Fit nb2onXtraintfidfandYtrainusing.fit()` method

Find the accuracy with Bag-of-words approach using accuracy_score(nb_1.predict(X_test_count), Y_test) and save it as acc_count_nb

Similarly find the accuracy for the TF-IDF approach (only difference is the classifer is nb_2) and save it as acc_tfidf_nb

Print out acc_count_nb and acc_tfidf_nb to check which version performs better for with Multinomial Naive Bayes as classifer


