import nltk
import glob
import os, sys

#nltk.download()

from senti_classifier import senti_classifier

path = '/home/stonehange/Desktop/txt_sentoken/pos/'

for filename in os.listdir(path):
#sentences = ['The movie was the worst movie', 'It was the worst acting by the actors']
    pos_score, neg_score = senti_classifier.polarity_scores(filename)
    print pos_score, neg_score

