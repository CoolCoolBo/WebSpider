
# **********************************BeautifulSoup***********************************
# from bs4 import BeautifulSoup

# soup = BeautifulSoup('<p>Hello</p>', 'lxml')
# print(soup.p.string)

# --------------------------基本用法-----------------------------
html = """
<html><head ><title>The Dormouse's story</title></head>
<body>
<p class='title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="linkl"><!-- Elsie -- ></la>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a> ;
and they lived at the bottom of a well.</p>
<p class="story"> ... </p>
"""
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
# print(soup.title.string)


# --------------------------节点选择器：选择元素-----------------------------

# html = """
# <html><head ><title>The Dormouse's story</title></head>
# <body>
# <p class='title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="linkl"><!-- Elsie -- ></la>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a> ;
# and they lived at the bottom of a well.</p>
# <p class="story"> ... </p>
# """
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.title)
# print(type(soup.title))
# print(soup.title.string)
# print(soup.head)
# print(soup.p)


# --------------------------节点选择器：提取信息-----------------------------
# 获取节点的名称
# print(soup.title.name)
# 获取节点的所有属性
# print(soup.p.attrs)
# print(soup.p.attrs['name']) 或 print(soup.p['name'])
# 获取节点的内容
# print(soup.p.string)


# --------------------------节点选择器：嵌套选择-----------------------------
html = """
<html><head><title>The Dormouse's story</title></head>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.head.title)
print(type(soup.head.title))
print(soup.head.title.string)

