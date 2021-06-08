import nltk

from nltk.tokenize import word_tokenize
import re
# download list of stopwords

from nltk.corpus import stopwords, wordnet

# a new comment
#from nltk.stem.porter import PorterStemmer
#stemmer = PorterStemmer()
lemmatizer = nltk.WordNetLemmatizer()

def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)


def process_text(text):
    # Make all the strings lowercase and remove non alphabetic characters
    text = re.sub('[^A-Za-z]', ' ', text.lower())

    # tokenize the text: separate every sentence into a list of words
    # hint: text is already split into sentences, so no need to use sent_tokenize
    tokenized_text = word_tokenize(text)

    # Remove the stopwords and stem each word to its root
    clean_text = [lemmatizer.lemmatize(word, get_wordnet_pos(word)) for word in tokenized_text
                  if word not in stopwords.words('english')]
    return clean_text
