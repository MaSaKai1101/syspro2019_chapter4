import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

bottom = 2.5
middle = 7.2
top = 12.0

def setservo(input):
	value = float(input) * 0.02666
	return value

servo.ChangeDutyCycle(top)
for i in range(5):
	inputer = input()
	value = setservo(inputer)
	print("{:1f}".format(value))
	servo.ChangeDutyCycle(value)
	time.sleep(1.0)

servo.stop()
GPIO.cleanup()




