from gpiozero import Motor
from time import sleep

motor1 = Motor(18, 23)

motor1.forward()
while True:
    print("ahhh")
    sleep(5)
    motor1.reverse()
    sleep(5)
