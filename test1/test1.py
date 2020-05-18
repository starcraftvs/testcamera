import cv2
cap=cv2.VideoCapture(0)
cap.set(3,1080)
cap.set(4,3840)
while(True):
    ret,frame=cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1)&0xFF==ord('q'):
        cv2.imwrite('img.jpg',frame)
        break
cap.release()
cv2.destroyAllWindows()
