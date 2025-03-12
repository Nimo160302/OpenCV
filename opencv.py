#READING IMAGES AND VIDEOS
import cv2 as cv
img =  cv.imread('data/aero1.jpg')

cv.imshow('aero',img)
cv.waitKey(0)

#Reading Videos
# we can work with webcam too by using integer argument or with path of video
capture = cv.VideoCapture('data/vid1.mp4')

#video is read frame by frame

#problem statement : Videos are made up of many frame..
# ... so we need to show frames one by one such that it appear as video

# .read() funciton will return two output
# 1. a bool that say if the frame is succesfully read or not
# 2. an ndarray that is data of the frame


while True: #infinte loop\
    isTrue, data =  capture.read()
    cv.imshow('video', data)

    if cv.waitKey(20) & 0xFF== ord('d'):
        # it says that if the button d is pressed than exit
        break
capture.release()
cv.destroyAllWindows()













