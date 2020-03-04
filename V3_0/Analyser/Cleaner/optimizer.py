from V3_0.Selector.api import findAllWithRe2

businessClassTwoExclusionList = [
	# '物理',
	# '电路',
	# '传感器',
	# '信号',
	# '971-互联网+创新设计专业基础综合',
	# '微机',
	# '自动',
	# '通信',
	# '数学',
	# '数值',
	# '信息',
	# '821-常微分方程',
	# '电子',
	# '现代测试',
	# '仪器',
	# '测控',
	# '力',
	# '光',
	# '生物',
	# '化学',
	# '电气',
	# '数字',
	# '环境',
	# '材料',
	# '807-单片机原理及应用',
	# '管理',
	# '940-计算机网络与安全',
]


def exclusionBusinessClassTwo(businessClassTwo):
	return containsLike(businessClassTwo, businessClassTwoExclusionList)


def containsLike(s, likeList):
	for i in likeList:
		if i in s:
			return True
	return False


def removeLike(s, likeList):
	for i in likeList:
		s = str.replace(s, i, "")
	return s


proposedEnrollmentLike = [
	'(不含推免)'
]


def optimizeProposedEnrollment(pe):
	if containsLike(pe, proposedEnrollmentLike):
		pe = removeLike(pe, proposedEnrollmentLike)
		res = findAllWithRe2(pe, r"\d+")
		if int(res[0]) == 0:
			return False
		if len(res) != 1:
			print(pe)
			raise UnknownDataError
		return pe
	print(pe)
	raise UnknownDataError


def optimizeCourse(*args):
	new = []
	for i in args:
		new.append(str.split(i, '：')[0])
	return new


class UnknownDataError(Exception):
	def __str__(self): return "此数据是未知的"
