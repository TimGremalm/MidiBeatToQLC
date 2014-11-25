#!/usr/bin/env python
import sys
from PyQt4 import QtGui
from guiMidiBeatToQLC import guiMidiBeatToQLC

def main():
	app = QtGui.QApplication([''])
	gui = guiMidiBeatToQLC()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()

