import os
import pickle
from ..Error.api import FileNotExistError


def getPickleFileData(pickleFilePath):
	if not os.path.exists(pickleFilePath):
		raise FileNotExistError
	with open(pickleFilePath, 'rb') as f:
		data = pickle.load(f)
		f.close()
		return data
