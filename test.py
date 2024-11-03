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
