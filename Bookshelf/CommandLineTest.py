import os
import sys
import serial
import time

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
#os.system(f"picocom -b 9600 -r -l {port}")
#os.system("5")
#ser = serial.Serial(
#        port=p,
#        baudrate=9600,
#        parity=serial.PARITY_NONE,
#        stopbits=serial.STOPBITS_ONE,
#        bytesize=serial.EIGHTBITS,
#        timeout=1)
ser = serial.Serial(port=p, baudrate=9600)
ser.flushInput()
time.sleep(3)
print("Done initializing")
command = "6"
ser.write(command.encode('utf-8'))
time.sleep(5)
while True:
    while (ser.inWaiting() == 0):
        pass
    x = ser.readline()
    print("Received from Arduino:", (x.decode('utf-8')).strip())
#lineIn = ser.read()
    #print("test", lineIn)
#ser.write(b'5')
#time.sleep(5)
#output = ser.readline()
#time.sleep(2)
ser.close()
#print(output)
