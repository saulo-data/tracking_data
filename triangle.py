#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 09:30:30 2022

@author: saulo
"""


import cv2


# use csrt for this video
TrDict = {'csrt': cv2.legacy.TrackerCSRT_create, 
          'kcf': cv2.legacy.TrackerKCF_create, 
          'multi': cv2.legacy.MultiTracker_create,
          'boosting': cv2.legacy.TrackerBoosting_create,
          'mil': cv2.legacy.TrackerMIL_create,
          'tld': cv2.legacy.TrackerTLD_create,
          'medianflow': cv2.legacy.TrackerMedianFlow_create,
          'mosse': cv2.legacy.TrackerMOSSE_create
           }

trackers = TrDict['multi']()

video = cv2.VideoCapture(r'seu_video')

ret, frame = video.read()

 

for i in range(3):
    cv2.imshow('Frame', frame)
    bbi = cv2.selectROI('Frame', frame)
    tracker_i = TrDict['csrt']()
    trackers.add(tracker_i, frame, bbi)

while True:
    ret, frame = video.read()
    if not ret:
        break
    (success, boxes) = trackers.update(frame)
    for i, box in enumerate(boxes):
        (x, y, w, h) = [a.astype(int) for a in box]
        cv2.ellipse(frame, (x+w//2, y+h//2), (w//2, h//2), 90, 0, 360, (255, 255, 255), 1)
        if i <= 1: 
            frame = cv2.line(frame, (int(boxes[i][0]+boxes[i][2]//2), int(boxes[i][1]+boxes[i][3]//2)), 
                          (int(boxes[i+1][0]+boxes[i+1][2]//2), int(boxes[i+1][1]+boxes[i+1][3]//2)), (255, 25, 0), 3)
        if i == 2:
            frame = cv2.line(frame, (int(boxes[i][0]+boxes[i][2]//2), int(boxes[i][1]+boxes[i][3]//2)), 
                          (int(boxes[0][0]+boxes[0][2]//2), int(boxes[0][1]+boxes[0][3]//2)), (255, 25, 0), 3)
    cv2.imshow('Frame', frame)
    key = cv2.waitKey(5) & 0xFF
    if key == ord('q'):
        break
        
video.release()
cv2.destroyAllWindows()