#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 14:08:34 2022

@author: saulo

"""

import cv2

# use csrt for this video
TrDict = {'csrt': cv2.legacy.TrackerCSRT_create, 
          'kcf': cv2.legacy.TrackerKCF_create, 
          'multi': cv2.legacy.MultiTracker_create,
          # 'boosting': cv2.legacy.TrackerBoosting_create,
          # 'mil': cv2.legacy.TrackerMIL_create,
          # 'tld': cv2.legacy.TrackerTLD_create,
          # 'medianflow': cv2.legacy.TrackerMedianFlow_create,
          # 'mosse': cv2.legacy.TrackerMOSSE_create
           }

trackers = TrDict['multi']()

video_1 = r'seu_video'
video_2 = r'seu_video'
video_3 = r'seu_video'
video_4 = r'seu_video'

video = cv2.VideoCapture(video_1)

ret, frame = video.read()

k = 4
for i in range(k):
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
        cX, cY = int(x+w//2), int(y+h//2)
        rX, rY = int(w//2), int(h//2)
        cv2.ellipse(frame, (cX, cY), (rX, rY), 90, 0, 360, (255, 255, 255), 1)
        
        if i != 0:
            frame = cv2.line(frame, (int(boxes[i][0]+boxes[i][2]//2), int(boxes[i][1]+boxes[i][3]//2)), 
                          (int(boxes[0][0]+boxes[0][2]//2), int(boxes[0][1]+boxes[0][3]//2)), (255, 25, 0), 4)
    cv2.imshow('Frame', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
        
video.release()
cv2.destroyAllWindows()