#!/usr/bin/python2.7
import serial as ser
import time
import datetime

ser = ser.Serial(
    port = '/dev/ttyUSB0',
    baudrate = 9600,
    bytesize = ser.EIGHTBITS,
    parity = ser.PARITY_NONE,
    stopbits = ser.STOPBITS_ONE
)


#for i in range(3):     #here we created a for loop to read the temp every 10 seconds for n times in range(n)
 #   reading = ser.read(size=8)
  #  dt = datetime.datetime.utcnow().isoformat()
   # print dt, reading
    #time.sleep(10)

#for i in range(3):     #here we did as above but this introduces a time lag 
 #   print datetime.datetime.utcnow().isoformat(), ser.read(size=8)
  #  time.sleep(10)

#while ser.isOpen():     #here we created a for loop to read the temp every 10 seconds for n times in range(n)
 #   reading = ser.read(size=8)
  #  dt = datetime.datetime.utcnow().isoformat()
   # print dt, reading
    #time.sleep(10)

import io
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser, 1), encoding='ascii', newline='\r')

while ser.isOpen():   #here we created a for loop to read the temp every 10 seconds for n times in range(n)
    reading = ser.read(size=8)
    dt = datetime.datetime.utcnow().isoformat()
    print dt, reading
    
    