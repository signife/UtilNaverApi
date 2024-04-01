from googleapiclient.discovery import build

api_key = 'AIzaSyBpp5HYjdWQjhTjTAMAYKFB79PZ5sYleEA'
video_id = 'u2BCGcOweTo'

comment = []

api_youtube = build('youtube','v3',developerKey=api_key)
response = api_youtube.search().list(
    q='삼육대학교',
    order='relevance',
    part='snippet',
    maxResults = 100
).execute()

video_list = []
for temp in response['items']:
    try:
        video_id = temp['id']['videoId']
        print(video_id)
        video_list.append(video_id)
        print(temp['snippet']['title'])
    except:
        pass


