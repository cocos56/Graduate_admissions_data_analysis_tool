import os
import pickle
from ..Error.api import FileNotExistError
from ..WriteData.api import writeDataToPickleFile


def getPickleFileData(pickleFilePath):
	if not os.path.exists(pickleFilePath):
		raise FileNotExistError
	with open(pickleFilePath, 'rb') as f:
		data = pickle.load(f)
		f.close()
		return data


def getPickleFileDataFromOtherData(pickleFilePath, func, OtherData):
	try:
		data = getPickleFileData(pickleFilePath)
	except FileNotExistError:
		data = func(OtherData)
		writeDataToPickleFile(pickleFilePath, data)
	return data
