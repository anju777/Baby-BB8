from gpiozero import LED
import time
#import RPI.GPIO as GPIO

#3y? 18
#2a? 16
#12: 1A, 22: 4a

# motor1 = Motor(18, 23)
# motor2 = Motor(24, 25)

BIN1 = LED(18)  # 16


for i in range(5):
    # motor1.forward()
    # motor2.forward()

    BIN1.on()
    time.sleep(3)
    print("LED off")
    BIN1.off()
    time.sleep(3)
    print("LED on")
