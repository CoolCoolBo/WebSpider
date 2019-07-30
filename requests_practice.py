# -*- coding: utf-8 -*



#********************requests库的使用********************

# import requests

# r = requests.get('https://www.baidu.com/')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)


# import requests

# r = requests.get('http://httpbin.org/get')
# print(r.text)


# import requests

# data = {
# 	'name': 'germey',
# 	'age': 22
# }
# r = requests.get("http://httpbin.org/get", params=data)
# print(type(r.text))
# print(r.text)


# import requests

# r = requests.get("http://httpbin.org/get")
# print(type(r.text))
# print(r.json())
# print(type(r.json()))


# 抓取网页
# import requests
# import re

# headers = {
# 	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
# }
# r = requests.get("https://www.zhihu.com/explore", headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# titles = re.findall(pattern, r.text)
# for t in titles:
# 	print(t.encode('utf8'))


# 抓取二进制数据
# import requests

# r = requests.get('https://github.com/favicon.ico')
# with open('favicon.ico', 'wb') as f:
# 	f.write(r.content)


# POST请求
# import requests

# data = {
# 	'name': 'germey',
# 	'age': 22
# }
# r = requests.post('http://httpbin.org/post', data=data)
# print(r.text)


# 文件上传
# import requests

# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post("http://httpbin.org/post", files=files)
# print(r.text)


# Prepared Request
# from requests import Request, Session

# url = 'http://httpbin.org/post'
# data = {
# 	'name': 'germey'
# }
# headers = {
# 	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'	
# }
# s = Session()
# req = Request('POST', url, data=data, headers=headers)
# prepped = s.prepare_request(req)
# r = s.send(prepped)
# print(r.text)
