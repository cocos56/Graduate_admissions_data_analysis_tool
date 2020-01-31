class SubjectsCode:
	@classmethod
	def get(cls, data):
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


def setProFlag(dic):
	proList = [
		'0252', '0253', '0254', '0255', '0256', '0257', '0351', '0352', '0353', '0451',
		'0452', '0453', '0454', '0551', '0552', '0553', '0651', '0851', '0853', '0854',
		'0855', '0856', '0857', '0858', '0859', '0860', '0861', '0951', '0952', '0953',
		'0954', '1051', '1052', '1053', '1054', '1055', '1056', '1057', '1151', '1251',
		'1252', '1253', '1254', '1255', '1256', '1351',
	]
