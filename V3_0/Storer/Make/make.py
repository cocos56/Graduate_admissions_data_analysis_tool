from os.path import exists
from os import mkdir


def makeDir(path):
	if not exists(path):
		mkdir(path)
	return path
