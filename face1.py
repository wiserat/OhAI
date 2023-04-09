import cv2
import numpy as np
import face_recognition as fr
from ohbot import *



video_capture = cv2.VideoCapture(0)


bottom_last = 0
left_last = 0
while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]

    face_locations = fr.face_locations(rgb_frame)
    
    for _, _, bottom, left in face_locations:

        bottom /= 50
        left /= 50
        
        bottom = int(bottom)
        left = int(left)
        
        if bottom == bottom_last and left == left_last:
            break
        elif bottom + 1 == bottom_last or bottom - 1 == bottom_last or bottom == bottom_last and left + 1 == left_last or left - 1 == left_last or left == left_last:
            move(EYETILT, bottom)
            move(EYETURN, left)
        else:
            move(HEADNOD, bottom)
            move(HEADTURN, left)
        
        to_blink += 1
        if to_blink == 100:
            move(LIDBLINK, 1)
            to_blink = 0
        
        bottom_last = bottom
        left_last = left