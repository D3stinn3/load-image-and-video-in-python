import cv2
#imput the video path
cap = cv2.VideoCapture("C:\\Users\\Daniel Samuel\\Videos\\machinel learning tutorials\\computer visioin (open cv) for beiggners\\02.How To Read Image-Video-Webcam [1] - OpenCV Python Tutorials for Beginners 2020.mp4")
#for webcam
#cap = cv2.VideoCapture(0)

# set the frame size
framewidht = 2000
frameheight = 1000

# for webcam
# cap.set(3,framewidht)
# cap.set(4,frameheight)

# loop through every frame in the video
while True:
    suc,img = cap.read()
    #display video
    img = cv2.resize(img,(framewidht,frameheight))
    cv2.imshow("displayed image",img)

    #quit if q is pressed
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break