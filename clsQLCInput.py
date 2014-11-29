#!/usr/bin/env python

class QLCInput:
	Name = ""
	QlcType = ""
	QlcId = ""
	QlcCommand = ""
	NextMS = 0
	PreviousState = 0
	PreviousBeats = []
	SendFactor = 1
	Send = False
	def __init__(self, iName, iQlcType, iQlcId, iQlcCommand):
		self.Name = iName
		self.QlcType = iQlcType
		self.QlcId = iQlcId
		self.QlcCommand = iQlcCommand
		self.PreviousBeats.append(0)

