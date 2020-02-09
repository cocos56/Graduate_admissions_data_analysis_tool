from V3_0.Selector.api import findAllWithRe2


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
