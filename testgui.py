#!/usr/bin/env python
import sys
from PyQt4 import QtGui
from guiMidiBeatToQLC import guiMidiBeatToQLC
from clsQLCInput import QLCInput
import threading
import time

QLCInputs = []
avgBpm = 127
shutdown = False

def main():
	#Declare inputs
	global QLCInputs
	QLCInputs.append(QLCInput("Takkrona", "http://127.0.0.1:8000/takkrona"))
	QLCInputs.append(QLCInput("Spotlights", "http://127.0.0.1:8000/spotlights"))

	t = threading.Thread(target=incAvgBpm, args=())
	t.start()

	app = QtGui.QApplication([''])
	gui = guiMidiBeatToQLC(QLCInputs, avgBpm)

	app.exec_()

	global shutdown
	shutdown = True

	sys.exit(0)

def incAvgBpm():
	while shutdown == False:
		global avgBpm
		avgBpm += 1
		print(str(avgBpm))

		for input in QLCInputs:
			print(input.Name + " " + str(input.SendFactor))

		time.sleep(1)

if __name__ == '__main__':
	main()

