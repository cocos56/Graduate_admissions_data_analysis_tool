from os.path import exists, isfile, isdir
from os import remove
from shutil import rmtree


def deleteFile(path):
	if exists(path) and isfile(path):
		remove(path)


def deleteDir(path):
	if exists(path) and isdir(path):
		rmtree(path)
