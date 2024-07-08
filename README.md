# RedBack Racing SensorHub PCB ADC Validation using ENOB

The CANNode PCB gathers analogue sensor data to an 12-bit ADC chip, which then communicates via SPI to an STM32F446RET6 chip. The data is lightly processed and packaged into a CAN2.0-A packet and sent to the ECU via a full speed CANBUS. 
![CANNode4.0 2024](C:\Users\Public\Pictures\CANNode4.0.jpg)

## Introduction

This Repository contains the algorithm i used to perfrom Fourier Analysis on raw ADC data values that were parsed into a txt file. This code will output a ENOB value which is calculated using SNR (Signal to noise Ratio). It is better to use SINAD as this also accounts for harmonic distorion, however this is something i will improve on the future.

![Project Logo](https://example.com/path/to/logo.jpg)

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

Instructions on how to install the project.

```bash
# Example command to install
git clone https://github.com/username/repository.git
cd repository
