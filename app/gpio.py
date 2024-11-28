LED_PIN = 14 
BUTTON_PIN = 15
SERVO_PIN = 18
 
import sys 
import RPi.GPIO as GPIO 

#GPIO.cleanup()
GPIO.setmode(GPIO.BCM) 
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(LED_PIN, GPIO.OUT) 
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)
angle = 0
 
def SetAngle(angle):
    duty = angle/18+2
    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty)
while True: 
    inputValue = GPIO.input(BUTTON_PIN) 
    if (inputValue == True): 
        #print("BUT")
        GPIO.output(LED_PIN,True) 
        if (angle < 180):
            angle+=20
        else:
            angle = 5
        #angle+=15
        SetAngle(angle)
    else: 
        GPIO.output(LED_PIN,False)
        #SetAngle(0)
    #GPIO.cleanup()
GPIO.cleanup()