import json

# ********************************JSON**********************************

# --------------------------loads():读取JSON，将JSON文本字符串转为JSON对象------------------------------
# str = '''
# [{
# 	"name": "bob",
# 	"gender": "male",
# 	"birthday": "1992-10-18"
# },{
# 	"name": "Selina",
# 	"gender": "female",
# 	"birthday": "1995-10-18"
# }]
# '''
# print(type(str))
# data = json.loads(str)
# print(data)
# print(type(data))

# with open('data.json', 'r') as file:
# 	str = file.read()
# 	data = json.loads(str)
# 	print(data)


# --------------------------loads():输出JSON，将JSON对象串转为字符串------------------------------
# data = [{
# 	'name': 'Bob',
# 	'gender': 'male',
# 	'birthday': '1992-10-18'
# }]
# with open('data.json', 'w') as file:
# 	file.write(json.dumps(data, indent=2))

# 有中文的时候
# data = [{
# 	'name': '波',
# 	'gender': '男',
# 	'birthday': '1992-10-18'
# }]
# with open('data.json', 'w', encoding='utf-8') as file:
# 	file.write(json.dumps(data, indent=2, ensure_ascii=False))