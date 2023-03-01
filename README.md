# AutoFish
A program that will allow you to auto fish. Fishing is based off the sound the bobber makes when a fish bites the line.

Requirements
------------
The [Interactive Fishing Bobber][ifb] addon is required for the program to work.

[Python 3.5+][python]

PyAutoGUI

* `py -m pip install pyautogui`

SoundCard

* `py -m pip install souncard`

NumPy

* `py -m pip install numpy`

Setup
------------

The CAST_KEY is the hot key you have your fish cast set to (mine is "-").

The CATCH_KEY is the interact hot key (mine is "=").

```py
CAST_KEY = "-"
CATCH_KEY = "="
SOUND_THRESHOLD = 0.0008
```
Sound Threshold is the minimum volume that the CATCH_KEY will be triggered.
The example output below shows a successful catch. The fish volume average value shows that the ambient noise
averages around .0003 to .0004. When the splash of the bobber is triggered, the fish volume average increases to .00168 and triggers our CATCH_KEY.
```
Fish iteration = 3, Time Elapsed = 0:00:48, Minutes Selected = 1
0 - catch = False: fish volume =   0.00043, speaker = 'Headphones (4- Arctis 7 Game)'
1 - catch = False: fish volume =   0.00025, speaker = 'Headphones (4- Arctis 7 Game)'
2 - catch = False: fish volume =   0.00026, speaker = 'Headphones (4- Arctis 7 Game)'
3 - catch = False: fish volume =   0.00028, speaker = 'Headphones (4- Arctis 7 Game)'
4 - catch = False: fish volume =   0.00029, speaker = 'Headphones (4- Arctis 7 Game)'
5 - catch = False: fish volume =   0.00027, speaker = 'Headphones (4- Arctis 7 Game)'
6 - catch = False: fish volume =   0.00032, speaker = 'Headphones (4- Arctis 7 Game)'
7 - catch = True: fish volume =   0.00168, speaker = 'Headphones (4- Arctis 7 Game)'
Fish caught!!!
```

[python]: https://www.python.org/downloads/
[ifb]: https://www.curseforge.com/wow/addons/interactivefishingbobber
