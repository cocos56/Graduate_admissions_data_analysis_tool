import os
from V3_0.Setting.api import dbPath


def getDataBasePath():
	if os.path.exists(dbPath):
		return dbPath
	if os.path.exists(os.path.dirname(dbPath)):
		os.mkdir(dbPath)
		return dbPath
	raise FatherPathNotExist


class FatherPathNotExist(Exception):
	def __str__(self):
		return "父目录不存在，请检查"
