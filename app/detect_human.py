import cv2

person_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

camera = cv2.VideoCapture(0)  

if not camera.isOpened():
    print("Не удалось подключиться к камере.")
    exit()

try:
    while True:
        ret, frame = camera.read()
        if not ret:
            print("Не удалось получить кадр.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        persons = person_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(50, 50)
        )

        for (x, y, w, h) in persons:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow("Human Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    camera.release()
    cv2.destroyAllWindows()
