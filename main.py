import time
import sys
import vlc

def bip(sound_path):
    sound = vlc.MediaPlayer(sound_path)
    sound.play()
    time.sleep(0.1)
    sound.stop()

sleep_time = 10
if len(sys.argv) > 1:
    sleep_time = int(sys.argv[1])


while (1):
    bip("./bip.mp3")
    time.sleep(sleep_time)
