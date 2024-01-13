import requests

keyword = input('enter a key word:')
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'
}
params = {
    'query':keyword
}
# 1.指定url
url = 'https://www.sogou.com/web'
# 2.发起请求get方法的返回值为响应对象
response = requests.get(url=url,params=params,headers=headers)
response.encoding = 'utf-8'
# 3. 获取响应数据
page_text = response.text
fileName = keyword+'.html'
print(fileName)
# 4. 持久化存储
with open(fileName,'w',encoding='utf-8') as fp:
    fp.write(page_text)
print(fileName,'爬取成功！')