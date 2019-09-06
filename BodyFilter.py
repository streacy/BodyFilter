import cv2
import sys


def body_filter():
    ascPath = sys.argv[1]
    faceCascade = cv2.CascadeClassifier(cascPath)

    video_capture = ccv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiscale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30,30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    body_filter()