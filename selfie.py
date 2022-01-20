import cv2

def takeSnapshot():
    vcObject=cv2.VideoCapture(0 , cv2.CAP_DSHOW)
    result=True

    while(result):
        r,frame = vcObject.read()
        cv2.imwrite("picture.jpg" , frame)
        result=False

    vcObject.release()
    cv2.destroyAllWindows()

takeSnapshot()