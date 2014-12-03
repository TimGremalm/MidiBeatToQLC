MidiBeatToQLC
=============
An interface to grab a beat-signal from MIDI-in and send it to QLC+ through a websocket.

![MidiBeatToQLC](https://raw.githubusercontent.com/TimGremalm/MidiBeatToQLC/master/MidiBeatToQLC_Screenshot1.png)

What does MidiBeatToQLC do?
===========================
It listens on beats on a MIDI-channel and sends it to specifically assigned gui-element in a virtual console in QLC+ to make lighting flash to the music.

What is QLC+?
-------------
QLC+ is a program to control light sources at for example concerts. (http://qlcplus.sourceforge.net/)
It's a powerful cross-platform program that can do really awesome stuff. But it lacks a little bit of scripting for the more advanced users, fortunately they implemented a API through websocket.

What is MIDI?
-------------
MIDI is a protocol for sending different audio-related stuff, for example a key down on a keyboard or a button pushed.

Requirements
============
QLC+
Python 2.7
PyQt4
PyGame
A program that analyzes audio and sends MIDI-beats or similar.

Install
=======
Google the respectively requirement above and follow their install-instructions.

Configuration
=============
Start QLC+ with the --web option enabled. Open a virtual console or create a new with button-elements.
Open http://127.0.0.1:9999 in your web-browser, you should see a web-interface for QLC+.
Press F12 to inspect web-elements, hover the button you want to press with MidiBeatToQLC and note the id.
Edit MidiBeatToQLC.py and declare your inputs in the main-section.

Run
===
Run MidiBeatToQLC with the -l option to list MIDI-devices, nte your decired input-id.
Start QLC+ with the --web option to make sure the websocket-mode is used.
Run MidiBeatToQLC with the -i option to start the program.
python MidiBeatToQLC.py -i1

![MidiBeatToQLC](https://raw.githubusercontent.com/TimGremalm/MidiBeatToQLC/master/MidiBeatToQLC_Screenshot2.png)

