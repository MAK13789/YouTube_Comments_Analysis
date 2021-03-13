'''
this file will directly do sentiment analysis on the dataset, without any preprocessing
'''
from textblob import TextBlob
import pandas as pd
from tqdm import tqdm
dataset = pd.read_csv('dataset.csv')
def plain_sentiment(data):
    '''takes in a dataset in the form of dataset.csv and for each comment adds the basic sentiment without preprocessing for that comment in a new column with the name of sentiment'''
    data["sentiment"] = ""
    for index, row in tqdm(data.iterrows(), ncols=100):
        data.at[index, 'sentiment'] = TextBlob(data.iloc[data]['comment']).sentiment
    data.to_csv('dataset_basic_sentiment.csv')