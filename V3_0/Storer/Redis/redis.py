from redis import StrictRedis

sr = StrictRedis(host='st.coco56.top', port=6379, db=0)

def getInt(key, default=0):
	"""
	从Redis数据库中通过键获取整数
	:param key: 键
	:param default:当键不存在时设置的默认值
	:return: 键所对应的值
	"""
	value = int(sr.get(key))
	if value is None:
		value = default
		setInt(key, value)
	return value

def setInt(key, value):
	"""
	在Redis数据库中设置键值对
	:param key:
	:param value:
	:return: 成功返回True，错误返回False
	"""
	return sr.set(key, int(value))
