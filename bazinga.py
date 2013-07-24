#!/usr/bin/python2.7
#
# Copyright (C) 2013 Aneesh Dogra (lionaneesh@gmail.com)
#
# Work in progress, not usable

import vlc # libVLC
import time
import pysrt
import random

subs = pysrt.open('/Users/aneeshdogra/Downloads/The Big Bang Theory/01x17 - The Tangerine Factor.srt')

def play(file, sub):
    instance = vlc.Instance()
    mediaPlayer = instance.media_player_new()
    mediaPlayer.set_mrl(file)
    start_time = sub.start.hours * 3600 + sub.start.minutes * 60 + sub.start.seconds
    end_time = sub.end.hours * 3600 + sub.end.minutes * 60 + sub.end.seconds

    mediaPlayer.play()
    mediaPlayer.set_time(start_time * 1000)

    time.sleep(end_time - start_time)

    start_time = mediaPlayer.get_time() / 1000.

    if start_time < end_time:
        time.sleep(end_time - start_time)

    mediaPlayer.stop()
    print sub.text


for s in subs:
    if "Sheldon" in s.text:
        rs = play("/Users/aneeshdogra/Downloads/The Big Bang Theory/01x17 - The Tangerine Factor.avi", s)