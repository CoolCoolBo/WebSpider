
# ***************************lxml解析库*****************************

# ------------------------网页解析-----------------------------
# from lxml import etree

# text = '''
# <div>
# <ul>
# <li class="item-O"><a href="link1.html">first item</a></li>
# <li class="item-1"><a href="link2.html">second item</a></li>
# <li class="item-inactive"><a href="link3.html">third item</a></ih>
# <li class="item-1"><a href="link4.html">fourth item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a>
# </ul>
# </div>
# '''
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf-8'))

# 直接读取文本文件进行解析
# from lxml import etree

# html = etree.parse('./test.html', etree.HTMLParser())
# result = etree.tostring(html)
# print(result.decode('utf-8'))


# ------------------------所有节点-----------------------------

# 选取所有节点
# from lxml import etree
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//*')
# print(result)

# 选取所有li节点
# from lxml import etree
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li')
# print(result)


# ------------------------子节点-----------------------------
# 注意/和//的区别，其中/用于获取直接子节点，//用于获取所有子孙节点

# from lxml import etree

# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li/a')
# print(result)


# ------------------------父节点-----------------------------

# 首先选中href属性为link4.html的a节点，然后再获取其父节点，然后再获取其class属性
# from lxml import etree

# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//a[@href="link4.html"]/../@class')
# print(result)


# ------------------------属性匹配-----------------------------
# 我们还可以用＠符号进行属性过滤。比如，这里如果要选取class为item-1的li节点
# from lxml import etree

# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li[@class="item-1"]')
# print(result)


# ------------------------文本获取-----------------------------

# from lxml import etree

# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]//text()')
# print(result)


# ------------------------属性获取-----------------------------

# from lxml import etree

# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li/a/@href')
# print(result)


# ------------------------属性多值匹配-----------------------------

# from lxml import etree

# text = '''
# <li class="li li-first"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[contains(@class, "li")]/a/text()')
# print(result)



# ------------------------多属性匹配-----------------------------

# from lxml import etree

# text = '''
# <li class="li li-first" name="item"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
# print(result)


# ------------------------按序选择-----------------------------

from lxml import etree

text = '''
<div>
<ul>
<li class="item-O"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></ih>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
html = etree.HTML(text)
result = html.xpath('//li[1]/a/text()')
print(result)
result = html.xpath('//li[last()]/a/text()')
print(result)
result = html.xpath('//li[position()<3]/a/text()')
print(result)
result = html.xpath('//li[last()-2]/a/text()')
print(result)


# ------------------------节点轴选择-----------------------------

# .........

