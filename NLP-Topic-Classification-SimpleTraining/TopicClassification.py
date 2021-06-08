import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report
import Preprocessing



# collect data from the file as a list of lists.
# inner list: one entry per column
# outer list: rows
reviews = [row for row in csv.reader(open('reviews.csv'))]

# Processing the Data
# remove first row that carries only labels
reviews = reviews[1:]

# the text to analyse is found in the first column of the data
texts = [row[0] for row in reviews]
# the third column of the data contains already annotated topics
topics = [row[2] for row in reviews]

# process the text but transform the list of words back to string format
# this turns the sentences in texts into a list of stemmed words without any
# connectors
texts = [' '.join(Preprocessing.process_text(text)) for text in texts]

# vectorize the texts
matrix = CountVectorizer(max_features=1000)
vectors = matrix.fit_transform(texts).toarray()

# separate training and test data
vectors_train, vectors_test, topics_train, topics_test = train_test_split(vectors, topics)

# train a naive bayes classifier with the training set and test the model
classifier = GaussianNB()
classifier.fit(vectors_train, topics_train)

# predict with the testing set
topics_pred = classifier.predict(vectors_test)

# and measure the accuracy
print(classification_report(topics_test, topics_pred))
