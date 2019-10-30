import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOAORD)
LED=11
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
try:
    while 1:
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED, GPIO.LOW)
        time.sleep(0.5)

except KeyboardInterrupt:
    pass
GPIO.clenaup()
