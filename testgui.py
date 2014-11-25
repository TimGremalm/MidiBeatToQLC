#!/usr/bin/env python
import sys
from PyQt4 import QtGui
from guiMidiBeatToQLC import guiMidiBeatToQLC
from clsQLCInput import QLCInput

QLCInputs = []
avgBpm = 127

def main():
	#Declare inputs
	global QLCInputs
	QLCInputs.append(QLCInput("Takkrona", "http://127.0.0.1:8000/takkrona"))
	QLCInputs.append(QLCInput("Spotlights", "http://127.0.0.1:8000/spotlights"))

	app = QtGui.QApplication([''])
	gui = guiMidiBeatToQLC(QLCInputs, avgBpm)
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()

