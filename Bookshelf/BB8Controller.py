import os
import sys
import serial
import time
from tkinter import *

p = None
fqbn = "arduino:avr:uno"

#get port through second argument
for i, arg in enumerate(sys.argv):
    if i == 1:
        p = arg

print("Port: ", p)

print("Compiling...")
os.system(f"arduino-cli compile --fqbn {fqbn} MotorArduino")

print("Executing...")
os.system(f"arduino-cli upload -p {p} --fqbn {fqbn} MotorArduino")

print("Opening serial...")
ser = serial.Serial(port=p, baudrate=9600)
ser.flushInput()
time.sleep(3)

#set up tkinter window
window = Tk(className = "controller app")
window.geometry("200x200")
window.configure(bg = "white")
title = Label(window, text="BB8 Controller", bg = "white")
title.pack(pady = 20)

def sendCommandToArduino(command):
    #takes in command as a string
    ser.write(command.encode('utf-8'))
    while (ser.inWaiting() == 0):
        pass
    x = ser.readline()
    print("Received from Arduino:", (x.decode('utf-8')).strip())

def driveForward():
    sendCommandToArduino("1")
def driveBackward():
    sendCommandToArduino("2")
def driveLeft():
    sendCommandToArduino("4")
def driveRight():
    sendCommandToArduino("3")
def brake():
    sendCommandToArduino("5")

btnForward = Button(window, text = "forward", command = driveForward)
btnBackward = Button(window, text = "backward", command = driveBackward)
btnLeft = Button(window, text = "left", command = driveLeft)
btnRight = Button(window, text = "right", command = driveRight)
btnBrake = Button(window, text = "brake", command = brake, bg = "#FF7C73", activebackground = "#FC9992")
btnForward.place(anchor = S, relx = 0.5, rely = 0.4)
btnBackward.place(anchor = N, relx = 0.5, rely = 0.6)
btnLeft.place(anchor = E, rely = 0.5, relx = 0.45)
btnRight.place(anchor = W, rely = 0.5, relx = 0.55)
btnBrake.place(anchor = S, relx = 0.5, rely = 1, relwidth = 1)

print("Done initializing.")

mainloop()
ser.close()
time.sleep(0.2)
print("Port closed")
