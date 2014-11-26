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

		self.fntLabels = QtGui.QFont('Courier New', 20, QtGui.QFont.Bold)

		self.lblAvgBpm = QtGui.QLabel(self)
		self.lblAvgBpm.setText('BPM: ' + str(avgBpm))
		self.lblAvgBpm.setFont(self.fntLabels)

		vbox = QtGui.QVBoxLayout()
		vbox.addStretch(1)
		self.setLayout(vbox)

		a = guiQlcInput()
		b = guiQlcInput()
		vbox.addWidget(self.lblAvgBpm)
		vbox.addWidget(a)
		vbox.addWidget(b)

		self.show()

class guiQlcInput(QtGui.QWidget):
	def __init__(self):
		super(guiQlcInput, self).__init__()
		self.initUI()

	def initUI(self):
		#vbox = QtGui.QVBoxLayout()
		#vbox.addStretch(1)
		#self.setLayout(vbox)
		grid = QtGui.QGridLayout()
		self.setLayout(grid)

		fntLabels = QtGui.QFont('Courier New', 16, QtGui.QFont.Light)

		lblName = QtGui.QLabel(self)
		lblName.setText('Name')
		lblName.setFont(fntLabels)

		lblAvgBpm = QtGui.QLabel(self)
		lblAvgBpm.setText('BPM: ' + str(0))
		lblAvgBpm.setFont(fntLabels)

		lblFactor = QtGui.QLabel(self)
		lblFactor.setText('Factor: ' + str(1))
		lblFactor.setFont(fntLabels)

		btnBeatHalf = QtGui.QPushButton("/ 2")
		btnBeatDouble = QtGui.QPushButton("* 2")

		grid.addWidget(lblName, 0, 0)
		grid.addWidget(lblAvgBpm, 1, 0)
		grid.addWidget(lblFactor, 1, 1)
		grid.addWidget(btnBeatHalf, 2, 0)
		grid.addWidget(btnBeatDouble, 2, 1)

