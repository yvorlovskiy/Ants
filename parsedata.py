import cv2
import numpy as np 

#filters 
def ImageOperation(frame):
    closing = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, kernel)
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
    dilate = cv2.dilate(closing, (5, 5), iterations=1)
    ret, thresh =  cv2.threshold(dilate,127,255,cv2.THRESH_BINARY)
    return thresh


#boundingbox points 
def GetBoundingBoxes(thresh):
    fgmask = BackgroundSubtrator.apply(thresh, None, -1)
    bboxes = []
    keypoints = BlobDetector.detect(fgmask)
    for keypoint in keypoints:
        if keypoint:
            x = int(round(keypoint.pt[0]))
            y = int(round(keypoint.pt[1]))
            s = int(round(keypoint.size))/2
            bbox = (x-s,y+s,x,y)
            bboxes.append(bbox)
            
            #cv2.rectangle(frame,(x-s,y+s),(x+s,y-s),(255,0,255),3)
            
            return bboxes
            

#Saves cropped images ants
def CollectImages(frame, points):
    count = 1 
    
    if ((len(points[0])) == 4):
        image = frame[points[0][0]:points[0][2], points[0][3]:points[0][1]] 
        cv2.imwrite('ant'+str(count) + '.jpg', image)
        count += 1

 


#Sets up Background Subtraction
BackgroundSubtrator = cv2.createBackgroundSubtractorMOG2(999, detectShadows=True)
Parameters = cv2.SimpleBlobDetector_Params()

#Parameters for blob tracking
Parameters.minThreshold = 0
Parameters.maxThreshold = 255
Parameters.filterByArea = True
Parameters.minArea = 10
Parameters.maxArea = 50
Parameters.filterByCircularity = False
Parameters.filterByInertia = True
Parameters.filterByConvexity = False
Parameters.filterByColor = False
Parameters.blobColor = 0
BlobDetector = cv2.SimpleBlobDetector_create(Parameters)

kernel = np.ones((11,11),np.uint8)

cap = cv2.VideoCapture('footage.mov')

while True: 
    ret, frame = cap.read()
    cropped = frame[100:250, 100:250] #takes part of the image for analysis
    
    bboxes = [] #bounding boxes for the images from Background subtraction
    bboxes.append(GetBoundingBoxes(ImageOperation(frame)))

    #CollectImages(frame, bboxes)
    


    cv2.imshow('frame', frame)

    
    cv2.imshow('cropped', cropped)
    cv2.imshow('fgmask', ImageOperation(cropped))

    print(bboxes)

    #Draws circles around ants (test)
    if (type(bboxes) is not None): 
        cv2.circle(frame, (int(bboxes[0][2]), int(bboxes[0[3]])), 50,  (0,0,0), 5)

    
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()



