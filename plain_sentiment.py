'''
this file will directly do sentiment analysis on the dataset, without any preprocessing
'''
from textblob import TextBlob
import pandas as pd
from tqdm import tqdm
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
        comment_sentiment = TextBlob(j).sentiment



    '''
    sentiments = []
    error_count = 0
    for index, row in tqdm(data.iterrows(), ncols=100):
        try:
            comment = data.at[row, "Comment"]
            sentiment = TextBlob(comment).sentiment
            temp = []
            temp.append(sentiment.polarity)
            temp.append(sentiment.subjectivity)
            sentiments.append(temp)  
        except:
            error_count += 1
    print (error_count)
    return sentiments 
    '''
#sentiments = plain_sentiment(dataset)
#print (sentiments)
comment_column = dataset["Comment"]
comments = []
#print (len(comment_column))
for i in comment_column:
    comments.append(i)
sentiment = TextBlob(comments[64523]).sentiment
temp = []
temp.append(sentiment.polarity)
temp.append(sentiment.subjectivity)
print (temp)



'''
returns empty list and error count which is the same as the num of iterations......
doing sth wrong then so gotta fix this
'''

