import pymysql

************************************mysql**************************************


--------------------------------------连接数据库---------------------------------------
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:', data)
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8") # 创建spiders数据库
db.close()


--------------------------------------连接spiders数据库, 创建表---------------------------------------
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
cursor.execute(sql)
db.close()


--------------------------------------插入数据---------------------------------------
id = '20120001'
user = 'Bob'
age = 20

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
try:
	cursor.execute(sql, (id, user, age))
	db.commit()
except:
	db.rollback()
db.close()

# 通用方法，可以根据传入字典动态构造sql语句
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()
data = {
	'id': '20120002',
	'name': 'Jordan',
	'age': '21',
}
table = 'students'
keys = ', '.join(data.keys())
print(keys)
values = ', '.join(['%s'] * len(data))
print(values)
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
print(sql)
print(tuple(data.values()))
try:
	if cursor.execute(sql, tuple(data.values())):
		print('Successful')
		db.commit()
except:
	print('Failed')
	db.rollback()
db.close()


--------------------------------------更新数据---------------------------------------
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()
sql = 'UPDATE students SET age = %s WHERE name = %s'
try:
	cursor.execute(sql, (25, 'Bob'))
	db.commit()
except:
	db.rollback()
db.close()

# 如果数据存在，则更新数据;如果不存在，则插入数据   
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()
data = {
 	'id': '20120001',
 	'name': 'Bob',
 	'age': '21',
 }

table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))

sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(table=table, keys=keys, values=values)
update = ', '.join(["{key} = %s".format(key=key) for key in data])
sql += update
print(sql)
try:
	if cursor.execute(sql, tuple(data.values())*2):
		print('Successful')
		db.commit()
except:
	print('Failed')
	db.rollback()
db.close()


--------------------------------------删除数据---------------------------------------
table = 'students'
condition = 'age > 20'
sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
try:
	cursor.execute(sql)
	db.commit()
except:
	db.rollback()
db.close()


--------------------------------------查询数据---------------------------------------
sql = 'SELECT * FROM students WHERE age >= 20'
try:
	cursor.execute(sql)
	print('Count:', cursor.rowcount)
	one = cursor.fetchone()
	print('One:' one)
	results = cursor.fetchall()
	print('Results:', results)
	print('Results Type:', type(results))
	for row in results:
		print(row)
except:
	print('Error')


# 用一条取一条,更高效
sql = 'SELECT * FROM students WHERE age >= 20'
try:
	cursor.execute(sql)
	print(cursor.rowcount)
	row = cursor.fetchone
	while row:
		print('Row: ', row)
		row = cursor.fetchone
except:
	print('Error')