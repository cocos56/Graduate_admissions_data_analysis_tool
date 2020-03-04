from redis import StrictRedis
from redis.exceptions import ConnectionError
from V3_0.Setting.api import redisHost

sr = StrictRedis(host=redisHost, port=63, db=0)


def getInt(key, default=0):
	"""
	从Redis数据库中通过键获取整数
	:param key: 键
	:param default:当键不存在时设置的默认值
	:return: 键所对应的值
	"""
	try:
		value = int(sr.get(key))
	except ConnectionError as err:
		print(err)
		value = getInt(key, default)
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
