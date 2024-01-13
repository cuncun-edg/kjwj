import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'
}
url ='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
data = {
    'cname': '',
    'pid': '',
    'keyword': '江西',
    'pageIndex': '1',
    'pageSize': '10',
}
response = requests.post(url=url,headers=headers,data=data)
page_text = response.json()
for dic in page_text['Table1']:
    title = dic['storeName']
    addr = dic['addressDetail']
    print(title,addr)