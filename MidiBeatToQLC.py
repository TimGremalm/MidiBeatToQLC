#!/usr/bin/env python

import sys
import getopt
import threading
import time
import pygame
import pygame.midi
import pygame.time
from pygame.locals import *

inputMidiDevice = 1
midiTickStatus = 248
midiTickViceId = 1
midiTickCounter = 0
avgBpm = 0
lastMidiBeat = 0
lastMidiBeats = []
lastMidiBeatDeltas = []
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

	global threadList
	t = threading.Thread(target=receiveMidi, args=())
	t.start()
	threadList.append(t)

	t = threading.Thread(target=calculateBeats, args=())
	t.start()
	threadList.append(t)

	waitForExit()
	print("Threads is closed, terminating self.")
	sys.exit(0)

def receiveMidi():
	initMidi()

	global lastMidiBeats
	global midiTickCounter

	pygame.init()
	pygame.fastevent.init()
	event_get = pygame.fastevent.get
	event_post = pygame.fastevent.post

	i = pygame.midi.Input(inputMidiDevice)

	#250 MIDI Clock Start
	#252 MIDI Clock Stop
	#248 MIDI Clock Tick
	while shutdown == False:
		events = event_get()
		for e in events:
			if e.type in [QUIT]:
				going = False
			if e.type in [KEYDOWN]:
				going = False
			if e.type in [pygame.midi.MIDIIN]:
				#Uncommend to see all MIDI-messages
				#print (e)
				#print(str(pygame.time.get_ticks()))
				if e.status == midiTickStatus and e.vice_id == midiTickViceId:
					midiTickCounter += 1

					#24 MIDI Clock-Ticks per Beat
					if midiTickCounter >= 24:
						lastMidiBeats.append(e.timestamp)
						#Only hold 10 latest beats
						if len(lastMidiBeats) > 10:
							lastMidiBeats.pop(0)
						print("Beat! " + str(lastMidiBeats[-1]))
						midiTickCounter = 0
		if i.poll():
			midi_events = i.read(10)
			# convert them into pygame events.
			midi_evs = pygame.midi.midis2events(midi_events, i.device_id)
			for m_e in midi_evs:
				event_post( m_e )
	del i

	unloadMidi()

def calculateBeats():
	global lastMidiBeat
	global lastMidiBeats
	global avgBpm
	while shutdown == False:
		if len(lastMidiBeats) > 1:
			if lastMidiBeat != lastMidiBeats[-1]:
				#Calculate instant values
				deltaBeatMs = lastMidiBeats[-1] - lastMidiBeats[-2]
				lastMidiBeat = lastMidiBeats[-1]
				#bpm = 60/(deltaBeatMs / float(1000))

				#Add delta to list
				lastMidiBeatDeltas.append(deltaBeatMs)
				if len(lastMidiBeatDeltas) > 10:
					lastMidiBeatDeltas.pop(0)

				#Calculate mean values
				avgDeltaBeatMs = sum(lastMidiBeatDeltas)/float(len(lastMidiBeatDeltas))
				avgBpm = 60/(avgDeltaBeatMs / float(1000))

				print(" "+str(round(avgBpm, 0)))
				for input in QLCInputs:
					nextDeltaBeatMS = avgDeltaBeatMs/float(input.SendFactor)
					input.NextMS = lastMidiBeats[-1] + nextDeltaBeatMS
					#print("nextms:" + str(input.NextMS) + " lastbeatms:" + str(lastMidiBeats[-1]) + " deltams:" + str(avgDeltaBeatMs))

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

def waitForExit():
	print("Write exit to exit")
	while (raw_input("") != "exit"):
		print("Write exit to exit")

	global shutdown
	shutdown = True
	print("Key pressed, waiting for threads to close.")

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

	pygame.init()

	inputMidiDevice = 0
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
				inputMidiDevice = int(a)
			except ValueError:
				print("Input \""+a+"\" is not a valid integer, use --list to see input-MIDI-channels.")
				usage()
				sys.exit(3)
		else:
			assert False, "unhandled option"

	#Call main-function
	main()

