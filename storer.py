# -*- coding : utf-8 -*-
# @Author : Coco
# @Author's GitHub : https://github.com/COCO5666
# @Author's CSND : https://blog.csdn.net/COCO56
# @Author's Webpage : https://coco5666.github.io/
# @IDE: PyCharm
# @Python: Python3.7.2
# @Created Time :2019-02-16 20:32:20
# @Modified Time :2019-02-16 23:58:25
# @File : storer.py

'''
* 存储器模块
* 为存储与读取数据提供支持
'''

from designPattern import singleton
import os
import json
import pickle
import xlsxwriter

#通过designPattern.singleton装饰器来实现单例模式，具体为新建类的_instance属性，重写new方法，并对外提供getInstance接口
@singleton  #此处等于selector = singleton(selector)
class storer:
    '''
    本类用于写入数据到硬盘/从硬盘读取数据
	本类采用单例模式（通过重写new方法，并对外提供getInstance接口）
    '''
    
    def __init__(self):
        self.databasePath = self.getDataBasePath()

    #获取名为“Database”的文件夹所在的目录
    def getDataBasePath(self):
        '''
        获取名为“Database”的文件夹所在的目录，
        存在的话立即返回目录所在路径，
        不存在的话创建目录后再返回路径
        '''
        path = os.getcwd() + '\\Database'
        if(os.path.exists(path)):
            return path
        else:
            os.mkdir(path)
            return path

    def makeDir(self, path):
        if not os.path.exists(path):
            os.mkdir(path)
        return path

    def writeStringDataToJsonFile(self, data, filePath):
        data = json.loads(data)
        with open(filePath, 'w') as f:
            json.dump(data, f)
            f.close()
        pass

    def getJsonFileData(self, filePath):
        with open(filePath, 'r') as f:
            data = json.load(f)
            f.close()
        #返回数据
        return data

    def getPickleFileData(self, pickleFilePath):
        '''
        :param pickleFilePath:
            self, pickleFilePath
        :return:
        '''
        if (os.path.exists(pickleFilePath)):
            with open(pickleFilePath, 'rb') as f:
                data = pickle.load(f)
                f.close()
                return data
        else:
            return False

    def writeDataToPickleFile(self, pickleFilePath, data):
        with open(pickleFilePath, 'wb') as f:
            pickle.dump(data, f)
            f.close()

    def getPickleFileDataFromJsonFile(self, pickleFilePath, func, jsonFilePath):
        '''
        获取Pickle文件数据
        '''
        #本地存在
        data = self.getPickleFileData(pickleFilePath)
        #本地不存在
        if data == False:
            data = storer.getInstance().getJsonFileData(jsonFilePath)
            data = func(data)
            self.writeDataToPickleFile(pickleFilePath, data)
        #返回数据
        return data

    def getPickleFileDataFromOtherData(self, pickleFilePath, func, OtherData):
        # 本地存在
        data = self.getPickleFileData(pickleFilePath)
        # 本地不存在
        if data == False:
            data = func(OtherData)
            self.writeDataToPickleFile(pickleFilePath, data)
        # 返回数据
        return data

    def dellAllFiles(self, dirPath):
        ls = os.listdir(dirPath)
        for i in ls:
            file_path = os.path.join(dirPath, i)
            if os.path.isdir(file_path):
                self.dellAllFiles(file_path)
            else:
                os.remove(file_path)

    def writeDataToXlsxFile(self, xlsxFilePath, sheetName, sheetHead, sheetDatum):
        if os.path.exists(xlsxFilePath):
            return
        workbook = xlsxwriter.Workbook(xlsxFilePath)
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
        sizeLi = self._getColumnsSize(sheetHead, oldSizeList = None, factor = 1.75)
        r = 1
        format = workbook.add_format(
            {
                'text_wrap' : True,
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
                if(type(i) == tuple):
                    ws.write_url(r, c, i[1], urlFormat, string = i[0])
                else:
                    ws.write(r, c, i, format)
                c += 1
            r += 1
            sizeLi = self._getColumnsSize(data, oldSizeList=sizeLi, factor=1)
        self._setColumnsSize(ws, sizeLi)
        workbook.close()

    def _setColumnsSize(self, worksheet, sizeList):
        cnt = 0
        for size in sizeList:
            worksheet.set_column(cnt, cnt, size)
            cnt += 1

    def _getColumnsSize(self, rowsData, oldSizeList = None, factor=1):
        #print(rowsData)
        li = []
        for i in rowsData:
            if (type(i) == tuple):
                str = i[0]
            else:
                str = i
            size = self._getColumnSize(str) * factor
            li.append(size)
        if(not oldSizeList == None):
            len1 = len(li)
            len2 = len(oldSizeList)
            if not len1 == len2:
                print('not len1 == len2:')
                exit(-1)
            cntLi = [i for i in range(len1)]
            li2 = []
            for cnt in cntLi:
                if(oldSizeList[cnt]>=56):
                    li2.append(56)
                    continue
                if(li[cnt]>oldSizeList[cnt]):
                    max = li[cnt]
                else:
                    max = oldSizeList[cnt]
                li2.append(max)
            li = li2
        return li

    def _getColumnSize(self, str):
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
        #9是制表符，10是回车，183：·，252：ü
        enSymbol = [9, 10, 183, 252]
        size = 0
        for c in str:
            o = ord(c)
            # 中文汉字：'\u4e00'到'\u9fa5'
            if (40869 >= o >= 19968) or (o in chSymbol) or (o > 900):
                size += 2
            # 32为空格
            elif (126 >= o >= 32)or (o in enSymbol):
                size += 1
            else:
                for c in str:
                    print('c=', c, 'o=', ord(c))
                print('str=', str)
                print('c=', chr(o), 'o=', o)
                exit(-1)
        return size
        pass
