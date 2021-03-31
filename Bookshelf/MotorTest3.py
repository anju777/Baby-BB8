import RPi.GPIO as GPIO  
import time

# for GPIO numbering, choose BCM  
GPIO.setmode(GPIO.BCM)  
  
# or, for pin numbering, choose BOARD  
#GPIO.setmode(GPIO.BOARD)

# battery1 = 2
# battery2 = 4

AEnable = 27
AIN1 = 25
AIN2 = 24
# BIN1 = 23  # 16
# BIN2 = 18  # 12

GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(AEnable, GPIO.OUT)

forward = GPIO.PWM(AIN1, 100)
reverse = GPIO.PWM(AIN2, 100)
# GPIO.setup(BIN1, GPIO.OUT)
# GPIO.setup(BIN2, GPIO.OUT)

# GPIO.setup(battery1, GPIO.OUT)
# GPIO.setup(battery2, GPIO.OUT)

# GPIO.output(battery1, GPIO.HIGH)
# GPIO.output(battery2, GPIO.HIGH)

forward.start(100)
reverse.start(0)
time.sleep(3)
forward.stop()

print("??")
# GPIO.output(AEnable, GPIO.HIGH)
# forward.ChangeDutyCycle(0)
# reverse.ChangeDutyCycle(80)
# time.sleep(2)

# for i in range(5):
#     # GPIO.output(AIN1, GPIO.HIGH)
#     # GPIO.output(AIN2, GPIO.LOW)
#     GPIO.output(BIN1, GPIO.HIGH)
#     GPIO.output(BIN2, GPIO.LOW)


#     time.sleep(2)
#     # GPIO.output(AIN1,GPIO.LOW)
#     # GPIO.output(AIN2, GPIO.HIGH)
#     GPIO.output(BIN1,GPIO.LOW)
#     GPIO.output(BIN2, GPIO.HIGH)


#     time.sleep(2)
#     print("attempt9")

GPIO.cleanup()