#from Control import Control
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

#GPIO.setup (1, GPIO.IN)         #LevelControl
GPIO.setup (5, GPIO.OUT)        #WaterPump


#INLevelControle = GPIO.input(1)

if True: 
    GPIO.output(5, GPIO.HIGH)
else: GPIO.output(5, GPIO.LOW)

