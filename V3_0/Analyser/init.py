from V3_0.Storer.api import getDataBasePath, makeDir, deleteDir, deleteFiles
from os.path import join


xlsxRootDirPath = join(getDataBasePath(), 'xlsx_Files')
pklPathList = [
	# storerIns.databasePath + '//step2-01-rawSubjectsInfo.pkl',
	join(getDataBasePath(), 'step2-03-1-infoByInstution.pkl')
	# storerIns.databasePath + '//step2-02-1-sortedByInstutionEnrolledNumber.pkl',
]


def init(reset=False):
	makeDir(xlsxRootDirPath)
	if reset:
		deleteFiles(pklPathList)
		deleteDir(xlsxRootDirPath)
