import cv2

cap = cv2.VideoCapture('../video/output1.avi')

while True:
    ret, frame = cap.read()
    #ret = cap.set(2, 320)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
