import requests
import pandas as pd

rom requests.exceptions import URLRequired
API_KEY = #Put your unique API key here#
CHANNEL_ID = #Put channel Id of the channel whoose info you want#
url = "https://www.googleapis.com/youtube/v3/search?key="+API_KEY+"&channelId="+CHANNEL_ID+"&part=snippet,id&order=date&maxResults=1000"
response = requests.get(url).json()

df = pd.DataFrame(columns=["video_title","upload_date","views","likes","comments"])

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
    
    df = df.append({'video_title':title,"upload_date":date,"views":view_count,"likes":like_count,"comments":comment_count},ignore_index=True)
 
df = df.sort_values(by="views",ascending=False)
    

    
