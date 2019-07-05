import cv2

FrameRects = []
a = 97
d = 100
num = 0 
k = 0

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
        else:
            print("Not a rectangle!")

def AddRect(_x1, _y1, _x2, _y2):
    FrameRects[num].append([_x1, _y1, _x2, _y2])

def ExpandFrames():
    for i in range(0, 10):
        FrameRects.append([])

ExpandFrames()
 
while 1:
    window = cv2.imread('frame' + str(num) + '.jpg')
    cv2.imshow('window' , window)

    cv2.setMouseCallback('window', MouseCallback)

    k=cv2.waitKey(10) & 0XFF
    if k == a:
        num -=1
    elif k == d:
        num +=1
    
    print(FrameRects)

    if k==27:    # Esc key to stop
        break

cv2.destroyAllWindows()
    
    


