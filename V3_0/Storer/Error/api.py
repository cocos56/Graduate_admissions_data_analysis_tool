class FileNotExistError(Exception):
	def __str__(self):
		return "文件不存在"
