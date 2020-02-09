from re import compile, DOTALL, S


# 用于快速使用正则表达式提取所有数据
def findAllWithRe(data, pattern):
	res = compile(pattern, DOTALL).findall(data, S)
	if len(res) == 0:
		res = ['']
	return res


def findAllWithRe2(data, pattern): return compile(pattern).findall(data)

