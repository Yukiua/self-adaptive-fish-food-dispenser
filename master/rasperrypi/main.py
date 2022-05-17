import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import grovepi
import time
import datetime
import serial
import os

def getMotorSpeed(): #This function retrieves from the firebase db under key motor, under key date;time, to get motor float value
    json = ref.get()
    speedster = 0
    for i in json:
        if(i == "motor"):
            for j in json.get(i):
                for k in json.get(i).get(j):
                    speedster = json.get(i).get(j).get(k)
                    #speedster = 1 - speedster #PENDING TO BE CHANGED DEPENDONG ON JETSON AI
    print("%.2f"%speedster)
    return speedster

#create your firebase db and put the certificate and database url here
cred = credentials.Certificate("CERTIFICATE.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://DATABASE.app'})

ref = db.reference('raspberrypi/')
users_ref = ref.child('rpi')
grovepi.set_bus("RPI_1")
# Connect the Grove Ultrasonic Ranger to D4, PIR Motion to D7
ultrasonic_ranger = 4
pir_sensor = 7
motion=0
grovepi.pinMode(pir_sensor,"INPUT")
ser = serial.Serial('/dev/ttyACM0',9600,timeout=0) #CHANGE DEPENDING ON /dev/ttyACM?
ser.flush()
ser1 = serial.Serial('dev/ttyACM1',9600,timeout=0) #CHANGE DEPENDING ON /dev/ttyACM?
ser1.flush()
print("waiting for arduino to come online")
time.sleep(5)

while True:
    try:
        # Read distance value from Ultrasonic
        print(grovepi.ultrasonicRead(ultrasonic_ranger))
        motion=grovepi.digitalRead(pir_sensor)
        if motion==0 or motion==1:	# check if reads were 0 or 1 it can be 255 also because of IO Errors so remove those values
            if motion==1:
                print ('Motion Detected')
            else:
                print ('-')
        humidtemp = ser.readline().decode('utf-8').rstrip()
        humidity = str(humidtemp).split(',')[0]
        print("Humidity:",humidity)
        temperature = str(humidtemp).split(',')[1][0:5]
        print("Temp:",temperature)
        fulldatetime = str(datetime.datetime.now())
        dateE = fulldatetime.split(' ')[0]
        timeE = fulldatetime.split(' ')[1].split('.')[0]
        motor = print(getMotorSpeed())
        ser1.write("{0}".format(motor).encode("UTF-8"))
        #Append the data to the child of the reference to be set in the json
        users_ref.child("{0};{1}".format(dateE,timeE)).set({
            "Date":dateE,
            "Time":timeE,
            "Motion":str(motion),
            "Ultrasonic":str(grovepi.ultrasonicRead(ultrasonic_ranger)),
            "Humidity":humidity,
            "Temperature":temperature})
        #Save the reference to a specific path in the db
        handle = db.reference('raspberrypi/rpi/{0};{1}'.format(dateE,timeE))
        # if your hold time is less than this, you might not see as many detections
        time.sleep(1)
    except Exception as e:
        print ("Error:{}".format(e))
    time.sleep(10) # don't overload the i2c bus
print(ref.get())# To view json file from reference