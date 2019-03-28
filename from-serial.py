#!/usr/bin/python

import serial

port = serial.Serial("/dev/ttyACM0", baudrate = 9600, timeout = 3.0)  

while True:
    data = port.readline()
    print(data)
