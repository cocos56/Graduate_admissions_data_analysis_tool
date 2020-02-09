from pymysql import connect

# 创建Connection连接并获得Cursor对象
conn = connect(
	host='localhost', port=3306, database='2020SchoolRawData',
	user='root', password='i,@mc0c0@MySQL.com', charset='utf8')

cs = conn.cursor()


def query(cmd):
	cs.execute(cmd)
	results = cs.fetchall()
	return results


def commit():
	"""
	# 提交之前的操作，如果之前已经之执行过多次的execute，那么就都进行提交
	"""
	conn.commit()
