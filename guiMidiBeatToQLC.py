#!/usr/bin/env python
from PyQt4 import QtCore
from PyQt4 import QtGui
import time

class guiMidiBeatToQLC(QtGui.QWidget):
	inputsQlc = []
	guiInputsQlc = []
	avgBpm = []

	def __init__(self, iinputsQlc, iavgBpm):
		super(guiMidiBeatToQLC, self).__init__()
		self.inputsQlc = iinputsQlc
		self.avgBpm = iavgBpm
		self.initUI()

	def initUI(self):
		self.resize(250, 650)
		self.setWindowTitle('MidiBeatToQLC')
		self.setWindowIcon(QtGui.QIcon('midi.ico'))
		self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

		self.fntLabels = QtGui.QFont('Courier New', 20, QtGui.QFont.Bold)

		self.lblAvgBpm = QtGui.QLabel(self)
		self.lblAvgBpm.setText('BPM: ' + str(self.avgBpm[0]))
		self.lblAvgBpm.setFont(self.fntLabels)

		vbox = QtGui.QVBoxLayout()
		vbox.addStretch(1)
		self.setLayout(vbox)

		vbox.addWidget(self.lblAvgBpm)
		for input in self.inputsQlc:
			temp = guiQlcInput(input)
			vbox.addWidget(temp)
			self.guiInputsQlc.append(temp)

		self.timerAvgBpm = QtCore.QTimer()
		self.timerAvgBpm.timeout.connect(self.lblAvgBpm_Timer)
		self.timerAvgBpm.start(500)

		self.show()

	def lblAvgBpm_Timer(self):
		self.lblAvgBpm.setText("BPM: " + str(round(self.avgBpm[0],1)))
		for i in self.guiInputsQlc:
			bpm = self.avgBpm[0] * i.inputQlc.SendFactor
			i.lblAvgBpm.setText("BPM: " + str(round(bpm,1)))

class guiQlcInput(QtGui.QWidget):
	def __init__(self, iinputQlc):
		self.inputQlc = iinputQlc
		super(guiQlcInput, self).__init__()
		self.initUI()

	def initUI(self):
		grid = QtGui.QGridLayout()
		self.setLayout(grid)

		fntLabels = QtGui.QFont('Courier New', 16, QtGui.QFont.Light)

		lblName = QtGui.QLabel(self)
		lblName.setText(self.inputQlc.Name)
		lblName.setFont(fntLabels)

		self.lblAvgBpm = QtGui.QLabel(self)
		self.lblAvgBpm.setText('BPM: ' + str(0))
		self.lblAvgBpm.setFont(fntLabels)

		self.lblFactor = QtGui.QLabel(self)
		self.lblFactor.setText('Factor: ' + str(1))
		self.lblFactor.setFont(fntLabels)

		btnBeatHalf = QtGui.QPushButton("/ 2")
		btnBeatHalf.clicked.connect(self.btnBeatHalf_OnClicked)
		btnBeatDouble = QtGui.QPushButton("* 2")
		btnBeatDouble.clicked.connect(self.btnBeatDouble_OnClicked)

		chkSend = QtGui.QCheckBox('Send', self)
		chkSend.stateChanged.connect(self.chkSend_Checked)

		grid.addWidget(lblName, 0, 0)
		grid.addWidget(chkSend, 1, 0)
		grid.addWidget(self.lblAvgBpm, 2, 0)
		grid.addWidget(self.lblFactor, 2, 1)
		grid.addWidget(btnBeatHalf, 3, 0)
		grid.addWidget(btnBeatDouble, 3, 1)

	def btnBeatHalf_OnClicked(self):
		self.inputQlc.SendFactor = self.inputQlc.SendFactor / float(2)
		self.lblFactor.setText("Factor: " + str(self.inputQlc.SendFactor))

	def btnBeatDouble_OnClicked(self):
		self.inputQlc.SendFactor = self.inputQlc.SendFactor * float(2)
		self.lblFactor.setText("Factor: " + str(self.inputQlc.SendFactor))

	def chkSend_Checked(self, state):
		if state == QtCore.Qt.Checked:
			self.inputQlc.Send = True
		else:
			self.inputQlc.Send = False

