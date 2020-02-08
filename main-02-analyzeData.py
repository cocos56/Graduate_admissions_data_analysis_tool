"""
* 程序入口模块二
* 为打开/启动程序以及调用执行相关库函数提供支持
* 具体的，启动后开始进行第二阶段的数据分析工作
"""

from analyser import analyser
from os.path import join, exists
from V3_0.Storer.api import getDataBasePath, getPickleFileData, getPickleFileDataFromOtherData
from V3_0.Analyser.api import init, initRawData

if __name__ == '__main__':
    #获取所有需要用到的单例
    analyserIns = analyser.getInstance()

    # 判断是否需要重新筛选数据
    reset = True
    reset = False

    #####################################
    #第二阶段：数据分析阶段
    #####################################
    ###第01步：获取所有学科的招生信息
    pklPath = join(getDataBasePath(), 'step2-01-rawSubjectsInfo.pkl')
    init(reset)
    if exists(pklPath):
        SubjectsInfo = None
    else:
        pklPath2 = join(getDataBasePath(), 'step1-04-SubjectsInfo.pkl')
        SubjectsInfo = getPickleFileData(pklPath2)

    # ###第02步：逐一将将每一个学科的招生原始数据保存成名为'rawInfo.xlsx'工作簿文件中的一张名为'rawInfo'工作表
    # 先把数据从step2-01-rawSubjectsInfo.pkl中读取出来
    # step2-01-rawSubjectsInfo.pkl是在step1-04-SubjectsInfo.pkl的基础上做了一些调整
    pklPath = join(getDataBasePath(), 'step2-01-rawSubjectsInfo.pkl')
    rawData = getPickleFileDataFromOtherData(
        pklPath, analyserIns.getRawSubjectInfo, SubjectsInfo
    )
    # 写入到Excel文件中
    analyserIns.writeRawSubjectInfoToXlsxFile(rawData)
    initRawData(rawData)

    ###第03步：把所有学科下的所有学校的招生数量按从高到低排列，
    ###         并将数据保存在'sortedByNumber.xlsx'工作簿文件中的一张名为'byEnrolledNumber'的工作表
    ## 第一小步：以招生机构（研究所或学校）为单位，合并所有学科的信息到学校下面
    # rawData = None
    # join(getDataBasePath(), 'step2-03-1-infoByInstution.pkl')
    # data = getPickleFileDataFromOtherData(
    #     pklPath, analyserIns.getInfoByInstitution, rawData)
    # print(len(data))
    # pklPath = join(getDataBasePath(), 'step2-03-1-sortedByInstutionEnrolledNumber.pkl')
    # data = getPickleFileDataFromOtherData(
    #     pklPath, analyserIns.getDataThatSortedByInstutionEnrolledNumber, rawData)
    # analyserIns.writeRawSubjectInfoToXlsxFile(rawData)
