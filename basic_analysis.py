'''
in this file i will be experimenting with some basic analysis techniques (i do not have experience in this stuff before so this is simply for learning purposes)
'''
import pandas as pd 
from nltk.corpus import stopwords
from textblob import TextBlob
from tqdm import tqdm
dataset = pd.read_csv('dataset.csv')
#basic pre-processing functions:
def lower_case(data):
    '''converts all the comments to lowercase'''
    data['Comment'] = data['Comment'].apply(lambda x: " ".join(x.lower() for x in x.split()))


def remove_punctuation(data):
    '''removes punctuation from the comments'''
    data['Comment'] = data['Comment'].str.replace('[^\w\s]', '')


def remove_stopwords(data):
    '''removes unnecessary stopwords, might not be needed for this project though'''
    stop = stopwords.words('english')
    data['Comment'] = data['Comment'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))


def remove_most_common_words(data):
    '''removes 10 most frequently occurring words in the dataset, might not be needed for this project though'''
    freq = pd.Series(' '.join(data['Comment']).split()).value_counts()[:10]
    freq = list(freq.index)
    data['Comment'] = data['Comment'].apply(lambda x: " ".join(x for x in x.split() if x not in freq))


def remove_most_rare_words(data):
    '''removes 10 most rare words in the dataset, might not be needed for this project (it might be better to remove all words that occur once only perhaps'''
    freq = pd.Series(' '.join(data['Comment']).split()).value_counts()[-10:]
    freq = list(freq.index)
    data['Comment'] = data['Comment'].apply(lambda x: " ".join(x for x in x.split() if x not in freq))


def spelling_correction(data):
    '''corrects spelling of comments, is slow and may or may not be accurate, YEA I THINK BETTER NOT TO USE IT'''
    data['Comment'].apply(lambda x: str(TextBlob(x).correct()))


def tokenize(data):
    '''tokenizes comments: divides them into lists of words, and adds the result to a new column called Tokenized Comment'''
    all_tokenized = []
    for i in tqdm(range(len(data.index)), ncols=100):
        all_tokenized.append(list(TextBlob(data['Comment'][i]).words))
    data['Tokenized Comment'] = all_tokenized


