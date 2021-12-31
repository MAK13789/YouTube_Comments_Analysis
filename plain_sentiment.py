'''
this file will directly do sentiment analysis on the dataset, without any preprocessing
'''
from textblob import TextBlob
import pandas as pd
dataset = pd.read_csv('dataset.csv')
def plain_sentiment(data):
    '''takes in a dataset in the form of dataset.csv and for each comment adds the basic sentiment without preprocessing for that comment in a new column with the name of sentiment'''
    comment_column = data["Comment"]
    comments = []
    for i in comment_column:    
        comments.append(i)
    sentiments = []
    for j in comments:
        try:
            comment_sentiment = TextBlob(j).sentiment    
            temp = []
            temp.append(comment_sentiment.polarity)
            temp.append(comment_sentiment.subjectivity)
            sentiments.append(temp)
        except:
            sentiments.append([0, 0])
    data["Sentiment"] = sentiments
    return data
updated_dataset = plain_sentiment(dataset)
updated_dataset.to_csv('plain_sentiment.csv')