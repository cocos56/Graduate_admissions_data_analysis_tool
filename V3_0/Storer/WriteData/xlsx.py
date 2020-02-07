import xlsxwriter
import os


def writeDataToXlsxFile(filePath, sheetName, sheetHead, sheetDatum):
	if os.path.exists(filePath):
		return
	print(filePath)
	workbook = xlsxwriter.Workbook(filePath)
	ws = workbook.add_worksheet(sheetName)
	r = 0
	c = 0
	format = workbook.add_format(
		{
			'bold': True,
			'font_size': 16,
			'align': 'center',
			'valign': 'vcenter'
		}
	)
	ws.set_row(0, 66)
	ws.freeze_panes(1, 0)
	for i in sheetHead:
		ws.write(r, c, i, format)
		c += 1
	sizeLi = getColumnsSize(sheetHead, oldSizeList=None, factor=1.75)
	r = 1
	format = workbook.add_format(
		{
			'text_wrap': True,
			'valign': 'vcenter'
		}
	)
	urlFormat = workbook.add_format(
		{
			'font_color': 'Blue',
			'valign': 'vcenter'
		}
	)
	for data in sheetDatum:
		c = 0
		for i in data:
			if type(i) == tuple:
				ws.write_url(r, c, i[1], urlFormat, string=i[0])
			else:
				ws.write(r, c, i, format)
			c += 1
		r += 1
		sizeLi = getColumnsSize(data, oldSizeList=sizeLi, factor=1)
	setColumnsSize(ws, sizeLi)
	workbook.close()


def setColumnsSize(worksheet, sizeList):
	cnt = 0
	for size in sizeList:
		worksheet.set_column(cnt, cnt, size)
		cnt += 1


def getColumnsSize(rowsData, oldSizeList=None, factor=1):
	# print(rowsData)
	li = []
	for i in rowsData:
		if type(i) == tuple:
			s = i[0]
		else:
			s = i
		size = getColumnSize(s) * factor
		li.append(size)
	if oldSizeList is not None:
		len1 = len(li)
		len2 = len(oldSizeList)
		if not len1 == len2:
			print('not len1 == len2:')
			exit(-1)
		cntLi = [i for i in range(len1)]
		li2 = []
		for cnt in cntLi:
			if oldSizeList[cnt] >= 56:
				li2.append(56)
				continue
			li2.append(max(li[cnt], oldSizeList[cnt]))
		li = li2
	return li


def getColumnSize(s):
	# chSymbol = [
	#     '–', '—', '‘', '’', '“', '”',
	#     '…', '、', '。', '〈', '〉', '《',
	#     '》', '「', '」', '『', '』', '【',
	#     '】', '〔', '〕', '！', '（', '）',
	#     '，', '．', '：', '；', '？'
	# ]
	chSymbol = [
		8211, 8212, 8216, 8217, 8220, 8221,
		8230, 12289, 12290, 12296, 12297, 12298,
		12299, 12300, 12301, 12302, 12303, 12304,
		12305, 12308, 12309, 65281, 65288, 65289,
		65292, 65294, 65306, 65307, 65311
	]
	# 9是制表符，10是回车，183：·，252：ü，233:é
	enSymbol = [9, 10, 183, 233, 252]
	size = 0
	for c in s:
		o = ord(c)
		# 中文汉字：'\u4e00'到'\u9fa5'
		if (40869 >= o >= 19968) or (o in chSymbol) or (o > 900):
			size += 2
		# 32为空格
		elif (126 >= o >= 32) or (o in enSymbol):
			size += 1
		else:
			for i in s:
				print('c=', i, 'o=', ord(i))
			print('str=', s)
			print('c=', chr(o), 'o=', o)
			raise CharacterOutOfRangeError
	return size


class CharacterOutOfRangeError(Exception):
	def __str__(self):
		return "字符不在已知范围内"
