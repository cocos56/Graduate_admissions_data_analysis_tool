from .subjectsCode import SubjectsCode
from .regular import Regular
from .subjectsURLs import SubjectsURLs


# 获取所有学科类别的代码
def getSubjectsCode(data): return SubjectsCode.get(data)


# 用于快速使用正则表达式提取所有数据
def findAllWithRe(data, pattern): return Regular.getAll(data, pattern)

# 获取所有学科类别的URL
def getSubjectsURLs(data):
	return SubjectsURLs.get(data)