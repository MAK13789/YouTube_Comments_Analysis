'''
this file will investigate the relationship between the number of likes a comment has and its sentiment (polarity and subjectivity score)
'''
import pandas as pd
dataset = pd.read_csv('plain_sentiment.csv')
likes_column = dataset["Likes"]
likes_complete = []
for i in likes_column:
    likes_complete.append(i)
sentiment_column = dataset["Sentiment"]
sentiment_complete = []
for j in sentiment_column:
    sentiment_complete.append(j)
print (likes_complete)
print (sentiment_complete)
print (len(likes_complete))
print (len(sentiment_complete)