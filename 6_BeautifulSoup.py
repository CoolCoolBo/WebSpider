
# **********************************BeautifulSoup***********************************
# from bs4 import BeautifulSoup

# soup = BeautifulSoup('<p>Hello</p>', 'lxml')
# print(soup.p.string)

# --------------------------基本用法-----------------------------
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
# html = """
# <html><head><title>The Dormouse's story</title></head>
# """
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.head.title)
# print(type(soup.head.title))
# print(soup.head.title.string)


# --------------------------节点选择器：关联选择-----------------------------
# 子节点
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.p.children)
# for i, child in enumerate(soup.p.children):
# 	print(i, child)

# 子孙节点
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.p.descendants)
# for i, child in enumerate(soup.p.descendants):
	# print(i, child)

# 父节点
# soup.a.parent
# 所有祖先节点
# soup.a.parents
# 兄弟节点
# soup.a.next_sibling
# soup.a.previous_sibling


# --------------------------方法选择器: findall()-----------------------------
# find_all(name, attrs, recursive, text,**kwargs)

# name
# soup.find_all(name='ul')

# attrs
# soup.find_all(attrs={'id': 'list-1'})
# soup.find_all(attrs={'name': 'elements'})
# soup.find_all(id='list-1') | soup.find_all(class_='element') # 常用的属性可以不用attrs,直接用属性名

# text
# text参数可以用来匹配节点的文本，传输的形式是字符串或正则表达式，结果返回匹配的文本组成的列表


# --------------------------方法选择器: find()-----------------------------
# 返回匹配到的第一个节点


# --------------------------CSS选择器-----------------------------
# soup.select('ul li')
# soup.select('.panel .panel-heading')
