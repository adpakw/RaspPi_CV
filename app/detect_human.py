import cv2
import sys 
import RPi.GPIO as GPIO 

LED_PIN = 14 
BUTTON_PIN = 15
SERVO_PIN = 18

GPIO.setmode(GPIO.BCM) 
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(LED_PIN, GPIO.OUT) 
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)
angle = 0

def SetAngle(angle):
    duty = abs(angle)/18+2
    if duty >= 90:
        duty = 1
    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty)

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
            GPIO.output(LED_PIN,True) 
            if x > 160:
                angle += 20
            else:
                angle -= 20
            SetAngle(angle)
            cv2.rectangle(resized_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow("Human Detection", resized_frame)
        GPIO.output(LED_PIN,False)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            GPIO.cleanup()
            break
finally:
    camera.release()
    cv2.destroyAllWindows()
