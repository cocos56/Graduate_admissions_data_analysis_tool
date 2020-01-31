import os


def getDataBasePath():
	root = r'D:\0\G\考研数据分析'
	path = root + r'\Database'
	print(path)
	if os.path.exists(path):
		return path
	if not os.path.exists(root):
		raise FatherPathNotExist
	os.mkdir(path)
	return path

class FatherPathNotExist(Exception):
	def __str__(self):
		"父目录不存在，请检查"