import cv2
import dropbox
import time
import random

starttime=time.time()
def takesnapshot():
    number=random.randint(0,100)
    vca=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=vca.read()
        imagename="img"+str(number)+".png"
        cv2.imwrite(imagename,frame)
        starttime=time.time()
        result=False
    return imagename
    print("snapshottaken")
    vca.release()
    cv2.destroyAllWindows()
def uploadfile(imagename):
    accesstoken="sl.BE-SZuT39F8JtKN5hrQcUS0e_l6Vs5LCYyQs2Esw3K8PMG4TV87FfbEBULL850b9MCaI018XanCpg1T-TUmYOzDdtNwQq_zTv8Vs1IEU0RxYWkOYdrP-CIfIv5p5MoXpYjD4PA0"
    file=imagename
    file_from=file
    file_to="/imagefolder/"+(imagename)
    dbx=dropbox.Dropbox(accesstoken)
    with open(file_from,"rb")as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("fileuploaded")
def main():
    while True:
           if((time.time()-starttime)>=5):
               name=takesnapshot()
               uploadfile(name)
main()
                    
    
        
            
            
             
