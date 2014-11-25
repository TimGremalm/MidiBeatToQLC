#!/usr/bin/env python
from PyQt4 import QtCore
from PyQt4 import QtGui

class guiMidiBeatToQLC(QtGui.QWidget):
	inputsQlc = []
	avgBpm = 0

	def __init__(self, iinputsQlc, iavgBpm):
		global inputsQlc
		global avgBpm

		super(guiMidiBeatToQLC, self).__init__()
		inputsQlc = iinputsQlc
		avgBpm = iavgBpm
		self.initUI()

	def initUI(self):
		self.resize(250, 650)
		self.setWindowTitle('MidiBeatToQLC')
		self.setWindowIcon(QtGui.QIcon('midi.ico'))

		self.fntLabels = QtGui.QFont('Courier New', 16, QtGui.QFont.Light)

		self.lblAvgBpm = QtGui.QLabel(self)
		self.lblAvgBpm.setText('BPM: ' + str(avgBpm))
		self.lblAvgBpm.setFont(self.fntLabels)

		self.show()

#class guiStatus(QtGui.QWidget):
#	def __init__(self):
#		super(guiStatus, self).__init__()
#		self.initUI()
#
#	def initUI(self):
