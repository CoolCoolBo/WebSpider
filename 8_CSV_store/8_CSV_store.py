
***********************************CSV***************************************

import csv

--------------------------------写入-----------------------------------
# with open('data.csv', 'w') as csvfile:
# 	writer = csv.writer(csvfile)
# 	writer.writerow(['id', 'name', 'age'])
# 	writer.writerow(['10001', 'Mike', '20'])
# 	writer.writerow(['10002', 'Bob', '18'])
# 	writer.writerow(['10003', 'Jordan', '22'])

# 改变分隔符
# with open('data.csv', 'w') as csvfile:
# 	writer = csv.writer(csvfile, delimiter=' ')
# 	writer.writerow(['id', 'name', 'age'])
# 	writer.writerow(['10001', 'Mike', '20'])
# 	writer.writerow(['10002', 'Bob', '18'])
# 	writer.writerow(['10003', 'Jordan', '22'])

# 多行写入
# with open('data.csv', 'w') as csvfile:
# 	writer = csv.writer(csvfile)
# 	writer.writerow(['id', 'name', 'age'])
# 	writer.writerows([['10001', 'Mike', '20'], ['10001', 'Bob', '18'], ['10001', 'Jordan', '22']])

# 以字典方式写入
# with open('data.csv', 'w') as csvfile:
# 	fieldnames = ['id', 'name', 'age']
# 	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# 	writer.writeheader()
# 	writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
# 	writer.writerow({'id': '10002', 'name': 'Bob', 'age': 18})
# 	writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 22})

# 追加
# with open('data.csv', 'a') as csvfile:
# 	fieldnames = ['id', 'name', 'age']
# 	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# 	writer.writerow({'id': '10004', 'name': 'Durant', 'age': 21})


--------------------------------读取-----------------------------------
# with open('data.csv', 'r', encoding='utf-8') as csvfile:
# 	reader = csv.reader(csvfile)
# 	for row in reader:
# 		print(row)

# pandas方式
# import pandas as pd
# df = pd.read_csv('data.csv')
# print(df)