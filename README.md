# Feed Device

This repository contains implementations to be hosted on the feeding device.

## Instructions

The folder `master` contains codes that are to be used in a RaspberryPi4 that is connected to a GrovePi board.

The folder `slave` contains codes that are to be used in an Arduino Nano RP2040.

The RaspberryPi4 depends on serial connection to the Arduino Nano RP2040 via USB.
For the stepper motor, ensure that it is connected to a motor driver such as a ULN2803.
The Nvidia Jetson communicates to the RaspberryPi4 and back using an external database of Firebase, such that the data transmitted can be stored and retrieved easily.

The `main.py` file is the main host for the RaspberryPi4 while an alternative for CSV files can be used in `main-csv.py`.
The `jetson.py` file is the main host for the Nvidia Jetson and will hold the Tensorflow Object Detection.

## Setup
![Example 1](IOT-Setup.png)

## Firebase JSON Database

![Example 2](firebase-json-example.PNG)