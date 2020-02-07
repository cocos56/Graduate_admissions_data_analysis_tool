# -*- coding: utf-8 -*-
# @Author : Coco
# @About author: https://coco56.gitee.io/blog/about/
# @IDE: PyCharm
# @Python: Python3.8.1
# @Created Time :2020/2/7 23:08
# @File : pkl.py

"""
"""

import pickle


def writeDataToFile(filePath, text):
	# print(filePath, text)
	# 为了方便，避免忘记close掉这个文件对象，可以用下面这种方式替代
	with open(filePath, "w", encoding="utf-8") as f:  # 设置文件对象
		f.write(text)
		f.close()


def writeDataToPickleFile(pickleFilePath, data):
	with open(pickleFilePath, 'wb') as f:
		pickle.dump(data, f)
		f.close()
