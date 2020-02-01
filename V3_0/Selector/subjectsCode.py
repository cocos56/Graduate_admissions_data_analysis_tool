def getSubjectsCode(data):
	data2 = {}
	for i in data:
		dic = {i['dm']: i['mc']}
		data2.update(dic)
	data = modifySubjectsName(data2)
	print(data2)
	return data


# 修正没有名字的学科类别
def modifySubjectsName(data):
	modifyList = [
		('0471', '教育经济与管理'),
		('0784', '教育技术学'),
		('0785', '运动人体科学'),
		('0786', '农药学'),
		# ('1073', ''),
		('1074', '社会医学与卫生事业管理')
	]
	for mod in modifyList:
		(code, name) = mod
		data.update({code: name})
	return data
