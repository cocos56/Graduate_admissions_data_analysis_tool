import re


# 用于快速使用正则表达式提取所有数据
def findAllWithRe(data, pattern):
	expression = re.compile(pattern, re.DOTALL)
	res = expression.findall(data, re.S)
	if len(res) == 0:
		res = ['']
	return res
