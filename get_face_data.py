import picamera
import cv2
import time
import os
from subprocess import call
def face_data(name, mode = 0):
    camera = picamera.PiCamera()
    camera.start_preview()
    print('starting preview, start moving')
    time.sleep(2)
    camera.start_recording(name + '.h264')
    camera.wait_recording(10)
    camera.stop_recording()
    camera.stop_preview()
    path = "dataset/%s" % (name)
    if(mode):
        os.mkdir(path)
    cap = cv2.VideoCapture(name + '.h264')
    success, image = cap.read()
    count = 0
    while(success):
        cv2.imwrite("%s/%d.jpg" % (path,count), image)
        success, image = cap.read()
        count += 1
    cap.release()
    cv2.destroyAllWindows()
    if os.path.exists(name + '.h264'):
        os.remove(name + '.h264')
    if mode:
        call(["python3 extract_embeddings.py --dataset dataset --embeddings output/embeddings.pickle \	--detector face_detection_model --embedding-model openface_nn4.small2.v1.t7"], shell=True)
