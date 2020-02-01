class FileNotExistError(Exception):
	def __str__(self):
		return "文件不存在"


class FileSizeIsZeroError(Exception):
	def __str__(self):
		return "文件大小为0"