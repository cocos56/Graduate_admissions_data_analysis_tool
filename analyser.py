# -*- coding : utf-8 -*-
# @Author : Coco
# @Author's GitHub : https://github.com/COCO5666
# @Author's CSND : https://blog.csdn.net/COCO56
# @Author's Webpage : https://coco5666.github.io/
# @IDE: PyCharm
# @Python: Python3.7.2
# @Created Time :2019-02-14 10:16:50
# @Modified Time :2019-02-16 23:58:25
# @File : analyser.py

'''
* 分析器模块
* 为数据分析提供支持
'''

from designPattern import addGetInstanceFunc
from storer import storer
from spider import spider
domain = spider.domain
from selector import selector
import os
import re
from multiple import getArgs
import shutil

storerIns = storer.getInstance()
selectorIns = selector.getInstance()

def findAllWithRe(data, pattern):
    expression = re.compile(pattern)
    res = expression.findall(data)
    return res

@addGetInstanceFunc
class analyser:
    xlsxRootDirPath = storerIns.databasePath + '//xlsx_Files'
    pklPathList = [
        #storerIns.databasePath + '//step2-01-rawSubjectsInfo.pkl',
        storerIns.databasePath + '//step2-03-1-infoByInstution.pkl',
        #storerIns.databasePath + '//step2-02-1-sortedByInstutionEnrolledNumber.pkl',
    ]
    @classmethod
    def Reanalyze(cls, flag):
        if flag:
            for i in cls.pklPathList:
                if(os.path.exists(i)):
                    os.remove(i)
            if(os.path.exists(cls.xlsxRootDirPath)):
                #storerIns.dellAllFiles(cls.xlsxRootDirPath)
                pass

    def __init__(self):
        storerIns.makeDir(self.xlsxRootDirPath)
        pass

    def getRawSubjectInfo(self, subjectsInfo):
        instance = modifyRawSubjeectsInfo.getInstance()
        final = [self.xlsxRootDirPath]
        for subjectInfo in subjectsInfo:
            subjectCodeAndName = subjectInfo[0]
            subjectData = subjectInfo[1:]
            subjectCode = subjectCodeAndName[0]
            subjectName = subjectCodeAndName[1]
            xlsxDirPath = self.xlsxRootDirPath + '//' + subjectCode + '-' + subjectName
            data = instance.getInstitutionInfo(subjectData, xlsxDirPath)
            (xlsxFilePath, sheetName, sheetHead, sheetDatum) = data
            data = tuple(data)
            data = []
            temp = getArgs(xlsxDirPath, xlsxFilePath, sheetName, sheetHead)
            data.append(temp)
            data = data + sheetDatum
            final.append(data)
        return final

    def writeRawSubjectInfoToXlsxFile(self, data):
        xlsxRootDir = data[0]
        subjectsInfo = data[1:]
        storerIns.makeDir(xlsxRootDir)
        for subjectInfo in subjectsInfo:
            head = subjectInfo[0]
            (subjectXlsxDir, xlsxFilePath, sheetName, sheetHead) = head
            storerIns.makeDir(subjectXlsxDir)
            sheetDatum = subjectInfo[1:]
            storerIns.writeDataToXlsxFile(xlsxFilePath, sheetName, sheetHead, sheetDatum)

    def getInfoByInstitution(self, data):
        subjectsInfo = data[1:]
        insDic = {}
        for subjectInfo in subjectsInfo:
            head = subjectInfo[0]
            (subjectXlsxDir, xlsxFilePath, sheetName, sheetHead) = head
            xlsxFilePath = subjectXlsxDir + '//sortedByNumber.xlsx'
            sheetName = 'byEnrolledNumber'
            datum = subjectInfo[1:]
            subjectName = subjectXlsxDir.replace('D:\pycharm\YZSpider\Database//xlsx_Files//', '')
            instance = getInfoByInstitution.getInstance()
            dic = instance.getSubjectInfo(subjectName, datum)
            for key in dic:
                if key in insDic:
                    insDic[key] = insDic[key]+dic[key]
                else:
                    insDic.update({key:dic[key]})
        return insDic

