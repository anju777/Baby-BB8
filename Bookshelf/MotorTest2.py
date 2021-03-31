import RPi.GPIO as GPIO  
import time

# for GPIO numbering, choose BCM  
#GPIO.setmode(GPIO.BCM)  
  
# or, for pin numbering, choose BOARD  
GPIO.setmode(GPIO.BOARD)

# battery1 = 2
# battery2 = 4

AEnable = 13 #27
AIN1 = 22 #25
AIN2 = 18 #24
# BIN1 = 23  # 16
# BIN2 = 18  # 12

GPIO.setup(AEnable, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
# GPIO.setup(BIN1, GPIO.OUT)
# GPIO.setup(BIN2, GPIO.OUT)

# GPIO.setup(battery1, GPIO.OUT)
# GPIO.setup(battery2, GPIO.OUT)

# GPIO.output(battery1, GPIO.HIGH)
# GPIO.output(battery2, GPIO.HIGH)

for i in range(5):
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)
    GPIO.output(AEnable, GPIO.HIGH)
    # GPIO.output(BIN1, GPIO.HIGH)
    # GPIO.output(BIN2, GPIO.LOW)


    time.sleep(2)
    GPIO.output(AEnable, GPIO.LOW)
    # GPIO.output(AIN1,GPIO.LOW)
    # GPIO.output(AIN2, GPIO.HIGH)
    # GPIO.output(BIN1,GPIO.LOW)
    # GPIO.output(BIN2, GPIO.HIGH)


    time.sleep(2)
    print("attempt12")

GPIO.cleanup()
