import os


def runProgram(path):
	path = os.path.abspath(path)
	print(path)
	cwd = os.getcwd()
	os.chdir(os.path.dirname(path))
	os.system("start %s" % path)
	os.chdir(cwd)
