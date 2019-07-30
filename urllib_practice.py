# -*- coding: utf-8 -*
# import urllib.request

# response = urllib.request.urlopen('https://www.python.org')
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))
# ----------------------------------------------------------
# import urllib.parse
# import urllib.request

# string = urllib.parse.urlencode({'word': 'hello'})
# data = bytes(string, encoding='utf=8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())
# ------------------------------------------------------------
# import socket
# import urllib.request
# import urllib.error

# try:
# 	response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# except urllib.error.URLError as e:
# 	if isinstance(e.reason, socket.timeout):
# 		print('TIME OUT!')
# -----------------------------------------------------
# from urllib import request, parse

# url = 'http://httpbin.org/post'
# headers = {
# 	'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
# 	'Host': 'httpbin.org'
# }
# dict = {
# 	'name': 'Germey'
# }
# data = bytes(parse.urlencode(dict), encoding='utf8')
# req = request.Request(url=url, data=data, headers=headers, method='POST')
# response = request.urlopen(req)
# print(response.read().decode('utf8'))
# --------------------------------------------------------------

# from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
# from urllib.error import URLError

# username = 'username'
# password = 'password'
# url = 'http://localhost:5000/'

# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username, password)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)

# try:
# 	result = opener.open(url)
# 	html = result.read().decode('utf-8')
# 	print(html)
# except URLError as e:
# 	print(e.reason)
# ---------------------------验证-----------------------------------

# from urllib.error import URLError
# from urllib.request import ProxyHandler, build_opener

# proxy_handler = ProxyHandler({
# 	'http': 'http://127.0.0.1:9743',
# 	'https': 'https://127.0.0.1:9743'
# 	})
# opener = build_opener(proxy_handler)
# try:
# 	response = opener.open('https://www.baidu.com')
# 	print(response.read().decode('utf8'))
# except URLError as e:
# 	print(e.reason)
# ---------------------------代理----------------------------

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
import requests

files = {'file': open('favicon.ico', 'rb')}
r = requests.post("http://httpbin.org/post", files=files)
print(r.text)