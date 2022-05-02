# Raspberry Pi Zero Base Station

## Hardware Requirements

### Raspberry Pi Zero

![Raspberry Pi Zero](https://raw.githubusercontent.com/Nanich87/raspberry-pi-zero-base-station/main/raspberry-pi-zero.avif "Raspberry Pi Zero")

![Raspberry Pi Zero Pinout](https://raw.githubusercontent.com/Nanich87/raspberry-pi-zero-base-station/main/rpi-gpio.png "Raspberry Pi Zero Pinout")

### MicroSD Card

### u-blox ZED-F9P

![ZED-F9P RTK InCase PIN GNSS receiver board with SMA and USB](https://raw.githubusercontent.com/Nanich87/raspberry-pi-zero-base-station/main/ublox-zed-f9p-rtk-gnss-receiver-board-with-sma-base-or-rover-top.jpg "ZED-F9P RTK InCase PIN GNSS receiver board with SMA and USB")

![ZED-F9P RTK InCase PIN GNSS receiver board with SMA and USB](https://raw.githubusercontent.com/Nanich87/raspberry-pi-zero-base-station/main/ublox-zed-f9p-rtk-gnss-receiver-board-with-sma-base-or-rover-bottom.jpg "ZED-F9P RTK InCase PIN GNSS receiver board with SMA and USB")

![ZED-F9P RTK InCase PIN GNSS receiver board with SMA and USB Pinout](https://raw.githubusercontent.com/Nanich87/raspberry-pi-zero-base-station/main/ublox-zed-f9p-rtk-gnss-receiver-board-with-sma-base-or-rover-pinout.jpg "ZED-F9P RTK InCase PIN GNSS receiver board with SMA and USB Pinout")

### GNSS Antenna

![L1 L2 GPS, G1 G2 GLONASS B1 B2 B3 BDS Galileo E1 E5b 40dB Antenna FOR RTK Base station. Full set with cable and stand](https://raw.githubusercontent.com/Nanich87/raspberry-pi-zero-base-station/main/antenna.jpg "L1 L2 GPS, G1 G2 GLONASS B1 B2 B3 BDS Galileo E1 E5b 40dB Antenna FOR RTK Base station. Full set with cable and stand")

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

## STL

### Part 1

![STL Part 1](https://raw.githubusercontent.com/Nanich87/raspberry-pi-zero-base-station/main/3d-model-part-1.png "STL Part 1")

### Part 2

![STL Part 2](https://raw.githubusercontent.com/Nanich87/raspberry-pi-zero-base-station/main/3d-model-part-2.png "STL Part 2")

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

## Start

Press the button once. The LED will start blinking.

## Stop

Press the button again. The LED will stop blinking.

## Shutdown

Hold the button for at least 2-3 seconds and the Pi will turn off.