-----------------------------------------不能运行-----------------------------------------------
import requests
from lxml import etree


class Login(object):
	def __init__(self):
		self.headers = {
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
		'Host': 'github.com',
		'Referer': 'https://github.com/',
		}
		self.headers1 = {
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
		'Host': 'github.com',
		'Referer': 'https://github.com/',
		'X-Requested-With': 'XMLHttpRequest',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'zh-CN,zh;q=0.9',
		'Connection': 'keep-alive',
		}

		self.login_url = 'https://github.com/login'
		self.post_url = 'https://github.com/session'
		self.logined_url = 'https://github.com/settings/profile'
		self.feed_url = 'https://github.com/dashboard-feed'
		self.session = requests.Session()

	def token(self):
		response = self.session.get(self.login_url, headers=self.headers)
		selector = etree.HTML(response.text)
		token = selector.xpath('//div//input[2]/@value')[0]
		return token

	def login(self, email, password):
		post_data = {
			'commit': 'Sign in',
			'utf8': '✓',
			'authenticity_token': self.token(),
			'login': email,
			'password': password,
			'webauthn-support': 'supported',
		}

		response = self.session.post(self.post_url, data=post_data, headers=self.headers)
		print(response.text)
		response = self.session.get(self.feed_url, headers=self.headers1) # 发送ajax请求
		if response.status_code == 200:
			self.dynamics(response.text)

		response = self.session.get(self.logined_url, headers=self.headers)
		if response.status_code == 200:
			self.dynamics(response.text)

	def dynamics(self, html):
		selector = etree.HTML(html)
		dynamics = selector.xpath('//*[@id="dashboard"]/div/div[2]/div')
		print(dynamics)
		for item in dynamics:
			dynamic = ' '.join(item.xpath('.//div[@class="body"]//div[@class="d-flex flex-justify-between flex-items-baseline"]/div//text()')).strip()
			print(dynamic)

	def profile(self, html):
		selector = etree.HTML(html)
		name = selector.xpath('//input[@id="user_profile_name"]/@value')[0]
		email = selector.xpath('//select[@id="user_profile_email"]/option[@value!=""]/text()')

if __name__ == '__main__':
	login = Login()
	login.login(email='512167784@qq.com', password='zhangjiabo123')