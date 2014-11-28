#!/usr/bin/env python
import sys
from PyQt4 import QtGui
from guiMidiBeatToQLC import guiMidiBeatToQLC
from clsQLCInput import QLCInput
import threading
import time

QLCInputs = []
avgBpm = []
shutdown = False
app = 0

def main():
	#Declare inputs
	global QLCInputs
	global avgBpm
	QLCInputs.append(QLCInput("Takkrona", "http://127.0.0.1:8000/takkrona"))
	QLCInputs.append(QLCInput("Spotlights", "http://127.0.0.1:8000/spotlights"))

	avgBpm.append(127)
	print(str(avgBpm[0]))

	t = threading.Thread(target=incAvgBpm, args=())
	t.start()

	global app
	app = QtGui.QApplication([''])
	gui = guiMidiBeatToQLC(QLCInputs, avgBpm)

	app.exec_()

	global shutdown
	shutdown = True

	sys.exit(0)

def incAvgBpm():
	while shutdown == False:
		global avgBpm
		avgBpm[0] += 1
		print(str(avgBpm[0]))

		for input in QLCInputs:
			print(input.Name + " " + str(input.SendFactor) + " " + str(input.Send))

		time.sleep(1)

if __name__ == '__main__':
	main()

