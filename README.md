# Raspberry Pi Zero Base Station

## Hardware Requirements

### Raspberry Pi Zero

![Raspberry Pi Zero](https://github.com/Nanich87/raspberry-pi-zero-base-station/blob/main/images/raspberry-pi-zero/raspberry-pi-zero.avif "Raspberry Pi Zero")

### MicroSD Card

16GB or 32GB MicroSD Card

### GNSS Receiver u-blox ZED-F9P

![ZED-F9P RTK InCase PIN GNSS receiver board with SMA and USB](https://github.com/Nanich87/raspberry-pi-zero-base-station/blob/main/images/gnss/ublox-zed-f9p-rtk-gnss-receiver-board-with-sma-base-or-rover-top.jpg "ZED-F9P RTK InCase PIN GNSS receiver board with SMA and USB")

![ZED-F9P RTK InCase PIN GNSS receiver board with SMA and USB](https://github.com/Nanich87/raspberry-pi-zero-base-station/blob/main/images/gnss/ublox-zed-f9p-rtk-gnss-receiver-board-with-sma-base-or-rover-bottom.jpg "ZED-F9P RTK InCase PIN GNSS receiver board with SMA and USB")

### GNSS Antenna

![L1 L2 GPS, G1 G2 GLONASS B1 B2 B3 BDS Galileo E1 E5b 40dB Antenna FOR RTK Base station. Full set with cable and stand](https://github.com/Nanich87/raspberry-pi-zero-base-station/blob/main/images/gnss/antenna.jpg "L1 L2 GPS, G1 G2 GLONASS B1 B2 B3 BDS Galileo E1 E5b 40dB Antenna FOR RTK Base station. Full set with cable and stand")

### Button

### LED

### Connectors/Wires

## Wiring

![Raspberry Pi Zero Pinout](https://github.com/Nanich87/raspberry-pi-zero-base-station/blob/main/images/raspberry-pi-zero/rpi-gpio.png "Raspberry Pi Zero Pinout")

![ZED-F9P RTK InCase PIN GNSS receiver board with SMA and USB Pinout](https://github.com/Nanich87/raspberry-pi-zero-base-station/blob/main/images/gnss/ublox-zed-f9p-rtk-gnss-receiver-board-with-sma-base-or-rover-pinout.jpg "ZED-F9P RTK InCase PIN GNSS receiver board with SMA and USB Pinout")

- Raspberry Pi GPIO14 (Pin #08) -> u-blox ZED-F9P RX
- Raspberry Pi GPIO15 (Pin #10) -> u-blox ZED-F9P TX
- Raspberry Pi DC Power 5v (Pin #04) -> u-blox ZED-F9P +5v
- Raspberry Pi Ground (Pin #06) -> u-blox ZED-F9P Ground
- Raspberry Pi GPIO21 (Pin #40) -> Button
- Raspberry Pi Ground (Pin #39) -> Button
- Raspberry Pi GPIO20 (Pin #38) -> LED+
- Raspberry Pi Ground (Pin #34) -> LED-

## Enclosure

### 3D Model / STL Files

#### Part 1 / Bottom

![STL Part 1](https://github.com/Nanich87/raspberry-pi-zero-base-station/blob/main/images/3d-model/3d-model-part-1.png "STL Part 1")

#### Part 2 / Top

![STL Part 2](https://github.com/Nanich87/raspberry-pi-zero-base-station/blob/main/images/3d-model/3d-model-part-2.png "STL Part 2")

## OS

<pre>
2021-05-07-raspios-buster-armhf-lite.img
</pre>

## Software Requerements

<pre>
sudo apt update

sudo apt upgrade
</pre>

### Prerequisites

<pre>
sudo apt install git

sudo apt install build-essential

sudo apt install automake

sudo apt install checkinstall

sudo apt install liblapack3

sudo apt install libblas3

sudo apt install gfortran
</pre>

### RTKLIB

#### Repository

<pre>
git clone https://github.com/rtklibexplorer/RTKLIB.git
</pre>

#### Build

<pre>
cd RTKLIB

cd app

cd consapp

sudo make

sudo make install
</pre>

## Operating Instructions

### Start

Press the button once. The LED will start blinking.

### Stop

Press the button again. The LED will stop blinking.

### Shutdown

Hold the button for at least 2-3 seconds and the Pi will turn off.
