# -*- coding : utf-8 -*-
# @Author : Coco
# @Author's GitHub : https://github.com/COCO5666
# @Author's CSND : https://blog.csdn.net/COCO56
# @Author's Webpage : https://coco5666.github.io/
# @IDE: PyCharm
# @Python: Python3.7.2
# @Created Time :2019-02-16 20:28:46
# @Modified Time :2019-02-16 23:58:25
# @File : spider.py

'''
* 采集器模块
* 为采集网页数据提供支持
对外主要提供getHtmlTextData(url, filePath)与saveCount()方法
其中getHtmlTextData用于采集HTML网页的数据，saveCount用于保存采集的计数信息到硬盘
'''

import requests
import os
from multiple import getArgs
from storer import storer

storerIns = storer.getInstance()

#模块变量
pklPath = storerIns.getDataBasePath() + '\\CountData.pkl'

def _getCount():
    data = storerIns.getPickleFileData(pklPath)
    if data == False:
        count = 0
        errCount = 0
        errNum = 0
        errMax = 0
        count2 = 0
        smallestFileSize = 999999999
    else:
        count = data['count']
        errCount = data['errCount']
        errNum = data['errNum']
        errMax = data['errMax']
        count2 = data['count2']
        smallestFileSize = data['smallestFileSize']
    return getArgs(count, errCount, errNum, errMax, count2, smallestFileSize)

class spider:
    #域名与访问的头
    domain = 'http://yz.chsi.com.cn'
    headers = {'User-Agent':
                        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6814.400 QQBrowser/10.3.3005.400'
                    }

    #解包到本模块变量
    (count, errCount, errNum, errMax, count2, smallestFileSize) = _getCount()

    @staticmethod
    def saveCount():
        dic = {}
        dic.update({'count' : spider.count})
        dic.update({'errCount': spider.errCount})
        dic.update({'errNum': spider.errNum})
        dic.update({'errMax': spider.errMax})
        dic.update({'count2': spider.count2})
        dic.update({'smallestFileSize': spider.smallestFileSize})
        print('saving ')
        storerIns.writeDataToPickleFile(pklPath, dic)

    @staticmethod
    def getHtmlTextData(url, filePath):
        path = filePath + '.html'
        data = spider._getHtmlFileData(path)
        if not data == False:
            spider.count2 += 1
            #print('count2 =', count2, 'got from', path)
            return data
        spider.count += 1
        print('count =', spider.count, ' errCount =', spider.errCount, ' errMax =', spider.errMax)
        print(filePath)
        print('No.', spider.errNum+1, ' accessing ', url, sep='')
        try:
            spider.r = requests.get(url, headers=spider.headers)
            errNum = 0
        except requests.exceptions.SSLError:
            print('requests.exceptions.SSLError')
            spider._regainHtmlTextData(url, filePath)
        except requests.exceptions.ConnectionError:
            print('requests.exceptions.ConnectionError')
            spider._regainHtmlTextData(url, filePath)
        spider._writeDataToHtmlFile(path, spider.r.text)
        return spider._getHtmlFileData(path)

    #重新采集网页数据并将其转为文本数据，一般用于处理异常
    @staticmethod
    def _regainHtmlTextData(url, filePath):
        spider.errCount += 1
        spider.errNum += 1
        if (spider.errMax < spider.errNum):
            errMax = spider.errNum
        spider.getHtmlTextData(url, filePath)
    
    #从本地文件中读取数据，一般首次爬取会从网上下载网页，接着保存在本地，这样再次爬取直接从本地读数据。
    @staticmethod
    def _getHtmlFileData(FilePath):
        if (os.path.exists(FilePath)):
            size = os.path.getsize(FilePath)
            size = size // 1024
            if(size == 0):
                print('deleting', size, FilePath)
                os.remove(FilePath)
                return False
            if(spider.smallestFileSize > 0 and size > 0):
                if(size < spider.smallestFileSize):
                    print('smallerSize:', size, FilePath)
                    print('smallestFileSize', spider.smallestFileSize)
                    smallestFileSize = size
                    spider.saveCount()
            with open(FilePath, 'r', encoding='utf-8') as f:
                data = f.read()
                f.close()
                return data
        else:
            return False