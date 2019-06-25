import cv2

videopath = 'footage.mov'
cap = cv2.VideoCapture(videopath)

frameNumber = 1     #starting frame
frameRects = []
lastFrame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frameDelta = 0
k = 0

a = 97
d = 100

x1 = 0
y1 = 0
x2 = 0
y2 = 0

showCrosshair = False
fromCenter = False

def getFrameImage(_frameNumber):
    cap.set(cv2.CAP_PROP_POS_FRAMES, _frameNumber-1)
    res, frame = cap.read()
    return frame

def getFrameDelta(_k):
    if _k == a:
        _frameDelta = -1
    elif _k == d:
        _frameDelta = 1
    return _frameDelta

def getNextFrame(_frameDelta, _frameNumber):
    if _frameDelta > 0:
        if _frameNumber >= lastFrame:
            _frameNumber = _frameNumber
        else:
            _frameNumber += 1
    elif _frameDelta < 0:
        if _frameNumber <= 1:
            _frameNumber = _frameNumber
        else:
             _frameNumber -= 1
    return _frameNumber

def MouseCallback(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        global x1
        global y1
        x1 = x
        y1 = y
    elif event == cv2.EVENT_LBUTTONUP:
        global x2
        global y2
        x2 = x
        y2 = y
        if (x1 != x2 and y1 != y2):
            AddRect(x1, y1, x2, y2)
 #           DrawAllRects()
            
        else:
            print("Not a rectangle!")
            
def AddRect(_x1, _y1, _x2, _y2):
    frameRects[frameNumber-1].append([_x1, _y1, _x2, _y2])

def ExpandFrames():
    for i in range(0, lastFrame):
        frameRects.append([])

def DrawRect(rect):
    cv2.rectangle(getFrameImage(frameNumber-1), (rect[0], rect[1]), (rect[2], rect[3]), (128, 0, 255), 5)

def DrawAllRects():
    for rect in frameRects[frameNumber-1]: #index is wrong, might be working backwards (as in from last frame to first)
        print(rect)
        DrawRect(rect)

def SaveRects(): # saves the images
    for rect in frameRects[frameNumber-1]: #index is wrong
        img = getFrameImage(frameNumber)[rect[0]:rect[2], rect[1]:rect[3    ]]
        cv2.imwrite('antimg' + str(count) + '.jpg' , img)
        print('image ' + str(count) + 'saved')


ExpandFrames()

cap2 = cv2.VideoCapture('footage.mov')
ret, frame2 = cap2.read()

cv2.rectangle(frame2, (300, 100), (400, 200), (128, 0, 255), 1)


cv2.imshow('ant', getFrameImage(frameNumber))

count = 0 

while(1):


    if (frameNumber != lastFrame):
        cap.set(cv2.CAP_PROP_POS_FRAMES, frameNumber-1)
        res, frame = cap.read()
        cv2.imshow('ant', getFrameImage(frameNumber))
    else:
        print('bruh stop')


    cv2.setMouseCallback('ant', MouseCallback)
    k = cv2.waitKey(33)
    if k==27:    # Esc key to stop
        break
    elif k==-1:  # normally -1 returned,so don't print it
        continue
    else:
        print("")


    
    frameDelta = getFrameDelta(k)
    frameNumber = getNextFrame(frameDelta, frameNumber)
    print(frameNumber)

    cv2.imshow('bruh', frame2)

    for rect in frameRects[frameNumber-1]: #works incorrectly 
        print(rect)
        DrawRect(rect)
    
    SaveRects() #works incorrectly
    count += 1
    
    cv2.waitKey(10)

cap.release()
cv2.destroyAllWindows()