@addGetInstanceFunc
class modifyRawSubjeectsInfo:
    def __init__(self):
        pass
    def getInstitutionInfo(self, subjectData, xlsxDirPath):
        xlsxFilePath = xlsxDirPath + '//rawInfo.xlsx'
        sheetName = 'rawInfo'
        sheetHead = [
            '机构名', '院系所', '专业',
            '研究方向', '考试方式', '学习方式',
            '指导教师', '拟招生人数', '考试范围',
            '政治', '外语', '业务课一',
            '业务课二', '跨专业', '备注'
        ]
        sheetDatum = []
        for insInfo in subjectData:
            insHead = insInfo[0]
            insCodeAndName = [insHead[0] + '-' + insHead[1]]
            insUrl = insHead[2]
            insData = insInfo[1:]
            sheetDatum = sheetDatum + self.getResearchInfo(insCodeAndName, insData, insUrl)
        data = getArgs(xlsxFilePath, sheetName, sheetHead, sheetDatum)
        return data

    def getResearchInfo(self, insCodeAndName, insData, insUrl):
        data = []
        for researchData in insData:
            researchInfo = []
            temp = getArgs(insCodeAndName[0], insUrl)
            researchInfo.append(temp)
            researchInfo = researchInfo + researchData
            temp = researchInfo.pop(1)
            researchInfo.insert(4, temp)
            temp = researchInfo.pop(8)
            temp = domain + '/zsml/kskm.jsp?id=' + temp
            researchInfo.insert(8, getArgs('点此查看', temp))
            temp = researchInfo.pop()
            scope = self.getScope(temp, researchInfo, researchData, insUrl)
            cntList = [i for i in range(0, 4)]
            for cnt in cntList:
                researchInfo.insert(9, scope.pop())
            data.append(researchInfo)
        return data

    def getScope(self, data, researchInfo, researchData, insUrl):
        scope_head = data[0]
        b = scope_head == ['政治', '外语', '业务课一', '业务课二']
        if (not b):
            print(scope_head)
            print(data)
            print(researchInfo)
            print(researchData)
            print(insUrl)
            print("not ['政治', '外语', '业务课一', '业务课二']")
            exit(0)
        scope_data = data[1:]
        scope_data_final = []
        cntList = [i for i in range(0, 4)]
        li = []
        for cnt in cntList:
            li.append([])
        (first, second, third, fourth) = li
        for i in scope_data:
            for cnt in cntList:
                (t, con) = (i[cnt], li[cnt])
                t = list(t)
                pattern = r'\((\d+)\)(.+)'
                try:
                    codeAndName = list(findAllWithRe(t[0], pattern)[0])
                except IndexError:
                    err = ['(-)无', '(--)无']
                    if t[0] in err:
                        codeAndName = ['-1' ,'无']
                    else:
                        print(t)
                        exit(-1)
                t = codeAndName + t[1:]
                t = tuple(t)
                if not t in con:
                    li[cnt].append(t)
        li = self._modifyScope(li)
        return li

    def _modifyScope(self, li):
        data = []
        for l in li:
            f = False
            temp = ''
            for i in l:
                if(f):
                    temp = temp + '\n或:\n'
                i = i[0] + '-' + i[1] + '：' + i[2]
                i = temp + i
                temp = i
                f = True
            data.append(temp)
        return data

@addGetInstanceFunc
class getInfoByInstitution:
    def __init__(self):
        pass

    def getSubjectInfo(self, subjectName, datum):
        dic = {}
        for data in datum:
            (
                insName, department, major, researchArea, examType, learngType, teacher, enrolledNumer,
                scopeUrl, course1, course2, course3, course4, crossMajor, remark
             ) = data
            # 'http://yz.chsi.com.cn/zsml/querySchAction.do?dwmc=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6&yjxkdm=0101'
            # examTypeLi = ['统考', '单考']
            # #examTypes = ['(不含推免)']
            # enrolledNumerTypes = ['一级学科：', '专业：', '研究方向：', '院系所：']
            (department, major, researchArea) = self._modifyData(department, major, researchArea)
            insName = insName[0]
            data = getArgs(insName, department, subjectName,
                           major, researchArea, examType, learngType, enrolledNumer
                           )
            value = getArgs(
                department, subjectName, major,researchArea, examType, learngType, enrolledNumer
            )
            if(not insName in dic):
                dic.update({insName: [value]})
            else:
                dic[insName] = dic[insName] +[value]
        return dic


    def _modifyData(self, department, major, researchArea):
        data = getArgs(department, major, researchArea)
        temp = []
        for i in data:
            try:
                tup = findAllWithRe(i, '\((.+)\)(.+)')[0]
                temp.append(tup[0] + '-' + tup[1])
            except IndexError:
                print(i)
                exit(-1)
        return temp

    # def _getEnrolledNumber(self, data):
    #     print(data)
    #     (insName, department, subjectName, major, researchArea, examType, learngType, enrolledNumer) = data
    #     if(not enrolledNumer.find('一级学科：') = -1)
    #     exit(0)