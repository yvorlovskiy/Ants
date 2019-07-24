 #to use: python3 TrainingData.py [insert video file here] [insert directory you want your images saved to]
#Note: program creates directory if you do not already have it

import cv2
import os
import sys
import math

args = sys.argv

drawing = False

frameNum = 0
frameSaved = 100

a = 97
d = 100
s = 115

x1=0
y1=0
x2=0
y2=0
dx=0
rect=[]
FrameRects = []
hoveringIndexes = []

videoPath = args[1]
#imagesPath = args[2]
framesPath = 'antdata/JPEGImages'
# framesPath = '/Users/yuryorlovskiy/Dev/Ants/AntsGit/Data-Collection/antdata/JPEGImages'
txtPath = '/Users/yuryorlovskiy/Dev/Ants/AntsGit/Data-Collection/antdata/Labels'
finalpath = '/Users/yuryorlovskiy/Dev/Ants/AntsGit/Data-Collection/antdata/'

cap = cv2.VideoCapture(videoPath)
lastFrame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
count = 0


def SaveFrames():
    global count
    if not os.path.isdir(framesPath):
        os.mkdir(framesPath)
    os.chdir(framesPath)

    print("Saving " + str(frameSaved) + " Frames out of " + str(lastFrame))
    while True:
        ret, frame = cap.read()
        if count <=frameSaved:
            cv2.imwrite(str(count) + '.jpg', frame)
            count +=1
        else:
            break
    cap.release()


def SaveImages():
    print("Saving Images...")
    os.chdir('..')
    if not os.path.isdir(imagesPath):
        os.mkdir(imagesPath)
    os.chdir(framesPath)
    
    for _frameNum in range(0, lastFrame):        
        if len(FrameRects[_frameNum]) > 0:
            image = cv2.imread(str(_frameNum) + '.jpg')
            for rectNum, _rect in enumerate(FrameRects[_frameNum]):
                roi = image[_rect[1][1]:_rect[0][1], _rect[0][0]:_rect[1][0]]
                os.chdir('..')
                os.chdir(imagesPath)
                cv2.imwrite(str(_frameNum) + '_' + str(rectNum) + '.jpg', roi)
                os.chdir('..')
                os.chdir(framesPath)
    print("Finished!")        

def WriteAnotations():
    if not os.path.isdir(txtPath):
        os.mkdir(txtPath)
    os.chdir(txtPath)
    
    print("Saving Annotations...")
    for _frameNum in range(0, lastFrame):
        if (len(FrameRects[_frameNum]) > 0):
            f = open(str(_frameNum) + ".txt", "a+")
            #anotationCount += 1   
        if len(FrameRects[_frameNum]) > 0:
            image = cv2.imread(str(_frameNum) + '.jpg')
            for rectNum, _rect in enumerate(FrameRects[_frameNum]):
                x = int((_rect[0][0] + _rect[1][0]) / 2)
                y = int((_rect[0][1] + _rect[1][1]) / 2)
                w = int((_rect[1][0] - _rect[0][0]))

                xval = x/width
                yval = y/height
                wval = w/width
                hval = w/height

                f.write(str(0) + " " + str(xval) + " " + str(yval) + " " + str(wval) + " " + str(hval))
                f.write('\n')
    f.close()
    print("Finished!")  


    
def ExpandFrames():
    for i in range(0, lastFrame):
        FrameRects.append([])


def DeleteRects():
    global hoveringIndexes
    if len(hoveringIndexes) > 0:
        for i in hoveringIndexes:
            FrameRects[frameNum].remove(i)
    hoveringIndexes = []
            

def MouseCallback(event, x, y, flags, params):
    global rect, drawing, dx, x1, y1, x2, y2, mouseX, mouseY, hoveringIndexes

    if event == cv2.EVENT_MOUSEMOVE:
        hoveringIndexes = []
        for i, _rect in enumerate(FrameRects[frameNum]):
            if _rect[0][0] <= x <= _rect[1][0] and _rect[1][1] <= y <= _rect[0][1]:
                hoveringIndexes.append(_rect)
        
        if not drawing:
            x1 = x
            y1 = y
        x2 = x
        y2 = y
        dx = abs(x2 - x1)
        rect = [(x1 - dx, y1 + dx), (x1 + dx, y1 - dx)]
    
    elif event == cv2.cv2.EVENT_LBUTTONDOWN:
        x1 = x
        y1 = y
        drawing = True
        
    elif event == cv2.EVENT_LBUTTONUP:
        FrameRects[frameNum].append(rect)
        drawing = False


SaveFrames()
ExpandFrames()

window = cv2.imread(str(frameNum) + '.jpg')
cv2.imshow('window' , window)


while True:
    
    window = cv2.imread(str(frameNum) + '.jpg')
    height, width = window.shape[:2]
    
    if drawing:
        cv2.rectangle(window ,rect[0] ,rect[1] ,(255,0,128) ,3)

    for _rect in FrameRects[frameNum]:
        if _rect in hoveringIndexes:
            cv2.rectangle(window ,_rect[0], _rect[1],(255,204,255) ,3)
        else:
            cv2.rectangle(window ,_rect[0], _rect[1],(0,0,255) ,3)

    cv2.imshow('window' , window)

    cv2.setMouseCallback('window', MouseCallback)
    
   

    k=cv2.waitKey(10) & 0XFF
    if k == a:
        if frameNum > 0:
            frameNum -=1
            print(frameNum)
    elif k == d:
        if frameNum < lastFrame:
            frameNum +=1
            print(frameNum)
    elif k == s:
        DeleteRects()

    elif k==27:    # Esc key to stop
        break

WriteAnotations() #ANNOTATIONS

cv2.destroyAllWindows()

os.chdir(finalpath)

import TrainTest
