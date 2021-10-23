import cv2
import dropbox
import time
import random

start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        imageName="img"+str(number)+".png"
        cv2.imwrite(imageName,frame)
        start_time=time.time
        result=False
    return imageName
    print("SnapShot Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadFile(imageName):
    access_token = "aa4nAQs2qwwAAAAAAAAAAfKIQ7Iog4D4k4DIzr_vvlumwfIU7OOJodE4B5-N0u3y"
    file = imageName
    file_from = file
    file_to="/testFolder/"+(imageName)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

    def main():
        while(True):
            if((time.time() - start_time) >= 5):
                name=take_snapshot()
                uploadFile(name)

    main()                