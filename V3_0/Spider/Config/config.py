from V3_0.Storer.Redis.api import getInt, setInt

_domain = 'http://yz.chsi.com.cn'
_headers = {'User-Agent':
				'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6814.400 QQBrowser/10.3.3005.400'
			}


def getDomain(): return _domain


def getHeaders(): return _headers


class Config:
	count, errCount, errNum, errMax, count2 = 0, 0, 0, 0, 0
	smallestFileSize = 999999999


def getCount(): return getInt("count")


def setCount(c): setInt("count", c)


def getErrCount(): return getInt("errCount")


def setErrCount(c): setInt("errCount", c)


def getErrNum(): return getInt("errNum")


def setErrNum(c): setInt("errNum", c)


def getErrMax(): return getInt("errMax")


def setErrMax(c): setInt("errMax", c)


def getCount2(): return getInt("count2")


def setCount2(c): setInt("count2", c)


def getSmallestFileSize(): return getInt("smallestFileSize", 999999999)


def setSmallestFileSize(c): setInt("smallestFileSize", c)
