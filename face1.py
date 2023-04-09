import cv2
import numpy as np
import face_recognition as fr
from ohbot import *


#start camera capture
video_capture = cv2.VideoCapture(0)

#just predifining
bottom_last = 0
left_last = 0
while True:
    #get frame from camera
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]

    #get face from frame
    face_locations = fr.face_locations(rgb_frame)
    
    #top, right, bottom, left = face_locations but we are fine with just two values
    for _, _, bottom, left in face_locations:

        #ohbot needs values from 0 to 10 so we need to divide these values that are in pixels
        bottom /= 50
        left /= 50
        
        #ohbot needs int values
        bottom = int(bottom)
        left = int(left)
        
        #if nothing changed, don't move
        if bottom == bottom_last and left == left_last:
            break
        #if face location changed a bit just move eyes
        elif bottom + 1 == bottom_last or bottom - 1 == bottom_last or bottom == bottom_last and left + 1 == left_last or left - 1 == left_last or left == left_last:
            move(EYETILT, bottom)
            move(EYETURN, left)
        #if face location changed a lot move head
        else:
            move(HEADNOD, bottom)
            move(HEADTURN, left)
        
        #blink so ohbot won't have creepy red eyes
        to_blink += 1
        if to_blink == 100:
            move(LIDBLINK, 1)
            to_blink = 0
        
        #save for later comparison
        bottom_last = bottom
        left_last = left
