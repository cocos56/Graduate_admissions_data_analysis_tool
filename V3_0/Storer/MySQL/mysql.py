from .Config.api import query, commit


def getTables():
	res = query('show tables;')
	tables = []
	for i in res:
		tables.append(i[0])
	return tables


def createTables(tablesName):
	for tableName in tablesName:
		createTable(tableName)


def createTable(tableName, drop=True):
	if tableName in getTables():
		if drop:
			dropTable(tableName)
		else:
			return
	print("CREATE TABLE %s;" % tableName)
	query("""CREATE TABLE `%s`(
	   `机构名` VARCHAR(1000), `机构URL` VARCHAR(1000),
	   `院系所` VARCHAR(1000), `专业` VARCHAR(1000),
	   `研究方向` VARCHAR(1000), `考试方式` VARCHAR(1000),
	   `学习方式` VARCHAR(1000), `拟招生` int,
	   `人数说明` VARCHAR(1000), `考试范围URL` VARCHAR(660) unique,
	   `政治` VARCHAR(1000), `外语` TEXT,
	   `业务课一` TEXT, `业务课二` TEXT,
	   `备注` TEXT)""" % tableName)


def insertList(li):
	cnt = 0
	for i in li:
		if cnt > 100:
			cnt = 0
			commit()
		tableName, info = i
		insert(tableName, info)
		cnt += 1
	commit()


def insert(tableName, info, commitFlag=False):
	(institution, institutionURL, department, major,
	researchDirection, examinationMethod, learningStyles,
	instructor, proposedEnrollment, enrollmentType, examinationSyllabusURL,
	politics, foreignLanguage, businessClassOne,
	businessClassTwo, transdiscipline, Notes) = info
	cmd = """insert into `%s`
	(`机构名`, `机构URL`, `院系所`, `专业`, `研究方向`,
	`考试方式`, `学习方式`, `拟招生`, `人数说明`, `考试范围URL`,
	`政治`, `外语`, `业务课一`, `业务课二`, `备注`)
	value('%s', '%s', '%s', '%s', '%s',
	'%s', '%s', %d, '%s', '%s',
	'%s', '%s', '%s', '%s', '%s')
	""" % (tableName, institution, institutionURL, department, major, researchDirection,
		   examinationMethod, learningStyles, proposedEnrollment, enrollmentType,
		   examinationSyllabusURL, politics, foreignLanguage, businessClassOne, businessClassTwo,
		   Notes)
	# print(cmd)
	query(cmd)
	if commitFlag:
		commit()


def testInsert(tableName, info):
	cmd = """insert into `%s`
	(`机构名`)
	value("%s")
	""" % (tableName, info,)
	print(cmd)
	query(cmd)


def dropTable(tableName):
	cmd = "drop table `%s`;" % tableName
	print(cmd)
	query(cmd)


def dropAllTable():
	for i in getTables():
		dropTable(i)
