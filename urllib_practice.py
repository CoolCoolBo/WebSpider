# -*- coding: utf-8 -*


# ********************urllib库的使用********************


# --------------------------urlopen--------------------------------
# import urllib.request

# response = urllib.request.urlopen('https://www.python.org')
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))


# --------------------------data参数--------------------------------
# import urllib.parse
# import urllib.request

# string = urllib.parse.urlencode({'word': 'hello'})
# data = bytes(string, encoding='utf=8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())


# -------------------------timeout参数--------------------------------
# import socket
# import urllib.request
# import urllib.error

# try:
# 	response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# except urllib.error.URLError as e:
# 	if isinstance(e.reason, socket.timeout):
# 		print('TIME OUT!')


# -------------------------request--------------------------------
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


# -------------------------request验证--------------------------------
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


# ---------------------------request代理-----------------------------------

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
