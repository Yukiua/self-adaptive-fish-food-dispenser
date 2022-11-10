# Self Adaptive Fish Food Dispenser

The aim of this project is to use Computer Vision to capture the appetite of the fish and feed them in inverse proportion based on the percentage of fish food covering the camera screen.

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
