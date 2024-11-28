import cv2

person_cascade = cv2.CascadeClassifier('/home/raspberry/RaspPi_CV/haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture(0, cv2.CAP_V4L2)  

if not camera.isOpened():
    print("Не удалось подключиться к камере.")
    exit()

try:
    while True:
        ret, frame = camera.read()
        if not ret:
            print("Не удалось получить кадр.")
            break

        resized_frame = cv2.resize(frame, (320, 240))

        gray = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

        persons = person_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        for (x, y, w, h) in persons:
            cv2.rectangle(resized_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow("Human Detection", resized_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    camera.release()
    cv2.destroyAllWindows()
