#from Control import Control
import RPi.GPIO as GPIO



GPIO.setmode(GPIO.BCM)

GPIO.setup (1, GPIO.IN)         #LevelControl
GPIO.setup (5, GPIO.OUT)        #WaterPump
GPIO.setup (6, GPIO.OUT)        #Valve1
GPIO.setup (7, GPIO.OUT)        #Valve2
GPIO.setup (8, GPIO.OUT)        #Valve3
GPIO.setup (9, GPIO.OUT)        #Valve4

INLevelControle = GPIO.input(1)

if Control.aWaterPump: GPIO.output(5, GPIO.HIGH)
else: GPIO.output(5, GPIO.LOW)

if Control.aValve_1: GPIO.output(6, GPIO.HIGH)
else: GPIO.output(6, GPIO.LOW)

if Control.aValve_2: GPIO.output(7, GPIO.HIGH)
else: GPIO.output(7, GPIO.LOW)

if Control.aValve_3: GPIO.output(8, GPIO.HIGH)
else: GPIO.output(8, GPIO.LOW)

if Control.aValve_4: GPIO.output(9, GPIO.HIGH)
else: GPIO.output(9, GPIO.LOW)