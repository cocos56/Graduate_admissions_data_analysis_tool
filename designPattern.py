# -*- coding : utf-8 -*-
# @Author : Coco
# @Author's GitHub : https://github.com/COCO5666
# @Author's CSND : https://blog.csdn.net/COCO56
# @Author's Webpage : https://coco5666.github.io/
# @IDE: PyCharm
# @Python: Python3.7.2
# @Created Time :2019-02-16 11:05:18
# @Modified Time :2019-02-16 23:58:25
# @File : designPattern.py

'''
* 设计模式模块
* 为类的设计模式（如单例模式）提供支持
* 具体的，我们暂时提供了单例模式的装饰器与仅添加添加获取单例方法的装饰器（未重新new方法）
'''

def singleton(obj):

    #类属性
    obj._instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            return cls._instance
        else:
            cls._instance = object.__new__(cls, *args, **kwargs)
            cls._instance.__init__()
            # print('object=')
            # print(object)
            # print('cls=')
            # print(cls)
            return cls._instance
    obj.__new__ = __new__
    
    #对外提供getInstance接口
    @classmethod
    def getInstance(cls, *args, **kwargs):
        '''
        获取单例
        '''
        if obj._instance:
            return obj._instance
        else:
            return obj.__new__(cls)
    obj.getInstance = getInstance

    return obj


# 添加获取单例的装饰器，未重写类的__new__方法，意味着可以使用new方法获取多个实例
# 对外提供getInstance接口,推荐在不是必要的情况下使用这个方法获取单例
# 使用这个装饰器主要是增加对多进程的支持（使用单例模式装饰器装饰的类无法支持多进程）
def addGetInstanceFunc(obj):
    # 类属性
    obj._instance = None

    # 对外提供getInstance接口
    @classmethod
    def getInstance(cls, *args, **kwargs):
        '''
        获取单例
        '''
        if not obj._instance:
            obj._instance = obj.__new__(cls)
            obj._instance.__init__()
        return obj._instance

    obj.getInstance = getInstance

    return obj