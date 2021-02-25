import nltk
# download tokenizer
#nltk.download('punkt')
from nltk.tokenize import word_tokenize
import re
# download list of stopwords
nltk.download('stopwords')
from nltk.corpus import stopwords

#from nltk.stem.porter import PorterStemmer
#stemmer = PorterStemmer()
lemmatizer = nltk.WordNetLemmatizer()


def process_text(text):
    # Make all the strings lowercase and remove non alphabetic characters
    text = re.sub('[^A-Za-z]', ' ', text.lower())

    # tokenize the text: separate every sentence into a list of words
    # hint: text is already split into sentences, so no need to use sent_tokenize
    tokenized_text = word_tokenize(text)

    # Remove the stopwords and stem each word to its root
    clean_text = [lemmatizer.lemmatize(word) for word in tokenized_text
                  if word not in stopwords.words('english')]
    return clean_text
