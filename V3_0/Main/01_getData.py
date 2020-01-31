import os
from V3_0.Storer.GetData.api import getPickleFileData
from V3_0.Storer.Config.api import getDataBasePath
from V3_0.Storer.Del.api import deleteFile

pklPath = os.path.join(getDataBasePath(), 'step1-02-SubjectsURL.pkl')
deleteFile(pklPath)
data = getPickleFileData(pklPath)
# print(data)
# for i in data:
# 	print(i, data[i])

