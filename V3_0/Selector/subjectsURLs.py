from V3_0.Spider.Config.api import getDomain
from V3_0.Spider.api import getHtmlTextData
from V3_0.Storer.Make.api import makeDir
from .api import findAllWithRe
import os
from .Config.api import htmlsRootPath
from .Config.api import proList


indexHtmlsRootPath = os.path.join(htmlsRootPath, r'0000index')


def getSubjectsURLs(data):
	urls = {}
	for SC_code in data:
		SC_name = data[SC_code]
		index_url = getIndexURL(SC_code)
		print(index_url, SC_code, SC_name)
		index_htmls_Path = indexHtmlsRootPath + '//' + SC_code + '-' + SC_name
		makeDir(index_htmls_Path)
		# 获取最大页码数
		max = getMaxPageNumberWithIndexURL(index_url, index_htmls_Path + '//1')
		dic = {SC_code: (SC_name, index_url, max)}
		print(dic)
		urls.update(dic)
	return urls


url = r'%s/zsml/queryAction.do?yjxkdm=' % getDomain()
def getIndexURL(SC_code):
	u = "%s%s" % (url, SC_code)
	if SC_code in proList:
		u = "%s&mldm=zyxw" % u
	else:
		u = "%s&mldm=%s" % (u, SC_code[:2])
	return u

def getMaxPageNumberWithIndexURL(index_url, index_htmlPath):
	data = getHtmlTextData(index_url, index_htmlPath)
	pattern = "<a href='#' onclick='nextPage\(\d+?\)'>(\d+?)</a>"
	return findAllWithRe(data, pattern)[-1]

