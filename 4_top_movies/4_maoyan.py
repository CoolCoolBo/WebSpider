from requests.exceptions import RequestException
import requests, re, json, time

def get_one_page(url):
	try:
		headers = {
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
		}
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		return None

def parse_one_page(html):
	pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?<img.*?data-src="(.*?)".*?name.*?}">(.*?)</a>.*?star">(.*?).*?</p>.*?releasetime">(.*?)</p>.*?score.*?integer">(.*?)</i>.*?>(.*?)</i>', re.S)
	items = re.findall(pattern, html)
	for item in items:
		yield {
			'index': item[0],
			'image': item[1],
			'title': item[2].strip(),
			'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
			'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
			'score': item[5].strip() + item[6].strip()
		}

# 写入文件
def write_to_file(content):
	with open('result.txt', 'a', encoding='utf-8') as f:
		print(type(json.dumps(content)))
		f.write(json.dumps(content, ensure_ascii=False)+'\n')

def main(offset):
	url = 'http://maoyan.com/board/4?offset' + str(offset)
	html = get_one_page(url)
	for item in parse_one_page(html):
		write_to_file(item)

if __name__ == '__main__':
	for i in range(10):
		main(offset=i * 10)
		time.sleep(1)