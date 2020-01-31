import os


def createDataBase(path):
	if os.path.exists(path):
		return path
	if os.path.exists(os.path.dirname(path)):
		os.mkdir(path)
		return path
	raise FatherPathNotExist


class FatherPathNotExist(Exception):
	def __str__(self):
		return "父目录不存在，请检查"
