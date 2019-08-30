import requests
import os
from hashlib import md5
from urllib.parse import urlencode


def get_page(offset):
	params = {
		'aid': '24',
		'app_name': 'web_search',
		'offset': offset,
		'format': 'json',
		'keyword': '街拍',
		'autoload': 'true',
		'count': '20',
		'n_qc': '1',
		'cur_tab': '1',
		'from': 'search_tab',
		'pd': 'synthesis'
	}
	url = 'https://www.toutiao.com/api/search/content/?' + urlencode(params)
	headers = {
		'authority': 'www.toutiao.com',
		'method': 'GET',
		'path': '/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1567090978232',
		'scheme': 'https',
		'accept': 'application/json, text/javascript',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'zh-CN,zh;q=0.9',
		'content-type': 'application/x-www-form-urlencoded',
		'cookie': 'tt_webid=6730201592479614476; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6730201592479614476; csrftoken=1685d7a366053adcf0a809f2cfbefe6c; s_v_web_id=a7bcb1bbe2b9d5e0d07dbd316a3fe12a; __tasessionId=phmobgtyb1567090632453',
		'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
		'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
		'x-requested-with': 'XMLHttpRequest'
}
	try:
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			return response.json()
	except requests.ConnectionError:
		return None

def get_images(json):
	if json.get('data'):
		for item in json.get('data'):
			if item.get('title'):
				title = item.get('title')
				images = item.get('image_list')
				if images:
					for image in images:
						yield {
							'image': image.get('url'),
							'title': title
						}
	else:
		print('None')

def save_image(item):
	base_file_path = 'picture/' + item.get('title')
	if not os.path.exists(base_file_path):
		os.makedirs(base_file_path)
	try:
		response = requests.get(item.get('image'))
		if response.status_code == 200:
			file_path = 'picture/{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
			if not os.path.exists(file_path):
				with open(file_path, 'wb') as f:
					f.write(response.content)
			else:
				print('Already Downloaded', file_path)
	except requests.ConnectionError:
		print('Failed to Save Image')

def main(offset):
	json = get_page(offset)
	for item in get_images(json):
		print(item)
		save_image(item)

GROUP_START = 0
GROUP_END = 10
if __name__ == '__main__':
	groups = [x * 20 for x in range(GROUP_START, GROUP_END + 1)]
	for i in groups:
		main(i)