# Raspberry Pi Zero Base Station

## Hardware Requirements

### Raspberry Pi Zero

![Raspberry Pi Zero](https://raw.githubusercontent.com/Nanich87/raspberry-pi-zero-base-station/main/raspberry-pi-zero.avif "Raspberry Pi Zero")

![Raspberry Pi Zero Pinout](https://raw.githubusercontent.com/Nanich87/raspberry-pi-zero-base-station/main/rpi-gpio.png "Raspberry Pi Zero Pinout")

### u-blox ZED-F9P

![ZED-F9P RTK InCase PIN GNSS receiver board with SMA and USB](https://raw.githubusercontent.com/Nanich87/raspberry-pi-zero-base-station/main/ublox-zed-f9p-rtk-gnss-receiver-board-with-sma-base-or-rover.jpg "ZED-F9P RTK InCase PIN GNSS receiver board with SMA and USB")

![ZED-F9P RTK InCase PIN GNSS receiver board with SMA and USB Pinout](https://raw.githubusercontent.com/Nanich87/raspberry-pi-zero-base-station/main/ublox-zed-f9p-rtk-gnss-receiver-board-with-sma-base-or-rover-pinout.jpg "ZED-F9P RTK InCase PIN GNSS receiver board with SMA and USB Pinout")

### Button

### LED

### Connectors/Wires

## Wiring

- Raspberry Pi GPIO14 (Pin #08) -> u-blox ZED-F9P RX
- Raspberry Pi GPIO15 (Pin #10) -> u-blox ZED-F9P TX
- Raspberry Pi DC Power 5v (Pin #04) -> u-blox ZED-F9P +5v
- Raspberry Pi Ground (Pin #06) -> u-blox ZED-F9P Ground
- Raspberry Pi GPIO21 (Pin #40) -> Button
- Raspberry Pi Ground (Pin #39) -> Button
- Raspberry Pi GPIO20 (Pin #38) -> LED+
- Raspberry Pi Ground (Pin #34) -> LED-

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

## Run

`python /home/pi/basestation.py`