# Raspberry Pi Zero Base Station

## Hardware Requirements

### Raspberry Pi Zero

### u-blox ZED-F9P

![ZED-F9P RTK InCase PIN GNSS receiver board with SMA and USB](https://raw.githubusercontent.com/Nanich87/raspberry-pi-zero-base-station/main/ublox-zed-f9p-rtk-gnss-receiver-board-with-sma-base-or-rover.jpg "ZED-F9P RTK InCase PIN GNSS receiver board with SMA and USB")

![ZED-F9P RTK InCase PIN GNSS receiver board with SMA and USB Pinout](https://raw.githubusercontent.com/Nanich87/raspberry-pi-zero-base-station/main/ublox-zed-f9p-rtk-gnss-receiver-board-with-sma-base-or-rover-pinout.jpg "ZED-F9P RTK InCase PIN GNSS receiver board with SMA and USB Pinout")

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