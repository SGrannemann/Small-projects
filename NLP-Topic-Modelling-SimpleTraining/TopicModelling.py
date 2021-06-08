import Preprocessing
from gensim import corpora
from gensim import models
import csv

# read in data from file
reviews = [row for row in csv.reader(open('reviews.csv'))]

# the text to analyse is found in the first column of the data
# texts is a list of strings
texts = [row[0] for row in reviews]
# preprocess the text. texts is now a list of list of stemmed words
texts = [Preprocessing.process_text(text) for text in texts]
# create gensim dictionary using bag of words model
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

# train LDA model with three topics in the data
model = models.ldamodel.LdaModel(corpus, num_topics=3, id2word=dictionary, passes=15)

topics = model.print_topics(num_words=3)
for topic in topics:
    print(topic)
