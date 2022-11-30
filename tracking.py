#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 14:08:34 2022

@author: saulo

"""

import cv2


TrDict = {'csrt': cv2.legacy.TrackerCSRT_create, 
          'kcf': cv2.legacy.TrackerKCF_create, 
          'multi': cv2.legacy.MultiTracker_create
           }

trackers = TrDict['multi']()

video = cv2.VideoCapture(r'brazil_tracking.mp4')

ret, frame = video.read()

k = 5
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
    for box in boxes:
        (x, y, w, h) = [a.astype(int) for a in box]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 1)
    cv2.imshow('Frame', frame)
    key = cv2.waitKey(5) & 0xFF
    if key == ord('q'):
        break
        
video.release()
cv2.destroyAllWindows()