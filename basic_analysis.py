'''
in this file i will be experimenting with some basic analysis techniques (i do not have experience in this stuff before so this is simply for learning purposes)
'''
import pandas as pd 
dataset = pd.read_csv('dataset.csv')
#basic pre-processing functions:
def lower_case(data):
    '''converts all the comments to lowercase'''
    dataset['Comment'] = dataset['Comment'].apply(lambda x: " ".join(x.lower() for x in x.split()))
def remove_punctuation(data):
    '''removes punctuation from the comments'''
    
