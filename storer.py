"""
* 存储器模块
* 为存储与读取数据提供支持
"""

import json
from V3_0.Storer.GetData.api import getPickleFileData
from V3_0.Storer.Error.api import FileNotExistError
from V3_0.Storer.WriteData.api import writeDataToPickleFile


class storer:
	"""
    本类用于写入数据到硬盘/从硬盘读取数据
	本类采用单例模式（通过重写new方法，并对外提供getInstance接口）
    """

	def writeStringDataToJsonFile(self, data, filePath):
		data = json.loads(data)
		with open(filePath, 'w') as f:
			json.dump(data, f)
			f.close()
		pass

	def getJsonFileData(self, filePath):
		with open(filePath, 'r') as f:
			data = json.load(f)
			f.close()
		# 返回数据
		return data

	def getPickleFileDataFromJsonFile(self, pickleFilePath, func, jsonFilePath):
		try:
			data = getPickleFileData(pickleFilePath)
		except FileNotExistError:
			data = storer.getInstance().getJsonFileData(jsonFilePath)
			data = func(data)
			writeDataToPickleFile(pickleFilePath, data)
		return data
