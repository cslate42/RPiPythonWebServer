#!/bin/bash

# output video to port 2222
# raspivid -t 0 -w 1280 -h 720 -hf -ih -fps 20 -o - | nc -k -l -p 2222
# can see from remote pc by: mplayer -fps 200 -demuxer h264es ffmpeg://tcp://192.168.11.42:2222

# too much work try not to doe this section
# @see https://raspberrypi.stackexchange.com/questions/7446/how-can-i-stream-h-264-video-from-the-raspberry-pi-camera-module-via-a-web-serve
# raspivid -n -w 720 -h 405 -fps 25 -vf -t 86400000 -b 1800000 -ih -o - \
# | ffmpeg -y \
#     -i - \
#     -c:v copy \
#     -map 0:0 \
#     -f ssegment \
#     -segment_time 4 \
#     -segment_format mpegts \
#     -segment_list "video/stream.m3u8" \
#     -segment_list_size 720 \
#     -segment_list_flags live \
#     -segment_list_type m3u8 \
#     "segments/%08d.ts"
# trap "rm stream.m3u8 segments/*.ts" EXIT
# vim:ts=2:sw=2:sts=2:et:ft=sh

# @see https://raspberrypi.stackexchange.com/questions/7446/how-can-i-stream-h-264-video-from-the-raspberry-pi-camera-module-via-a-web-serve
# @see smartphone integration
#    https://www.youtube.com/watch?v=ICyVH4u_Bhw&index=6&list=PLT2HCg4Nbo1upDmqPFxyT8koQwvCcUOph
#    https://www.linux-projects.org/uv4l/webrtc-extension/
#   http://www.linux-projects.org/documentation/uv4l-server/
# stream located at can use basic img tag http://192.168.11.42:8080/stream/video.mjpeg
uv4l --auto-video_nr --driver raspicam --server-option '--enable-webrtc-audio=0'

sudo python ./app.py
