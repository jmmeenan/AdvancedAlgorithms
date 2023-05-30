import cv2 

ip_addres = ""
url = "http://" + ip_addres + ":8080/video"

cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destoryAllWindows()
