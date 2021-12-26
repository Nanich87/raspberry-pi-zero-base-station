# Raspberry Pi Zero Base Station

## Hardware Requirements

### Raspberry Pi Zero

### u-blox ZED-F9P

### Button

### LED

### Connectors/Wires

## OS

`2021-05-07-raspios-buster-armhf-lite.img`

## Software Requerements

`sudo apt update`

`sudo apt upgrade`

### Libs

`sudo apt install git`

`sudo apt install build-essential`

`sudo apt install automake`

`sudo apt install checkinstall`

`sudo apt install liblapack3`

`sudo apt install libblas3`

`sudo apt install gfortran`

### RTKLIB

`git clone https://github.com/rtklibexplorer/RTKLIB.git`

## Build

`cd RTKLIB`

`cd app`

`cd consapp`

`sudo make`

`sudo make install`