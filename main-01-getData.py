# -*- coding : utf-8 -*-
# @Author : Coco
# @Author's GitHub : https://github.com/COCO5666
# @Author's CSND : https://blog.csdn.net/COCO56
# @Author's Webpage : https://coco5666.github.io/
# @IDE: PyCharm
# @Python: Python3.7.2
# @Created Time :2019-02-16 22:52:36
# @Modified Time :2019-02-16 23:58:25
# @File : main-01-getData.py

'''
* 程序入口模块一
* 为打开/启动程序以及调用执行相关库函数提供支持
* 具体的，启动后开始进行第一阶段的数据采集工作
'''

from storer import storer
from spider import spider
from selector import selector
import os

if __name__ == '__main__':
    #获取所有需要用到的单例
    storerIns = storer.getInstance()
    selectorIns = selector.getInstance()

    #初始化全局变量
    databasePath = storerIns.getDataBasePath()

    #判断是否需要重新筛选数据
    reSelectFlag = False
    subjectsInfoPklPath = databasePath + '\\step1-04-SubjectsInfo.pkl'
    selectorIns.reSelect(reSelectFlag, subjectsInfoPklPath)


    #####################################
    #第一阶段：数据采集阶段
    #####################################
    ###第01步：获取学科类别代码
    #(原始的json数据)
    #getRawSubjectsCode
    # 设置文件存放路径
    jsonPath = databasePath + '\\step1-01-1-RawSubjectsCode.json'
    jsonURL = 'https://yz.chsi.com.cn/zsml/pages/getZy.jsp'
    # 本地存在所需的Json文件，打开文件读取并返回数据
    if(os.path.exists(jsonPath)):
        data = storerIns.getJsonFileData(jsonPath)
    # 本地不存在所需的Json文件，访问URL获取数据，然后将数据保存在本地后返回数据
    else:
        jsonHtmlPath = databasePath + '\\step1-01-1-RawSubjectsCode'
        data = spider.getHtmlTextData(jsonURL, jsonHtmlPath)
        storerIns.writeStringDataToJsonFile(data, jsonPath)


    #(Python数据类型)
    #getSubjectsCode
    pklPath = databasePath + '\\step1-01-2-SubjectsCode.pkl'
    data = storerIns.getPickleFileDataFromJsonFile(
        pklPath, selectorIns.getSubjectsCode, jsonPath)
    # print(data)
    # print(len(data))
    ###第02步：获取所有学科类别的URL
    # 设置文件存放路径
    pklPath = databasePath + '\\step1-02-SubjectsURL.pkl'
    data = storerIns.getPickleFileDataFromOtherData(pklPath, selectorIns.getSubjectsURLs, data)
    #print(data)
    ###第03步：逐一获取每一个学科类别的所有机构名
    pklPath = databasePath + '\\step1-03-SubjectsInstitutions.pkl'
    data = storerIns.getPickleFileDataFromOtherData(pklPath, selectorIns.getInstitutionsName, data)
    ###第04步：获取所有学科的招生信息
    pklPath = subjectsInfoPklPath
    data = storerIns.getPickleFileDataFromOtherData(pklPath, selectorIns.getAllSCInfo, data)
    ###第05步：数据采集完毕
    print('数据采集完毕')