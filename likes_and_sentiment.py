'''
this file will investigate the relationship between the number of likes a comment has and its sentiment (polarity and subjectivity score)
'''
import pandas as pd
from ast import literal_eval
dataset = pd.read_csv('plain_sentiment.csv')
likes_column = dataset["Likes"]
likes_complete = []
for i in likes_column:
    likes_complete.append(i)
sentiment_column = dataset["Sentiment"]
sentiment_complete = []
for j in sentiment_column:
    sentiment_complete.append(j)
likes = []
sentiment = []
for k in range(len(sentiment_complete)):
    if sentiment_complete[k] != '[0.0, 0.0]':
        likes.append(likes_complete[k])
        sentiment.append(literal_eval(sentiment_complete[k]))
print (likes)
print (sentiment)
print (len(likes))
print (len(sentiment))