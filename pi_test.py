import RPi.GPIO as GPIO
from random import randint
import time
from grove.grove_button import GroveButton
# connect to pin and define pin number (22)
GPIO.setup(22, GPIO.IN)
GPIO.setup(5, GPIO.OUT)
frequence = randint(100,20000)
dc = 50
buzz = GPIO.PWM(5,frequence) # fréquence en Hz

buzz.start(dc)
button = GroveButton(22)
GPIO.setmode(GPIO.BCM) # le mode d’adressage des PIN choisit
def on_press(t):
# define on press behavior
    frequence = randint(100,500)
    GPIO.output(5, 1)
    # écriture state peut être 1 ou 0
    buzz.ChangeFrequency(frequence)
    buzz.ChangeDutyCycle(dc)
    
def on_release(t):
    buzz.ChangeDutyCycle(0)    
# define on press behavior
button.on_press = on_press
button.on_release = on_release

 # dc est le rapport cyclique (duty cycle) (0.0 <= dc <= 100.0)
"""
buzz.ChangeFrequency(freq)
buzz.ChangeDutyCycle(dc)
"""