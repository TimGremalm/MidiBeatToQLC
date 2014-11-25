#!/usr/bin/env python
from PyQt4 import QtGui

class guiMidiBeatToQLC(QtGui.QWidget):
	def __init__(self):
		super(guiMidiBeatToQLC, self).__init__()
		self.initUI()

	def initUI(self):
		self.resize(250, 650)
		self.setWindowTitle('MidiBeatToQLC')
		self.setWindowIcon(QtGui.QIcon('midi.ico'))
		self.show()

#class guiStatus(QtGui.QWidget):
#	def __init__(self):
#		super(guiStatus, self).__init__()
#		self.initUI()
#
#	def initUI(self):
