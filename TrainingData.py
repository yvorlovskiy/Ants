import cv2
import os

drawing = False

frameNum = 0

a = 97
d = 100

x1=0
y1=0
x2=0
y2=0
dx=0
rect=[]
FrameRects = []

videopath = 'sample.mp4'
cap = cv2.VideoCapture(videopath)
lastFrame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
count = 0

def SaveFrames():
    global count
    if not os.path.isdir(videopath + ' frames'):
        os.mkdir(videopath + ' frames')
    os.chdir(videopath + ' frames')
        
    while True:
        ret, frame = cap.read()
        if count <=lastFrame:
            cv2.imwrite(str(count) + '.jpg', frame)
            print(str(count) + '   saved')
            count +=1
        else:
            break
    cap.release()


def SaveImages():
    for _frameNum in range(0, lastFrame):
        
        if len(FrameRects[_frameNum]) > 0:
            image = cv2.imread(str(_frameNum) + '.jpg')
            for rectNum, _rect in enumerate(FrameRects[_frameNum]):
                x = int((_rect[0][0] + _rect[1][0]) / 2)
                y = int((_rect[0][1] + _rect[1][1]) / 2)
                w = int((_rect[0][0] - _rect[1][0]) / 2)

                x1 = int(x - w/2)
                x2 = int(x + w/2)
                y1 = int(y - w/2)
                y2 = int(y + w/2)
                roi = image[_rect[1][1]:_rect[0][1], _rect[0][0]:_rect[1][0]]
                cv2.imwrite(str(_frameNum) + '_' + str(rectNum) + '.jpg', roi)
        

def ExpandFrames():
    for i in range(0, lastFrame):
        FrameRects.append([])

def MouseCallback(event, x, y, flags, params):
    global rect, drawing, dx, x1, y1, x2, y2

    if event == cv2.EVENT_MOUSEMOVE:
        if not drawing:
            x1 = x
            y1 = y
        x2 = x
        y2 = y
        dx = abs(x2 - x1)
        rect = [(x1 - dx, y1 + dx), (x1 + dx, y1 - dx)]
    
    elif event == cv2.cv2.EVENT_MBUTTONDOWN:
        x1 = x
        y1 = y
        drawing = True
        
    elif event == cv2.EVENT_MBUTTONUP:
        FrameRects[frameNum].append(rect)
        drawing = False
        print(FrameRects)


SaveFrames()
ExpandFrames()

window = cv2.imread(str(frameNum) + '.jpg')
cv2.imshow('window' , window)


while True:
    
    window = cv2.imread(str(frameNum) + '.jpg')

    if drawing:
        cv2.rectangle(window ,rect[0] ,rect[1] ,(255,0,128) ,3)

    for _rect in FrameRects[frameNum]:
        cv2.rectangle(window ,_rect[0], _rect[1],(0,0,255) ,3)


    cv2.imshow('window' , window)

    cv2.setMouseCallback('window', MouseCallback)
    k=cv2.waitKey(10) & 0XFF
    if k == a:
        if frameNum > 0:
            frameNum -=1
    elif k == d:
        if frameNum < lastFrame:
            frameNum +=1
    elif k==27:    # Esc key to stop
        break

SaveImages()

cv2.destroyAllWindows()
    
    


