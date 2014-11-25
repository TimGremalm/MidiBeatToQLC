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

		vbox = QtGui.QVBoxLayout()
		vbox.addStretch(1)
		self.setLayout(vbox)

		a = guiQlcInput()
		b = guiQlcInput()
		vbox.addWidget(a)
		vbox.addWidget(b)

		self.show()

class guiQlcInput(QtGui.QWidget):
	def __init__(self):
		super(guiQlcInput, self).__init__()
		self.initUI()

	def initUI(self):
		vbox = QtGui.QVBoxLayout()
		vbox.addStretch(1)
		self.setLayout(vbox)

		fntLabels = QtGui.QFont('Courier New', 16, QtGui.QFont.Light)
		lblAvgBpm = QtGui.QLabel(self)
		lblAvgBpm.setText('BPM: ' + str(0))
		lblAvgBpm.setFont(fntLabels)

		vbox.addWidget(lblAvgBpm)

		hbox = QtGui.QVBoxLayout()
		hbox.addStretch(1)

		btnBeatHalf = QtGui.QPushButton("/ 2")
		btnBeatDouble = QtGui.QPushButton("* 2")
		hbox.addWidget(btnBeatHalf)
		hbox.addWidget(btnBeatDouble)

		vbox.addWidget(hbox)

