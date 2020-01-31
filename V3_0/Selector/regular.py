import re


class Regular:
	# 用于快速使用正则表达式提取所有数据
	@classmethod
	def getAll(cls, data, pattern):
		expression = re.compile(pattern, re.DOTALL)
		res = expression.findall(data, re.S)
		if len(res) == 0:
			res = ['']
		return res
