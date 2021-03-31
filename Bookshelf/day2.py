import RPi.GPIO as GPIO
from time import sleep

Motor1A = 24
Motor1B = 23
Motor1E = 25
ledPin = 22

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Motor1A, GPIO.OUT)
    GPIO.setup(Motor1B, GPIO.OUT)
    GPIO.setup(Motor1E, GPIO.OUT)
    GPIO.setup(ledPin, GPIO.OUT)

def loop():
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)
    print("first block")

    sleep(5)

    print ('LED on')
    GPIO.output(ledPin, GPIO.HIGH)
    sleep(1)
    print('LED off')
    GPIO.output(ledPin, GPIO.LOW)
    sleep(1)

    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)
    print("second block")

    sleep(5)
    GPIO.output(Motor1E, GPIO.LOW)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    while (True):
        try:
            loop()
        except KeyboardInterrupt:
            destroy()
