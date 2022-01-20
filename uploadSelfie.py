import cv2
import dropbox
import random
import time

startTime = time.time()

def takeSnapshot():
    num=random.randint(0,100)
    vcObject=cv2.VideoCapture(0 , cv2.CAP_DSHOW)
    result=True

    while(result):
        r,frame = vcObject.read()

        imgname = "image"+ str(num) + ".png"

        cv2.imwrite(imgname , frame)
        result=False

    return imgname
    print("Snapshot Taken!!!")
    vcObject.release()
    cv2.destroyAllWindows()

def uploadFile(imgname):
    accessToken = "fAb2zY9lEeYAAAAAAAAAAZ5NDmBAJpa-zeZwBlNmCdm9eVHHwikFDc_aiAn2xuDW"
    filefrom = imgname
    fileto = "/pictures/"+(imgname)
    dbx = dropbox.Dropbox()

    with open(filefrom , 'rb') as f:
        dbx.files_upload(f.read() , fileto , mode=dropbox.files.WriteMode.overwrite)
        print("Uploaded!!")


def main():
    while(True):
        if( (time.time() - startTime) >= 5 ):
            IName = takeSnapshot()
            uploadFile(IName)

main()
