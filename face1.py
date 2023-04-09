import cv2
import numpy as np
import face_recognition as fr
from ohbot import *
import os


#start camera capture
video_capture = cv2.VideoCapture(0)

#load images of known faces
known_face_names = []
known_face_encodings = []
for img in os.listdir("imgs"):
    image = fr.load_image_file("imgs/" + img)
    image_face_encoding = fr.face_encodings(image)[0]
    known_face_encodings.append(image_face_encoding)
    known_face_names.append(img.split(".")[0])

#just predifining
bottom_last = 0
left_last = 0
while True:
    #get frame from camera
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]

    #get face from frame
    face_locations = fr.face_locations(rgb_frame)
    face_encodings = fr.face_encodings(rgb_frame, face_locations)
    
    #top, right, bottom, left = face_locations but we are fine with just two values
    for (_, _, bottom, left), face_encoding in zip(face_locations, face_encodings):

        #ohbot needs values from 0 to 10 so we need to divide these values that are in pixels
        bottom /= 50
        left /= 50
        
        #ohbot needs int values
        bottom = int(bottom)
        left = int(left)
        
        #if nothing changed, don't move
        if bottom == bottom_last and left == left_last:
            bottom = bottom_last
            left = left_last
            break
        #if face location changed a bit just move eyes
        elif bottom + 1 == bottom_last or bottom - 1 == bottom_last or bottom == bottom_last and left + 1 == left_last or left - 1 == left_last or left == left_last:
            move(EYETILT, bottom)
            move(EYETURN, left)
            bottom = bottom_last
            left = left_last
        #if face location changed a lot move head
        else:
            move(HEADNOD, bottom)
            move(HEADTURN, left)
            move(EYETILT, 5)
            move(EYETURN, 5)
            
        #match face with known faces
        matches = fr.compare_faces(known_face_encodings, face_encoding)
        fc_distances = fr.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(fc_distances)
        #if match found
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            if name == "josh":
                say("Don't run away Josh, I'm about to suck your toes, yummy")
            elif name == "jonas":
                say("Here comes the ladies man")
            elif name == "sasa":
                say("ain't no lolis in here")
        
        #blink so ohbot won't have dryass creepy red eyes
        to_blink += 1
        if to_blink == 100:
            move(LIDBLINK, 1)
            to_blink = 0
        
        #save for later comparison
        bottom_last = bottom
        left_last = left
