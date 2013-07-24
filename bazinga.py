#!/usr/bin/python2.7
#
# Copyright (C) 2013 Aneesh Dogra (lionaneesh@gmail.com)
#
# Find my Bazinga

import vlc # libVLC
import time
import pysrt
import os

video_formats = [".mp4", ".avi"]
DIR = '/home/aneesh/The Big Bang Theory'

BUFFER = 0.5

def play(file, sub, mediaPlayer):
    start_time = sub.start.hours * 3600 + sub.start.minutes * 60 + sub.start.seconds
    end_time = sub.end.hours * 3600 + sub.end.minutes * 60 + sub.end.seconds

    mediaPlayer.play()
    mediaPlayer.set_time(start_time * 1000)

    time.sleep(end_time - start_time + BUFFER)

    start_time = mediaPlayer.get_time() / 1000.
    if start_time < end_time:
        time.sleep(end_time - start_time)

    mediaPlayer.pause()

def find_media_files(media_files):
    print "Finding media files in ", DIR
    for dirpath, dirs, files in os.walk(DIR):
        for filename in files:
            file_path = os.path.join(dirpath, filename)
            f, ext   = os.path.splitext(file_path)
            if ext in video_formats:
                subtitle_path = f + '.srt'
                if os.path.exists(subtitle_path):
                    media_files.append((file_path, subtitle_path))


instance = vlc.Instance()
mediaPlayer = instance.media_player_new()
mediaPlayer_list = instance.media_list_new()
listMediaPlayer = instance.media_list_player_new()
listMediaPlayer.set_media_list(mediaPlayer_list)
listMediaPlayer.set_media_player(mediaPlayer)
media_files = []
find_media_files(media_files)

req_subs = [] # (file, sub)

for m in media_files:
    print m[1]
    subs = pysrt.open(m[1], encoding='iso-8859-1')
    for s in subs:
        if "bazinga" in s.text.lower():
            req_subs.append((m[0], s))

for r in range(0, len(req_subs)):
    mediaPlayer_list.insert_media(instance.media_new(req_subs[r][0]), r)
    listMediaPlayer.play_item_at_index(r)
    play(req_subs[r][0], req_subs[r][1], mediaPlayer)
