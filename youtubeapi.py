import pandas
import openpyxl
from googleapiclient.discovery import build

api_key = ''
video_id = 'E1-63UJuz6Q'
# https://www.youtube.com/watch?v=E1-63UJuz6Q

comments = list()
api_obj = build('youtube', 'v3', developerKey=api_key)
response = api_obj.commentThreads().list(part='snippet,replies', videoId=video_id, maxResults=100).execute()

while True:
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']

        comments.append(
            [comment['textDisplay'], comment['authorDisplayName'], comment['publishedAt'], comment['likeCount']])

        if item['snippet']['totalReplyCount'] > 0:
            for reply_item in item['replies']['comments']:
                reply = reply_item['snippet']
                comments.append(
                    [reply['textDisplay'], reply['authorDisplayName'], reply['publishedAt'], reply['likeCount']])

    if 'nextPageToken' in response:
        response = api_obj.commentThreads().list(part='snippet,replies', videoId=video_id,
                                                 pageToken=response['nextPageToken'], maxResults=100).execute()
    else:
        break

df = pandas.DataFrame(comments)
df.to_excel('results.xlsx', header=['comment', 'author', 'date', 'num_likes'], index=None )


# api_youtube = build('youtube','v3',developerKey=api_key)
# response = api_youtube.search().list(
#     q = '삼육대학교',
#     order = 'relevance',
#     part = 'snipet',
#     maxResults = 100
# ).execute()
#
# video_list = []
# for temp in response['items']:
#     try:
#         video_id = temp['id']['videoId']
#         print(video_id)
#         video_list.append(video_id)
#         print(temp['snippet']['title'])
#     except:
#         pass