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

# import http.cookiejar, urllib.request

# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
# 	print(item.name+"="+item.value)

# filename = 'cookies.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# hanlder = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(hanlder)
# reponse = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)
# --------------------------Cookies--------------------------

# from urllib import request, error
# try:
# 	response = request.urlopen('https://cuiqingcai.com/index.htm')
# except error.URLError as e:
# 	print(e.reason)
# --------------------------异常处理：URLError--------------------------

# from urllib import request,error
# try:
# 	response = request.urlopen('https://cuiqingcai.com/index.htm')
# except error.HTTPError as e:
# 	print(e.reason, e.code, e.headers, sep='\n')
# --------------------------异常处理：HTTPError--------------------------

# from urllib import request, error

# try:
# 	response = request.urlopen('https://cuiqingcai.com/index.htm')
# except error.HTTPError as e:
# 	print(e.reason, e.code, e.headers, sep='\n')
# except error.URLError as e:
# 	print(e.reason)
# else:
# 	print('Request Successfully')
# --------------------------异常处理：HTTPError是URLError的子类，先捕获子类异常--------------------------

# from urllib.parse import urlparse

# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# print(type(result), result)
# --------------------------URL解析--------------------------


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


# Cookies
# import requests
# r = requests.get("https://www.baidu.com")
# print(r.cookies)
# for key, value in r.cookies.items():
# 	print(key + '=' + value)

# Cookies
# import requests

# headers = {
# 	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
# 	'Cookie': '_zap=52ac7807-b7ab-4d55-ac5c-0e418d6bf12e; d_c0="AFCoyL9Lcg6PTurxgbjUMnzIoe-ZBzBDA_g=|1540968436"; __utma=51854390.1184363008.1542701500.1542701500.1542701500.1; __utmv=51854390.100-1|2=registration_date=20131211=1^3=entry_date=20131211=1; _xsrf=PuknZMEJahfCBH7GWff0c95UEiayx5IH; q_c1=a241a3c0fb334ba596ffa54581d391f2|1552610144000|1541638967000; tst=r; capsion_ticket="2|1:0|10:1564474344|14:capsion_ticket|44:ZjRlMWFkMWZiMmRjNDMyOWFmODZiYzQ2ZDVlNjc3MWY=|c04c0069c449df1692bf8eced0d7055fb9901717b1be51d570539e5e53f80b0c"; z_c0="2|1:0|10:1564474346|4:z_c0|92:Mi4xS01NbkFBQUFBQUFBVUtqSXYwdHlEaVlBQUFCZ0FsVk42a2t0WGdEWi04MzlraUpSak11eTJkV0FwNlpEMHlrd1pR|6f374832cb96d080ed48bd6e719fbeeb1c6d2a72494de724c745004e01279a57"; tgw_l7_route=a37704a413efa26cf3f23813004f1a3b',
# 	'authority': 'www.zhihu.com'
# }
# r = requests.get('https://www.zhihu.com', headers=headers)
# print(r.text)

# cookies = '_zap=52ac7807-b7ab-4d55-ac5c-0e418d6bf12e; d_c0="AFCoyL9Lcg6PTurxgbjUMnzIoe-ZBzBDA_g=|1540968436"; __utma=51854390.1184363008.1542701500.1542701500.1542701500.1; __utmv=51854390.100-1|2=registration_date=20131211=1^3=entry_date=20131211=1; _xsrf=PuknZMEJahfCBH7GWff0c95UEiayx5IH; q_c1=a241a3c0fb334ba596ffa54581d391f2|1552610144000|1541638967000; tst=r; capsion_ticket="2|1:0|10:1564474344|14:capsion_ticket|44:ZjRlMWFkMWZiMmRjNDMyOWFmODZiYzQ2ZDVlNjc3MWY=|c04c0069c449df1692bf8eced0d7055fb9901717b1be51d570539e5e53f80b0c"; z_c0="2|1:0|10:1564474346|4:z_c0|92:Mi4xS01NbkFBQUFBQUFBVUtqSXYwdHlEaVlBQUFCZ0FsVk42a2t0WGdEWi04MzlraUpSak11eTJkV0FwNlpEMHlrd1pR|6f374832cb96d080ed48bd6e719fbeeb1c6d2a72494de724c745004e01279a57"; tgw_l7_route=a37704a413efa26cf3f23813004f1a3b'
# jar = requests.cookies.RequestsCookieJar()
# headers = {
# 	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
# 	'authority': 'www.zhihu.com'
# }
# for cookie in cookies.split(';'):
# 	key, value = cookie.split('=', 1)
# 	jar.set(key, value)
# r = requests.get("http://www.zhihu.com", cookies=jar, headers=headers)
# print(r.text)


# 会话维持
# import requests

# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)


# 代理设置
# import requests

# proxies = {
# 	"http": "http://10.10.1.10:3128",
# 	"https": "http://10.10.1.10:1080",
# }
# r = requests.get("https://www.taobao.com", proxies=proxies)
# print(r.status_code)


# 超时设置
# import requests

# r = requests.get("https://www.taobao.com", timeout = 1)
# print(r.status_code)


# 身份验证
# import requests
# from requests.auth import HTTPBasicAuth

# r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
# print(r.status_code)
# 上面代码可以简写为下面。
# import requests

# r = requests.get('http://localhost:5000', auth=('username', 'password'))
# print(r.status_code)