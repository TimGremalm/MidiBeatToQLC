#!/usr/bin/python

import sys
import getopt
import threading
import time
import pygame
import pygame.midi
from pygame.locals import *

inputMidiChannel = 1
channelMidi = 5
noteMidi = 0
lastBeat = 0
QLCInputs = []
threadList = []
shutdown = False

def about():
	print("MidiBeatToQLC")
	print("=============")
	print("An intreface to grab a beat-signal from MIDI-in and send it to QLC+ through a websocket.")
	print("By Tim Gremalm, tim@gremalm.se, http://tim.gremalm.se")

def main():
	print("main")

	#Declare inputs
	global QLCInputs
	QLCInputs.append(QLCInput("Takkrona", "http://127.0.0.1:8000/takkrona"))
	QLCInputs.append(QLCInput("Spotlights", "http://127.0.0.1:8000/spotlights"))

	initMidi()

	global threadList
	t = threading.Thread(target=receiveMidi, args=())
	t.start()
	threadList.append(t)

	unloadMidi()

def receiveMidi():
	global QLCInputs

	for input in QLCInputs:
		input.NextMS += 1

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

def initMidi():
	pygame.init()
	pygame.midi.init()

def unloadMidi():
	pygame.midi.quit()

def printDeviceInfo():
	for i in range( pygame.midi.get_count() ):
		r = pygame.midi.get_device_info(i)
		(interf, name, input, output, opened) = r
		in_out = ""
		if input:
			in_out = "(input)"
		if output:
			in_out = "(output)"
		print ("%2i: interface :%s:, name :%s:, opened :%s: %s" %
		(i, interf, name, opened, in_out))

def aboutAndUsage():
	about()
	usage()

def usage():
	print ("--help : shows this help")
	print ("--list : list available midi devices")
	print ("--input [device_id] : Midi-device to receive from")

if __name__ == '__main__':
	#Parse arguments
	if len(sys.argv) == 1:
		aboutAndUsage()
		sys.exit(1)

	try:
		opts, args = getopt.getopt(sys.argv[1:],"hli:",["help", "list", "input="])
	except getopt.GetoptError as err:
		print(err)
		usage()
		sys.exit(2)

	inputMidiChannel = 0
	for o, a in opts:
		if o in ("-h", "--help"):
			aboutAndUsage()
			sys.exit(0)
		elif o in ("-l", "--list"):
			initMidi()
			printDeviceInfo()
			unloadMidi()
			sys.exit(0)
		elif o in ("-i", "--input"):
			try:
				inputMidiChannel = int(a)
			except ValueError:
				print("Input \""+a+"\" is not a valid integer, use --list to see input-MIDI-channels.")
				usage()
				sys.exit(3)
		else:
			assert False, "unhandled option"

	#Call main-function
	main()

