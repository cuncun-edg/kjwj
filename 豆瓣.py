import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'
}
url = 'https://movie.douban.com/j/chart/top_list'
params = {
    'type': '5',
    'interval_id':'100:90',
    'action':'' ,
    'start': '0',
    'limit': '20',
}
response = requests.get(url=url,params=params,headers=headers)
page_text = response.json()
# print(page_text)
for movie in page_text:
    name = movie['title']
    score = movie['score']
    print(name+'：'+score)