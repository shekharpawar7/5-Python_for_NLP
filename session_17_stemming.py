#stemming
import nltk
def get_stem(text):
    stemmer=nltk.porter.PorterStemmer()
    text=" ".join([stemmer.stem(word) for word in text.split()])
    return text

get_stem("we are eating and swamming we have been eating and swaimming he eats and swins : he ate and swam")
        #'we are eat and swam we have been eat and swaim he eat and swin : he ate and swam'
