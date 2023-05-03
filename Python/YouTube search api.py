import requests

query = input("What do you want to search?: ")
order = input("What order do you want the results displayed in? (date, rating, relevance, viewCount): ")
type = input("Do you want a video, channel, or playlist?(Can enter all in a comma separated list if desired): ")
response = requests.get('https://youtube.googleapis.com/youtube/v3/search?part=snippet&q={}&order={}&type={}&key=AIzaSyB_gUjzz5lntp9dqljGgXUWD61KRYZt0pU'.format(query, order, type))
# print(response.status_code)
# data = response.json()
print(response.text)