# -*- coding: utf-8 -*


#********************requests库的使用********************

# ------------------------get请求-------------------------
# import requests

# r = requests.get('https://www.baidu.com/')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)


# import requests

# r = requests.get("http://httpbin.org/get")
# print(type(r.text))
# print(r.json())
# print(type(r.json()))


# ------------------------get传入参数-------------------------
# import requests

# data = {
# 	'name': 'germey',
# 	'age': 22
# }
# r = requests.get("http://httpbin.org/get", params=data)
# print(type(r.text))
# print(r.text)


# ------------------------添加header抓取网页-------------------------
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


# ------------------------抓取二进制数据-------------------------
# import requests

# r = requests.get('https://github.com/favicon.ico')
# with open('favicon.ico', 'wb') as f:
# 	f.write(r.content)


# ------------------------POST-------------------------
# import requests

# data = {
# 	'name': 'germey',
# 	'age': 22
# }
# r = requests.post('http://httpbin.org/post', data=data)
# print(r.text)


# ------------------------文件上传-------------------------
# import requests

# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post("http://httpbin.org/post", files=files)
# print(r.text)


# ------------------------获取Cookies-------------------------
# import requests

# r = requests.get("https://www.baidu.com")
# print(r.cookies)
# for key, value in r.cookies.items():
# 	print(key + '=' + value)


# ------------------------利用Cookies登录-------------------------
# import requests

# headers = {
# 	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
# 	'Cookie': '_zap=52ac7807-b7ab-4d55-ac5c-0e418d6bf12e; d_c0="AFCoyL9Lcg6PTurxgbjUMnzIoe-ZBzBDA_g=|1540968436"; __utma=51854390.1184363008.1542701500.1542701500.1542701500.1; __utmv=51854390.100-1|2=registration_date=20131211=1^3=entry_date=20131211=1; _xsrf=PuknZMEJahfCBH7GWff0c95UEiayx5IH; q_c1=a241a3c0fb334ba596ffa54581d391f2|1552610144000|1541638967000; tst=r; capsion_ticket="2|1:0|10:1564474344|14:capsion_ticket|44:ZjRlMWFkMWZiMmRjNDMyOWFmODZiYzQ2ZDVlNjc3MWY=|c04c0069c449df1692bf8eced0d7055fb9901717b1be51d570539e5e53f80b0c"; z_c0="2|1:0|10:1564474346|4:z_c0|92:Mi4xS01NbkFBQUFBQUFBVUtqSXYwdHlEaVlBQUFCZ0FsVk42a2t0WGdEWi04MzlraUpSak11eTJkV0FwNlpEMHlrd1pR|6f374832cb96d080ed48bd6e719fbeeb1c6d2a72494de724c745004e01279a57"; tgw_l7_route=a37704a413efa26cf3f23813004f1a3b',
# 	'authority': 'www.zhihu.com'
# }
# r = requests.get('https://www.zhihu.com', headers=headers)
# print(r.text)


# ------------------------会话维持-------------------------
# import requests

# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789') # 在测试网址中设置cookie
# r = s.get('http://httpbin.org/cookies')
# print(r.text)


# ------------------------代理设置-------------------------
# import requests

# proxies = {
# 	"http": "http://10.10.1.10:3128",
# 	"https": "http://10.10.1.10:1080",
# }
# r = requests.get("https://www.taobao.com", proxies=proxies)
# print(r.status_code)


# ------------------------代理设置-------------------------
# import requests

# r = requests.get("https://www.taobao.com", timeout = 1)
# print(r.status_code)


# ------------------------身份验证-------------------------
# import requests
# from requests.auth import HTTPBasicAuth

# r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
# print(r.status_code)
# 上面代码可以简写为下面。
# import requests

# r = requests.get('http://localhost:5000', auth=('username', 'password'))
# print(r.status_code)


# ------------------------Prepared Request-------------------------
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
