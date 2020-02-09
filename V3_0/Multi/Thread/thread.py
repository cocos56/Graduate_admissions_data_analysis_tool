import threading

threadLock = threading.Lock()


def runThread(functionName, interval=0):
	t = threading.Timer(interval, functionName)
	t.start()
