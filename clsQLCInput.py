#!/usr/bin/env python

class QLCInput:
	Name = ""
	QLCAddress = ""
	NextMS = 0
	PreviousBeats = []
	SendFactor = 1
	Send = False
	def __init__(self, iName, iQLCAddress):
		self.Name = iName
		self.QLCAddress = iQLCAddress

