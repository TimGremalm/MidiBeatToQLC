#!/usr/bin/python

import sys
import getopt
import pygame
import pygame.midi
from pygame.locals import *

global inputMidiChannel

def about():
	print("MidiBeatToQLC")
	print("=============")
	print("An intreface to grab a beat-signal from MIDI-in and send it to QLC+ through a websocket.")
	print("By Tim Gremalm, tim@gremalm.se, http://tim.gremalm.se")

def main():
	print("main")

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

	main()

