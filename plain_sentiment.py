'''
this file will directly do sentiment analysis on the dataset, without any preprocessing
'''
from textblob import TextBlob
temp = TextBlob("i love coding").sentiment