"""
* 采集器模块
* 为采集网页数据提供支持
对外主要提供getHtmlTextData(url, filePath)与saveCount()方法
其中getHtmlTextData用于采集HTML网页的数据，saveCount用于保存采集的计数信息到硬盘
"""
import requests
import os
from V3_0.Storer.WriteData.api import writeDataToFile
from .Config.api import getHeaders, saveCount
from .Config.api import getCount2, setCount2
from .Config.api import getCount, setCount
from .Config.api import getErrCount, setErrCount
from .Config.api import getErrMax, setErrMax
from .Config.api import getErrNum, setErrNum
from .Config.api import getSmallestFileSize, setSmallestFileSize
from V3_0.Storer.Error.api import FileNotExistError, FileSizeIsZeroError


def getHtmlTextData(url, filePath):
	path = filePath + '.html'
	try:
		data = _getHtmlFileData(path)
	except FileNotExistError:
		setCount(getCount() + 1)
		print('count=%d, errCount=%d, errMax=%d' % (getCount(), getErrCount(), getErrMax()))
		print(filePath)
		print('No.', getErrNum() + 1, ' accessing ', url, sep='')
		try:
			r = requests.get(url, headers=getHeaders())
			setErrNum(0)
		except Exception as err:
			print(err)
			_regainHtmlTextData(url, filePath)
		else:
			writeDataToFile(path, r.text)
		return _getHtmlFileData(path)
	else:
		setCount2(getCount2()+1)
		return data


# 重新采集网页数据并将其转为文本数据，一般用于处理异常
def _regainHtmlTextData(url, filePath):
	setErrCount(getErrCount()+1)
	setErrNum(getErrNum()+1)
	if getErrMax() < getErrNum():
		setErrMax(getErrNum())
	getHtmlTextData(url, filePath)


# 从本地文件中读取数据，一般首次爬取会从网上下载网页，接着保存在本地，这样再次爬取直接从本地读数据。
def _getHtmlFileData(FilePath):
	if not os.path.exists(FilePath):
		raise FileNotExistError
	size = os.path.getsize(FilePath)
	size = size // 1024
	if size == 0:
		print('deleting', size, FilePath)
		os.remove(FilePath)
		raise FileSizeIsZeroError
	if getSmallestFileSize() > 0 and size > 0:
		if size < getSmallestFileSize():
			print('smallerSize:', size, FilePath)
			print('smallestFileSize', getSmallestFileSize())
			setSmallestFileSize(size)
			saveCount()
	with open(FilePath, 'r', encoding='utf-8') as f:
		data = f.read()
		f.close()
		return data
