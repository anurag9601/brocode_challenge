from googleapiclient.discovery import build

api_key = 'AIzaSyC8r8XTo2oCgMWjc4hSQaP_sRo973Qit0Y'
youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.search().list(
    part='snippet',
    q="full stack sigma webdev code with harry",
    maxResults=10
)
response = request.execute()

for item in response['items']:
    print(item)
    # print(item['snippet']['title'], item['snippet']['thumbnails']['default']['url'])

#Ram's animation code

import turtle as t
import colorsys
t.bgcolor('black')
t.tracer(100)
t.pensize(1)
h = 0.5
for i in range(250):
    c = colorsys.hsv_to_rgb(h,1,1)
    h = 0.0008
    t.fillcolor(c)
    t.begin_fill()
    t.fd(i)
    t.lt(100)
    t.circle(30)
    for j in range(2):
        t.fd(i*j)
        t.rt(109)
        t.endfill()