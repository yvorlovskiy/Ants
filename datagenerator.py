import cv2 

videopath = 'sample.mp4'
cap = cv2.VideoCapture(videopath)

count = 0


while True:
    ret, frame = cap.read()
    if count <=10:
        cv2.imwrite('frame' + str(count) + '.jpg', frame)
        print('frame   ' + str(count) + '   saved')
    count +=1
    
    k = cv2.waitKey(33)
    if k==27:    # Esc key to stop
        break

    if __name__ == '__main__':
        cv2.imshow('frame', frame)

   
        

cap.release()
cv2.destroyAllWindows()











    