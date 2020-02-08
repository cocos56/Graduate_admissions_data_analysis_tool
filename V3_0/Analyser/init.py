from V3_0.Storer.api import getDataBasePath, getExcelRootPath, makeDir, deleteDir, deleteFiles
from os.path import join

filesPath = [
	join(getDataBasePath(), 'step2-01-rawSubjectsInfo.pkl'),
	join(getDataBasePath(), 'step2-03-1-infoByInstution.pkl'),
	join(getDataBasePath(), 'step2-02-1-sortedByInstutionEnrolledNumber.pkl')
]


def init(reset=False):
	if reset:
		deleteFiles(filesPath)
		deleteDir(getExcelRootPath())
	makeDir(getExcelRootPath())
