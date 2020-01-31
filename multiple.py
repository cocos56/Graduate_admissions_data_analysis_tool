# -*- coding : utf-8 -*-
# @Author : Coco
# @Author's GitHub : https://github.com/COCO5666
# @Author's CSND : https://blog.csdn.net/COCO56
# @Author's Webpage : https://coco5666.github.io/
# @IDE: PyCharm
# @Python: Python3.7.2
# @Created Time :2019-02-16 19:50:00
# @Modified Time :2019-02-16 23:58:25
# @File : multiple.py

'''
加速模块
暂时提供多进程加速（注意在使用多进程进行异步运行时不能运行采用单例模式设计的类的方法）
'''

import multiprocessing
import os

def asyncRunFunc(func, paraList, poolNum = None, asyn = True):
    if poolNum == None:
        poolNum = os.cpu_count() // 2
    if (poolNum < 1):
        poolNum = 1
    results = []
    if (asyn):
        pool = multiprocessing.Pool(poolNum)
        for para in paraList:
            #print(para)
            results.append(pool.apply_async(func, (para,)))
        pool.close()
        pool.join()
        data = []
        for res in results:
            data.append(res.get())
    else:
        for para in paraList:
            #print(para)
            results.append(func(para))
        data = results
    return data

def getArgs(*args):
    return args

def getKwArgs(**kwargs):
    print(kwargs)
