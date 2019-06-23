import cv2

videopath = 'footage.mov'
frame_number = 61

cap = cv2.VideoCapture(videopath)
cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number-1)#cv2.CV_CAP_PROP_POS_FRAMES
res, frame = cap.read()


while(1):
    cv2.imshow('image', frame)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
