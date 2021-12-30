'''
this file will directly do sentiment analysis on the dataset, without any preprocessing
'''
from textblob import TextBlob
import pandas as pd
#from tqdm import tqdm
dataset = pd.read_csv('dataset.csv')
def plain_sentiment(data):
    '''takes in a dataset in the form of dataset.csv and for each comment adds the basic sentiment without preprocessing for that comment in a new column with the name of sentiment'''
    #this wasn't working so rn i will try making a new list that has all the sentiments
    
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
    '''add sentiments as a column to the df'''
    return sentiments
sentiments = plain_sentiment(dataset)
print (sentiments)
'''
comment_column = dataset["Comment"]
comments = []
for i in comment_column:
    comments.append(i)
sentiment = TextBlob(comments[64523]).sentiment
temp = []
temp.append(sentiment.polarity)
temp.append(sentiment.subjectivity)
print (temp)
'''
