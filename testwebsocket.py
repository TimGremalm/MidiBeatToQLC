#!/usr/bin/env python

#from websocket import create_connection

#http://127.0.0.1:9999/qlcplusWS
#var url = 'ws://' + window.location.host + '/qlcplusWS';

#Button
#	websocket.send(id + "|" + obj.value);

#VCCueList
#	websocket.send(id + "|" + cmd);

import time
import websocket

ws = websocket.create_connection("ws://127.0.0.1:9999/qlcplusWS")


for i in range(0,10):
	ws.send("0|1")
	time.sleep(0.3)
	#result =  ws.recv()
	#print "Received '%s'" % result

	ws.send("0|0")
	time.sleep(0.3)

ws.close()


