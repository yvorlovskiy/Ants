import cv2
import numpy as np

def eventType(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Left Click Down!")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("Right Click Down!")
    elif event == cv2.EVENT_MBUTTONDOWN:
        print("Scroll Wheel Down!")
    elif event == cv2.EVENT_LBUTTONUP:
        print("Left Click Up!")
    elif event == cv2.EVENT_RBUTTONUP:
        print("Right Click Up!")
    elif event == cv2.EVENT_MBUTTONUP:
        print("Scroll Wheel Up!")
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        print("Double Click Left!")
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        print("Double Click Right!")
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        print("Double Click Scroll Wheel!")
    elif event == cv2.EVENT_MOUSEWHEEL:
        print("Scroll Up!")
    elif event == cv2.EVENT_MOUSEHWHEEL:
        print("Scroll Down!")

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', eventType)

while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
