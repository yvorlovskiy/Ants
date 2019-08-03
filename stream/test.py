import cv2
import sys
import os 
import time 

start_time = time.time()
elapsed_time = time.time() - start_time

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    cv2.imshow('frame', frame)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
    print(elapsed_time)
    
cap.release()
cv2.destroyAllWindows()

