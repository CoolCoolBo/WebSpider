# ---------------------------------urllib----------------------------------
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy = '111.231.94.44:8888'
# proxy = 'username:password@111.231.94.44:8888'  需要认证的代理
proxy_handler = ProxyHandler({
    'http':'http://' + proxy,
    'https':'https://' + proxy
                })
opener = build_opener(proxy_handler)
try:
    response = opener.open('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)

# ---------------------------------requests----------------------------------
import requests

proxy = '111.231.94.44:8888'
proxies = {
	'http': 'http://' + proxy,
	'https': 'https://' + proxy
}
try:
	response = requests.get('http://httpbin.org/get', proxies=proxies)
	print(response.text)
except requests.exceptions.ConnectionError as e:
	print('Error', e.args)

# ---------------------------------selenium----------------------------------
from selenium import webdriver

proxy = '111.231.94.44:8888'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://' + proxy)
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('http://httpbin.org/get')
print(browser.page_source)
