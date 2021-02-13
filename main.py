import pandas as pd
import os
import google.oauth2.credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
CLIENT_SECRETS_FILE = "client_secret.json"
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
def get_authenticated_service():
    credentials = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)
    #  Check if the credentials are invalid or do not exist
    if not credentials or not credentials.valid:
        # Check if the credentials have expired
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRETS_FILE, SCOPES)
            credentials = flow.run_console()
 
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)
 
    return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

'''
if __name__ == '__main__':
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    service = get_authenticated_service()
'''
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
service = get_authenticated_service()
def data_one_query(query):
    '''gets the relevant data for one query (which is a string input to the function)'''
    query_results = service.search().list(
        part = 'snippet',
        q = query,
        order = 'viewCount', 
        maxResults = 20,
        type = 'video', 
        relevanceLanguage = 'en',
        safeSearch = 'moderate',
        ).execute()
    video_id = []
    channel = []
    video_title = []
    video_desc = []
    for item in query_results['items']:
        video_id.append(item['id']['videoId'])
        channel.append(item['snippet']['channelTitle'])
        video_title.append(item['snippet']['title'])
        video_desc.append(item['snippet']['description'])
    video_id_pop = []
    channel_pop = []
    video_title_pop = []
    video_desc_pop = []
    comments_pop = []
    comment_id_pop = []
    reply_count_pop = []
    like_count_pop = []
    from tqdm import tqdm
    for i, video in enumerate(tqdm(video_id, ncols = 100)):
        response = service.commentThreads().list(
                    part = 'snippet',
                    videoId = video,
                    maxResults = 100, # Only take top 100 comments...
                    order = 'relevance', #... ranked on relevance
                    textFormat = 'plainText',
                    ).execute()
        comments_temp = []
        comment_id_temp = []
        reply_count_temp = []
        like_count_temp = []
        for item in response['items']:
            comments_temp.append(item['snippet']['topLevelComment']['snippet']['textDisplay'])
            comment_id_temp.append(item['snippet']['topLevelComment']['id'])
            reply_count_temp.append(item['snippet']['totalReplyCount'])
            like_count_temp.append(item['snippet']['topLevelComment']['snippet']['likeCount'])
        comments_pop.extend(comments_temp)
        comment_id_pop.extend(comment_id_temp)
        reply_count_pop.extend(reply_count_temp)
        like_count_pop.extend(like_count_temp)
        
        video_id_pop.extend([video_id[i]]*len(comments_temp))
        channel_pop.extend([channel[i]]*len(comments_temp))
        video_title_pop.extend([video_title[i]]*len(comments_temp))
        video_desc_pop.extend([video_desc[i]]*len(comments_temp))
    query_pop = [query] * len(video_id_pop)
    output_dict = {
        'Query': query_pop,
        'Channel': channel_pop,
        'Video Title': video_title_pop,
        'Video Description': video_desc_pop,
        'Video ID': video_id_pop,
        'Comment': comments_pop,
        'Comment ID': comment_id_pop,
        'Replies': reply_count_pop,
        'Likes': like_count_pop,
        }
    output_df = pd.DataFrame(output_dict, columns = output_dict.keys())
    return output_df


df = data_one_query('athletics')
print (df)
'''
get queries and for each query find the most popular videos and the most popular comments from the most popular videos

first focus on getting data of commments, then analyse it later

https://www.pingshiuanchua.com/blog/post/using-youtube-api-to-analyse-youtube-comments-on-python


problems: comments disabled!!!!  use try except to fix this

googleapiclient.errors.HttpError: <HttpError 403 when requesting https://youtube.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=yi1KOcy4hK4&maxResults=100&order=relevance&textFormat=plainText&alt=json returned "The video identified by the <code><a href="/youtube/v3/docs/commentThreads/list#videoId">videoId</a></code> parameter has disabled comments.". Details: "The video identified by the <code><a href="/youtube/v3/docs/commentThreads/list#videoId">videoId</a></code> parameter has disabled comments.">
'''