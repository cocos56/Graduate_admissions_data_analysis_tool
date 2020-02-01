from V3_0.Spider.Config.api import getDomain
from V3_0.Storer.Config.api import getDataBasePath
from V3_0.Storer.Make.api import makeDir
import os

htmlsRootPath = os.path.join(getDataBasePath(), r'htmls')
indexHtmlsRootPath = os.path.join(htmlsRootPath, r'0000index')

class SubjectsURLs:
	@classmethod
	def get(cls, data):
		urls = {}
		url = getDomain() + '/zsml/queryAction.do?yjxkdm='
		for SC_code in data:
			SC_name = data[SC_code]
			index_url = url + str(SC_code)
			print(index_url, SC_code, SC_name)
			index_htmls_Path = indexHtmlsRootPath + '//' + SC_code + '-' + SC_name
			makeDir(index_htmls_Path)
			# 获取最大页码数
			max = getMaxPageNumberWithIndexURL(index_url, index_htmls_Path + '//1')
			dic = {SC_code: (SC_name, index_url, max)}
			print(dic)
			urls.update(dic)
		return urls


def getMaxPageNumberWithIndexURL(self, index_url, index_htmlPath):
	data = getHtmlTextData(index_url, index_htmlPath)
	pattern = "<a href='#' onclick='nextPage\(\d+?\)'>(\d+?)</a>"
	return self._findAllWithRe(data, pattern)[-1]

