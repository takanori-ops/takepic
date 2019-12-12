import time
import picamera
import os
import RPi.GPIO as GPIO
import time

check = os.path.exists('output')
if  not check:
	os.makedirs('output')
else:
	print("directly is exists.please move it before starting")
	exit()

GPIO.setmode(GPIO.BCM)
gp_out = 2
GPIO.setup(gp_out,GPIO.OUT)

motor = GPIO.PWM(gp_out,50)
motor.start(1.0)
resolution_setting = (250,250)

time_sleep =2


try:	
	for i in range(2,12):
		with picamera.PiCamera() as camera:
			camera.resolution = resolution_setting
			if i == 2:
				camera.start_preview()
				val = input('enter key for start')
				
			time.sleep(time_sleep)
			print("start {}".format(i))
			camera.capture("output/picture_{}.jpg".format(i))
			time.sleep(time_sleep)
			motor.ChangeDutyCycle(i)
			time.sleep(time_sleep)
except:
	print("failed")
finally:
	print("finished")
	GPIO.cleanup()
