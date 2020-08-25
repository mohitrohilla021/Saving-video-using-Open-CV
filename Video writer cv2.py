import cv2

# fourcc is a 4 byte code that is used to specify the video codac...
cap=cv2.VideoCapture(0)
fourcc= cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter("output.avi", fourcc,20.0, (640,480))
# here, 20 is the number of frames per second...
while cap.isOpened():
    ret,frame=cap.read()
    if ret==True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)

        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)

        if cv2.waitKey(1) & 0xff==ord('q'):
            break
    else:
        continue

cap.release()
out.release()
cv2.destroyAllWindows()

