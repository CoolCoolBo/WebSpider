#********************正则表达式********************

# -------------------------- match() 从字符串的开头开始匹配的--------------------------------
# import re

# content = 'Hello 123 4567 World_This is a Regex Demo'
# print(len(content))
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
# print(result)
# print(result.group())
# print(result.span())


# 匹配目标
# import re

# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^Hello\s(\d+)\sWorld', content)
# print(result)
# print(result.group())
# print(result.group(1))
# print(result.span())


# 通用匹配
# import re

# content = 'Hello 123 4567 World_This is a Regex Demo'
# result = re.match('^Hello.*Demo$', content)
# print(result)
# print(result.group())
# print(result.span())


# 贪婪和非贪婪
# import re

# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('.*?(\d+).*Demo$', content)
# print(result)
# print(result.group(1))
# print(result.span())


# 修饰符
# import re

# content = '''Hello 1234567 World_This
# is a Regex Demo
# '''
# result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
# print(result.group(1))


# 转义匹配
# import re

# content = '(百度)www.baidu.com'
# result = re.match('\(百度\)www\.baidu\.com', content)
# print(result)


# -------------------------- search()--------------------------------
# import re

# content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
# result = re.search('Hello.*?(\d+).*?Demo', content)
# print(result)
# print(result.group(1))


# import re

# html = '''< div id="songs-list" >
# <h2 class = "title">经典老歌</h2>
# <p class="introduction">
# 经典老歌列表
# </p>
# <ul id="list" class="list-group">
# <li data-view="2">一路上有你</li>
# <li data-view="7">
# <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
# </li>
# <li data-view="4" class="active">
# <a href="/3.mp3" singer="齐秦">往事随风</a>
# </li>
# <li data-view="6" class="active"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
# <li data-view="5" class="active"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
# <li data-view="5" class="active"><a href="/6.mp3" singer="邓丽君">但愿人长久</a></li>
# </ul>
# </div>'''

# result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
# print(result.group(1), result.group(2))


# -------------------------- findall()--------------------------------
# import re

# html = '''< div id="songs-list" >
# <h2 class = "title">经典老歌</h2>
# <p class="introduction">
# 经典老歌列表
# </p>
# <ul id="list" class="list-group">
# <li data-view="2">一路上有你</li>
# <li data-view="7">
# <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
# </li>
# <li data-view="4" class="active">
# <a href="/3.mp3" singer="齐秦">往事随风</a>
# </li>
# <li data-view="6" class="active"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
# <li data-view="5" class="active"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
# <li data-view="5" class="active"><a href="/6.mp3" singer="邓丽君">但愿人长久</a></li>
# </ul>
# </div>'''
# results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
# print(results)


# -------------------------- sub()--------------------------------
# import re

# content = 'adfa2542adf22asf2141kasf3s3g5'
# content = re.sub('\d+', '', content)
# print(content)


# -------------------------- sub()--------------------------------
import re

content1 = '2016-12-15 12:00'
content2 = '2016-12-17 12:55'
content3 = '2016-12-17 13:55'
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3)