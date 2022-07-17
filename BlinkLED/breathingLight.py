import RPi.GPIO as GPIO
import time

#using BCM system:
GPIO.setmode(GPIO.BCM)

led1 = 19
led2 = 26
frequency = 120

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

led_pwm = []
led_pwm.append(GPIO.PWM(led1, frequency))
led_pwm.append(GPIO.PWM(led2, frequency))

for led in led_pwm:
	led.start(0)

try:
	while(True):
		#become lighter through change the duty cycle
		for i in range(0, 80, 5):
			for led in led_pwm:
				led.ChangeDutyCycle(i)
				time.sleep(0.1)

		#become darker
		for i in range(80, 0, -5):
			for led in led_pwm:
				led.ChangeDutyCycle(i)
				time.sleep(0.1)		

except KeyboardInterrupt:
	for led in led_pwm:
		led.stop()
	GPIO.cleanup()