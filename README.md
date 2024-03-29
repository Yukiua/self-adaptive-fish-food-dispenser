# Self Adaptive Fish Food Dispenser

The aim of this project is to use Computer Vision to capture the appetite of the fish and feed them in inverse proportion based on the percentage of fish food covering the camera screen. Using Computer Vision and Tensorflow, the goal is to provide real on-demand feeding requirements for target produces.


## Instructions

The folder `master` contains codes that are to be used in a RaspberryPi4 that is connected to a GrovePi board and the Nvidia Jetson Nano.


The `main.py` file in the raspberrypi folder is the main host for the RaspberryPi4 while an alternative for storing the output to CSV files can be found in `main-csv.py`.
The RaspberryPi4 is connected to the Arduino Nano RP2040 via USB.
The `run.py` file in the jetson folder is the main host for the Nvidia Jetson and will hold the Tensorflow Object Detection.
The `jetson.py` uses the RTSP of the cameras which are connected to the router to be captured and displayed through Python.
The `model.h5` is the trained AI model to be used to detect the feed percentage.


The Nvidia Jetson communicates to the RaspberryPi4 and back using an external database of Firebase, such that the data transmitted can be stored and retrieved easily.


The folder `slave` contains codes that are to be used in an Arduino Nano RP2040.


Each folder contains code for a Non-360 Servo Motor, a constant Stepper Motor speed, a 360 Stepper Motor, and a Humidity & Temperature Sensor.
For the stepper motor, ensure that it is connected to a motor driver such as a ULN2803.
The active code used for deployment are the HumidTemp code and the StepperMotor360 code.


## Image data example to train Tensorflow AI

![Example_4](master/jetson/example/feed_5.png)

## IOT Setup

The RaspberryPi4 connected to a GrovePi board, wired to 2 Arduinos.

![Example 1](IOT-Setup.png)

## Firebase JSON Database

Example of how the JSON file is stored.

![Example 2](firebase-json-example.PNG)

## Network

Network of the entire setup, along with their static IPv4 ranges.

![Example 3](network-setup.PNG)

## Sources

Ubuntu Tensorflow(depends on kernel) = [tensorflow-aarch64](https://github.com/KumaTea/tensorflow-aarch64/releases)

Device Manager/RSTP IP Finder = [ONVIF Device Manager](https://learncctv.com/onvif-device-manager/)

Real-Time Database = [Firebase](https://www.youtube.com/watch?v=qKxisFLQRpQ)

RaspberryPi GrovePi Library = [DexterIndustries](https://github.com/DexterInd/GrovePi)

Arduino: Stepper.h library, Arduino Nano RP2040 Standard Library, DHT Sensor Library
