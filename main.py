import requests
import pandas
import time

rom requests.exceptions import URLRequired
API_KEY = #Put your unique API key here#
CHANNEL_ID = #Put channel Id of the channel whoose info you want#
url = "https://www.googleapis.com/youtube/v3/search?key="+API_KEY+"&channelId="+CHANNEL_ID+"&part=snippet,id&order=date&maxResults=1000"
response = requests.get(url).json()

for video in response['items']:
  if video['id']['kind'] == "youtube#video":
    id = video['id']['videoId']
    title = video['snippet']['title']
    date = video['snippet']['publishTime']
    date = str(date).split("T")[0]
    url_video_stats = "https://www.googleapis.com/youtube/v3/videos?id="+id+"&part=statistics&key="+API_KEY
    response_video_stats = requests.get(url_video_stats).json()

    view_count = response_video_stats['items'][0]['statistics']['viewCount']
    like_count = response_video_stats['items'][0]['statistics']['likeCount']
    comment_count = response_video_stats['items'][0]['statistics']['commentCount']

    print(date)
    print(title)
    print(view_count)
    print(like_count)
    print(comment_count)
    print("\n")
