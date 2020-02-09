from V3_0.Storer.MySQL.api import createTables, insertList, dropAllTable
from .Cleaner.api import optimizeCourse, optimizeProposedEnrollment

priorSubject = [
	'0854-电子信息',
	'0835-软件工程'
]


def initRawData(data):
	# ExcelFilesPath = data[0] # D:\0\G\考研数据分析\Database\ExcelFiles
	data = data[1:]
	# subjectHead = data[1][0] # ('D:\\0\\G\\考研数据分析\\Database\\ExcelFiles\\0101-哲学', 'D:\\0\\G\\考研数据分析\\Database\\ExcelFiles\\0101-哲学\\rawInfo.xlsx', 'rawInfo', ['机构名', '院系所', '专业', '研究方向', '考试方式', '学习方式', '指导教师', '拟招生人数', '考试范围', '政治', '外语', '业务课一', '业务课二', '跨专业', '备注'])
	# print(subjectHead[0])# D:\0\G\考研数据分析\Database\ExcelFiles\0101-哲学
	# print(subjectHead[-1])# ['机构名', '院系所', '专业', '研究方向', '考试方式', '学习方式', '指导教师', '拟招生人数', '考试范围', '政治', '外语', '业务课一', '业务课二', '跨专业', '备注']
	# print(data[1][1])# [('10001-北京大学', 'http://yz.chsi.com.cn/zsml/querySchAction.do?dwmc=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6&yjxkdm=0101'), '(023)哲学系', '(010101)马克思主义哲学', '(01)马克思主义哲学史', '统考', '全日制', '', '专业：3(不含推免)', ('点此查看', 'http://yz.chsi.com.cn/zsml/kskm.jsp?id=1000121023010101011'), '101-思想政治理论：见招生简章', '201-英语一：见招生简章\n或:\n202-俄语：见招生简章\n或:\n203-日语：见招生简章\n或:\n254-德语：见招生简章', '652-西方哲学史一：见招生简章', '931-马克思主义哲学：见招生简章', '', '拟接收推免生以教育部推免服务系统确认录取人数为准。考试科目③西方哲学史一包括现代部分，考试科目④马克思主义哲学包括历史和原理部分。']
	tablesName = []
	iLi = []
	for subject in data:
		tableName = str.split(subject[0][0], '\\')[-1]
		if tableName not in priorSubject:
			continue
		tablesName.append(tableName)
		for rawInfo in subject[1:]:
			info = getInfo(rawInfo)
			if info is False:
				continue
			iLi.append((tableName, info))
	dropAllTable()
	createTables(tablesName)
	insertList(iLi)


def getInfo(rawInfo):
	(institutionInfo, department, major, researchDirection,
	 examinationMethod, learningStyles, instructor, proposedEnrollment,
	 examinationSyllabusInfo, politics, foreignLanguage, businessClassOne, businessClassTwo,
	 transdiscipline, Notes) = rawInfo
	institution, institutionURL = institutionInfo
	examinationSyllabusURL = examinationSyllabusInfo[1]

	proposedEnrollment = optimizeProposedEnrollment(proposedEnrollment)
	if proposedEnrollment is False:
		return False
	politics, foreignLanguage, businessClassOne, businessClassTwo = optimizeCourse(politics, foreignLanguage,
																				   businessClassOne, businessClassTwo)

	return (institution, institutionURL, department, major, researchDirection,
			examinationMethod, learningStyles, instructor, proposedEnrollment,
			examinationSyllabusURL, politics, foreignLanguage, businessClassOne, businessClassTwo,
			transdiscipline, Notes)