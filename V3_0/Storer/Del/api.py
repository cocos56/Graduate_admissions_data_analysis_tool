import os


def deleteFile(path):
	if os.path.exists(path):
		os.remove(path)
