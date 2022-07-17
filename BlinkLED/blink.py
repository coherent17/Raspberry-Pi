import RPi.GPIO as GPIO
import time

#using BCM system:
GPIO.setmode(GPIO.BCM)

led1 = 19
led2 = 26

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

try:
	while(True):
		GPIO.output(led1, True)
		time.sleep(0.5)
		GPIO.output(led1, False)
		time.sleep(0.5)

		GPIO.output(led2, True)
		time.sleep(0.5)
		GPIO.output(led2, False)
		time.sleep(0.5)

except KeyboardInterrupt:
	GPIO.cleanup()