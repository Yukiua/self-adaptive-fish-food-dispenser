import grovepi
import time
import datetime
import serial
import os

grovepi.set_bus("RPI_1")
# Connect the Grove Ultrasonic Ranger to digital port D4
ultrasonic_ranger = 4
pir_sensor = 7
motion=0
grovepi.pinMode(pir_sensor,"INPUT")
if os.stat("/home/pi/Desktop/test.csv").st_size == 0:
    file = open("/home/pi/Desktop/test.csv","a")
    file.write("Date,Time,Ultrasonic,MotionSensor,Humidity,Temperature\n")
    file.close()
ser = serial.Serial('/dev/ttyACM1',9600,timeout=0)
ser.flush()
while True:
    file = open("/home/pi/Desktop/test.csv","a")
    try:
        print(grovepi.ultrasonicRead(ultrasonic_ranger))
        motion=grovepi.digitalRead(pir_sensor)
        if motion==0 or motion==1:    # check if reads were 0 or 1 
            if motion==1:
                print ('Motion Deatected')
            else:
                print ('-')
        humidtemp = ser.readline().decode('utf-8').rstrip()
        humidity = str(humidtemp).split(',')[0]
        print("Humidity:",humidity)
        temperature = str(humidtemp).split(',')[1][0:5]
        print("Temp:",temperature)
        fulldate = str(datetime.datetime.now())
        dateE = fulldate.split(' ')[0]
        timeE = fulldate.split(' ')[1].split('.')[0]
        file.write("{0},{1},{2},{3},{4},{5}\n".format(dateE,timeE,str(grovepi.ultrasonicRead(ultrasonic_ranger)),str(motion),humidity,temperature))
        file.close()
        time.sleep(1)
    except Exception as e:
        print ("Error:{}".format(e))
    time.sleep(0.1)