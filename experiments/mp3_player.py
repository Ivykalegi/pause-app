'''code to play the mp3 tracks for the study sounds in Python using pygame'''

import itertools
import time
from pygame import mixer


mixer.init()
mixer.music.load("/Users/joannawaller/Desktop/Pause Study Sounds/lofi sounds.mp3")
mixer.music.play()
while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(3)

repeater = itertools.repeat(mixer.music.play())

