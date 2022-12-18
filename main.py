import cv2

video = cv2.VideoCapture('vd01.mp4')
tracker = cv2.TrackerCSRT_create()

check,img = video.read()
bbox = cv2.selectROI('video',img,False)
tracker.init(img,bbox)

while True:
    check,img = video.read()
    check2,bbox = tracker.update(img)
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    if check2:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)

    cv2.imshow('video',img)
    cv2.waitKey(10)
