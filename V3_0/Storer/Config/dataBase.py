from V3_0.Setting.api import dbPath
from ..Make.api import makeDir
from os.path import join


def getDataBasePath(): return makeDir(dbPath)


def getExcelRootPath(): return join(getDataBasePath(), 'ExcelFiles')
