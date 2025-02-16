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

### Raspberry Pi Zero Pinout

![Raspberry Pi Zero Pinout](https://github.com/Nanich87/raspberry-pi-zero-base-station/blob/main/images/raspberry-pi-zero/rpi-gpio.png "Raspberry Pi Zero Pinout")

### u-blox ZED-F9P Pinout

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

```stl
solid Mesh
  facet normal 0.991445 0.130522 0.000000
    outer loop
      vertex 4.250001 372.183990 2.000001
      vertex 4.304520 371.769867 2.000001
      vertex 4.304520 371.769867 0.000001
    endloop
  endfacet
  facet normal 0.991445 0.130522 -0.000000
    outer loop
      vertex 4.250001 372.183990 0.000001
      vertex 4.250001 372.183990 2.000001
      vertex 4.304520 371.769867 0.000001
    endloop
  endfacet
  facet normal 0.991444 -0.130532 0.000000
    outer loop
      vertex 4.304520 372.598083 2.000001
      vertex 4.250001 372.183990 2.000001
      vertex 4.250001 372.183990 0.000001
    endloop
  endfacet
  facet normal 0.991444 -0.130532 0.000000
    outer loop
      vertex 4.304520 372.598083 0.000001
      vertex 4.304520 372.598083 2.000001
      vertex 4.250001 372.183990 0.000001
    endloop
  endfacet
  facet normal 0.923881 -0.382679 0.000000
    outer loop
      vertex 4.464360 372.983978 2.000001
      vertex 4.304520 372.598083 2.000001
      vertex 4.304520 372.598083 0.000001
    endloop
  endfacet
  facet normal 0.923881 -0.382679 0.000000
    outer loop
      vertex 4.464360 372.983978 0.000001
      vertex 4.464360 372.983978 2.000001
      vertex 4.304520 372.598083 0.000001
    endloop
  endfacet
  facet normal 0.793370 -0.608739 0.000000
    outer loop
      vertex 4.718630 373.315369 2.000001
      vertex 4.464360 372.983978 2.000001
      vertex 4.464360 372.983978 0.000001
    endloop
  endfacet
  facet normal 0.793370 -0.608739 0.000000
    outer loop
      vertex 4.718630 373.315369 0.000001
      vertex 4.718630 373.315369 2.000001
      vertex 4.464360 372.983978 0.000001
    endloop
  endfacet
  facet normal 0.608719 -0.793386 0.000000
    outer loop
      vertex 5.050001 373.569611 2.000001
      vertex 4.718630 373.315369 2.000001
      vertex 4.718630 373.315369 0.000001
    endloop
  endfacet
  facet normal 0.608719 -0.793386 0.000000
    outer loop
      vertex 5.050001 373.569611 0.000001
      vertex 5.050001 373.569611 2.000001
      vertex 4.718630 373.315369 0.000001
    endloop
  endfacet
  facet normal 0.382705 -0.923871 0.000000
    outer loop
      vertex 5.435891 373.729462 2.000001
      vertex 5.050001 373.569611 2.000001
      vertex 5.050001 373.569611 0.000001
    endloop
  endfacet
  facet normal 0.382705 -0.923871 0.000000
    outer loop
      vertex 5.435891 373.729462 0.000001
      vertex 5.435891 373.729462 2.000001
      vertex 5.050001 373.569611 0.000001
    endloop
  endfacet
  facet normal 0.130564 -0.991440 0.000000
    outer loop
      vertex 5.850001 373.783997 2.000001
      vertex 5.435891 373.729462 2.000001
      vertex 5.435891 373.729462 0.000001
    endloop
  endfacet
  facet normal 0.130564 -0.991440 0.000000
    outer loop
      vertex 5.850001 373.783997 0.000001
      vertex 5.850001 373.783997 2.000001
      vertex 5.435891 373.729462 0.000001
    endloop
  endfacet
  facet normal -0.130564 -0.991440 0.000000
    outer loop
      vertex 6.264112 373.729462 2.000001
      vertex 5.850001 373.783997 2.000001
      vertex 5.850001 373.783997 0.000001
    endloop
  endfacet
  facet normal -0.130564 -0.991440 0.000000
    outer loop
      vertex 6.264112 373.729462 0.000001
      vertex 6.264112 373.729462 2.000001
      vertex 5.850001 373.783997 0.000001
    endloop
  endfacet
  facet normal -0.382705 -0.923871 0.000000
    outer loop
      vertex 6.650001 373.569611 2.000001
      vertex 6.264112 373.729462 2.000001
      vertex 6.264112 373.729462 0.000001
    endloop
  endfacet
  facet normal -0.382705 -0.923871 0.000000
    outer loop
      vertex 6.650001 373.569611 0.000001
      vertex 6.650001 373.569611 2.000001
      vertex 6.264112 373.729462 0.000001
    endloop
  endfacet
  facet normal -0.608719 -0.793386 0.000000
    outer loop
      vertex 6.981372 373.315369 2.000001
      vertex 6.650001 373.569611 2.000001
      vertex 6.650001 373.569611 0.000001
    endloop
  endfacet
  facet normal -0.608719 -0.793386 0.000000
    outer loop
      vertex 6.981372 373.315369 0.000001
      vertex 6.981372 373.315369 2.000001
      vertex 6.650001 373.569611 0.000001
    endloop
  endfacet
  facet normal -0.793371 -0.608739 0.000000
    outer loop
      vertex 7.235641 372.983978 2.000001
      vertex 6.981372 373.315369 2.000001
      vertex 6.981372 373.315369 0.000001
    endloop
  endfacet
  facet normal -0.793371 -0.608739 0.000000
    outer loop
      vertex 7.235641 372.983978 0.000001
      vertex 7.235641 372.983978 2.000001
      vertex 6.981372 373.315369 0.000001
    endloop
  endfacet
  facet normal -0.923881 -0.382680 0.000000
    outer loop
      vertex 7.395483 372.598083 2.000001
      vertex 7.235641 372.983978 2.000001
      vertex 7.235641 372.983978 0.000001
    endloop
  endfacet
  facet normal -0.923881 -0.382680 0.000000
    outer loop
      vertex 7.395483 372.598083 0.000001
      vertex 7.395483 372.598083 2.000001
      vertex 7.235641 372.983978 0.000001
    endloop
  endfacet
  facet normal -0.991444 -0.130531 0.000000
    outer loop
      vertex 7.450001 372.183990 2.000001
      vertex 7.395483 372.598083 2.000001
      vertex 7.395483 372.598083 0.000001
    endloop
  endfacet
  facet normal -0.991444 -0.130531 0.000000
    outer loop
      vertex 7.450001 372.183990 0.000001
      vertex 7.450001 372.183990 2.000001
      vertex 7.395483 372.598083 0.000001
    endloop
  endfacet
  facet normal -0.991446 0.130521 0.000000
    outer loop
      vertex 7.395483 371.769867 2.000001
      vertex 7.450001 372.183990 2.000001
      vertex 7.450001 372.183990 0.000001
    endloop
  endfacet
  facet normal -0.991446 0.130521 0.000000
    outer loop
      vertex 7.395483 371.769867 0.000001
      vertex 7.395483 371.769867 2.000001
      vertex 7.450001 372.183990 0.000001
    endloop
  endfacet
  facet normal -0.923881 0.382680 0.000000
    outer loop
      vertex 7.235641 371.383972 2.000001
      vertex 7.395483 371.769867 2.000001
      vertex 7.395483 371.769867 0.000001
    endloop
  endfacet
  facet normal -0.923881 0.382680 0.000000
    outer loop
      vertex 7.235641 371.383972 0.000001
      vertex 7.235641 371.383972 2.000001
      vertex 7.395483 371.769867 0.000001
    endloop
  endfacet
  facet normal -0.793344 0.608774 0.000000
    outer loop
      vertex 6.981372 371.052612 2.000001
      vertex 7.235641 371.383972 2.000001
      vertex 7.235641 371.383972 0.000001
    endloop
  endfacet
  facet normal -0.793344 0.608774 0.000000
    outer loop
      vertex 6.981372 371.052612 0.000001
      vertex 6.981372 371.052612 2.000001
      vertex 7.235641 371.383972 0.000001
    endloop
  endfacet
  facet normal -0.608765 0.793350 0.000000
    outer loop
      vertex 6.650001 370.798340 2.000001
      vertex 6.981372 371.052612 2.000001
      vertex 6.981372 371.052612 0.000001
    endloop
  endfacet
  facet normal -0.608765 0.793350 0.000000
    outer loop
      vertex 6.650001 370.798340 0.000001
      vertex 6.650001 370.798340 2.000001
      vertex 6.981372 371.052612 0.000001
    endloop
  endfacet
  facet normal -0.382705 0.923871 0.000000
    outer loop
      vertex 6.264112 370.638489 2.000001
      vertex 6.650001 370.798340 2.000001
      vertex 6.650001 370.798340 0.000001
    endloop
  endfacet
  facet normal -0.382705 0.923871 0.000000
    outer loop
      vertex 6.264112 370.638489 0.000001
      vertex 6.264112 370.638489 2.000001
      vertex 6.650001 370.798340 0.000001
    endloop
  endfacet
  facet normal -0.130493 0.991449 0.000000
    outer loop
      vertex 5.850001 370.583984 2.000001
      vertex 6.264112 370.638489 2.000001
      vertex 6.264112 370.638489 0.000001
    endloop
  endfacet
  facet normal -0.130493 0.991449 0.000000
    outer loop
      vertex 5.850001 370.583984 0.000001
      vertex 5.850001 370.583984 2.000001
      vertex 6.264112 370.638489 0.000001
    endloop
  endfacet
  facet normal 0.130493 0.991449 0.000000
    outer loop
      vertex 5.435891 370.638489 2.000001
      vertex 5.850001 370.583984 2.000001
      vertex 5.850001 370.583984 0.000001
    endloop
  endfacet
  facet normal 0.130493 0.991449 -0.000000
    outer loop
      vertex 5.435891 370.638489 0.000001
      vertex 5.435891 370.638489 2.000001
      vertex 5.850001 370.583984 0.000001
    endloop
  endfacet
  facet normal 0.382705 0.923871 0.000000
    outer loop
      vertex 5.050001 370.798340 2.000001
      vertex 5.435891 370.638489 2.000001
      vertex 5.435891 370.638489 0.000001
    endloop
  endfacet
  facet normal 0.382705 0.923871 -0.000000
    outer loop
      vertex 5.050001 370.798340 0.000001
      vertex 5.050001 370.798340 2.000001
      vertex 5.435891 370.638489 0.000001
    endloop
  endfacet
  facet normal 0.608765 0.793350 0.000000
    outer loop
      vertex 4.718630 371.052612 2.000001
      vertex 5.050001 370.798340 2.000001
      vertex 5.050001 370.798340 0.000001
    endloop
  endfacet
  facet normal 0.608765 0.793350 -0.000000
    outer loop
      vertex 4.718630 371.052612 0.000001
      vertex 4.718630 371.052612 2.000001
      vertex 5.050001 370.798340 0.000001
    endloop
  endfacet
  facet normal 0.793343 0.608775 0.000000
    outer loop
      vertex 4.464360 371.383972 2.000001
      vertex 4.718630 371.052612 2.000001
      vertex 4.718630 371.052612 0.000001
    endloop
  endfacet
  facet normal 0.793343 0.608775 -0.000000
    outer loop
      vertex 4.464360 371.383972 0.000001
      vertex 4.464360 371.383972 2.000001
      vertex 4.718630 371.052612 0.000001
    endloop
  endfacet
  facet normal 0.923881 0.382679 0.000000
    outer loop
      vertex 4.304520 371.769867 2.000001
      vertex 4.464360 371.383972 2.000001
      vertex 4.464360 371.383972 0.000001
    endloop
  endfacet
  facet normal 0.923881 0.382679 -0.000000
    outer loop
      vertex 4.304520 371.769867 0.000001
      vertex 4.304520 371.769867 2.000001
      vertex 4.464360 371.383972 0.000001
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 1.854447 367.925476 0.000001
      vertex 8.354447 367.925476 0.000001
      vertex 8.354447 367.925476 2.000001
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 1.854447 367.925476 2.000001
      vertex 1.854447 367.925476 0.000001
      vertex 8.354447 367.925476 2.000001
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.854447 361.425476 0.000001
      vertex 1.854447 367.925476 0.000001
      vertex 1.854447 367.925476 2.000001
    endloop
  endfacet
  facet normal 1.000000 -0.000000 0.000000
    outer loop
      vertex 1.854447 361.425476 2.000001
      vertex 1.854447 361.425476 0.000001
      vertex 1.854447 367.925476 2.000001
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 8.354447 367.925476 0.000001
      vertex 8.354447 361.425476 0.000001
      vertex 8.354447 361.425476 2.000001
    endloop
  endfacet
  facet normal -1.000000 -0.000000 -0.000000
    outer loop
      vertex 8.354447 367.925476 2.000001
      vertex 8.354447 367.925476 0.000001
      vertex 8.354447 361.425476 2.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 4.250001 372.183990 2.000001
      vertex 4.304520 372.598083 2.000001
      vertex 2.850001 375.073029 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 1.854447 367.925476 2.000001
      vertex 4.250001 372.183990 2.000001
      vertex 2.850001 375.073029 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 4.304520 371.769867 2.000001
      vertex 4.250001 372.183990 2.000001
      vertex 1.854447 367.925476 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 4.464360 371.383972 2.000001
      vertex 4.304520 371.769867 2.000001
      vertex 1.854447 367.925476 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 4.718630 371.052612 2.000001
      vertex 4.464360 371.383972 2.000001
      vertex 1.854447 367.925476 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 5.050001 370.798340 2.000001
      vertex 4.718630 371.052612 2.000001
      vertex 1.854447 367.925476 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 5.435891 370.638489 2.000001
      vertex 5.050001 370.798340 2.000001
      vertex 1.854447 367.925476 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 8.354447 367.925476 2.000001
      vertex 5.435891 370.638489 2.000001
      vertex 1.854447 367.925476 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 5.850001 370.583984 2.000001
      vertex 5.435891 370.638489 2.000001
      vertex 8.354447 367.925476 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 6.264112 370.638489 2.000001
      vertex 5.850001 370.583984 2.000001
      vertex 8.354447 367.925476 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 6.650001 370.798340 2.000001
      vertex 6.264112 370.638489 2.000001
      vertex 8.354447 367.925476 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 6.981372 371.052612 2.000001
      vertex 6.650001 370.798340 2.000001
      vertex 8.354447 367.925476 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 7.235641 371.383972 2.000001
      vertex 6.981372 371.052612 2.000001
      vertex 8.354447 367.925476 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 7.395483 371.769867 2.000001
      vertex 7.235641 371.383972 2.000001
      vertex 8.354447 367.925476 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 7.450001 372.183990 2.000001
      vertex 7.395483 371.769867 2.000001
      vertex 8.354447 367.925476 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 8.850001 375.073029 2.000001
      vertex 7.450001 372.183990 2.000001
      vertex 8.354447 367.925476 2.000001
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 7.395483 372.598083 2.000001
      vertex 7.450001 372.183990 2.000001
      vertex 8.850001 375.073029 2.000001
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 7.235641 372.983978 2.000001
      vertex 7.395483 372.598083 2.000001
      vertex 8.850001 375.073029 2.000001
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 6.981372 373.315369 2.000001
      vertex 7.235641 372.983978 2.000001
      vertex 8.850001 375.073029 2.000001
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 6.650001 373.569611 2.000001
      vertex 6.981372 373.315369 2.000001
      vertex 8.850001 375.073029 2.000001
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 6.264112 373.729462 2.000001
      vertex 6.650001 373.569611 2.000001
      vertex 8.850001 375.073029 2.000001
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 5.850001 373.783997 2.000001
      vertex 6.264112 373.729462 2.000001
      vertex 8.850001 375.073029 2.000001
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 2.850001 375.073029 2.000001
      vertex 5.850001 373.783997 2.000001
      vertex 8.850001 375.073029 2.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 5.435891 373.729462 2.000001
      vertex 5.850001 373.783997 2.000001
      vertex 2.850001 375.073029 2.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 5.050001 373.569611 2.000001
      vertex 5.435891 373.729462 2.000001
      vertex 2.850001 375.073029 2.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 4.718630 373.315369 2.000001
      vertex 5.050001 373.569611 2.000001
      vertex 2.850001 375.073029 2.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 4.464360 372.983978 2.000001
      vertex 4.718630 373.315369 2.000001
      vertex 2.850001 375.073029 2.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 4.304520 372.598083 2.000001
      vertex 4.464360 372.983978 2.000001
      vertex 2.850001 375.073029 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 8.850001 380.073029 2.000001
      vertex 8.850001 375.073029 2.000001
      vertex 36.845554 361.425476 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 39.350002 390.823029 2.000001
      vertex 8.850001 380.073029 2.000001
      vertex 36.845554 361.425476 2.000001
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 1.850001 390.823029 2.000001
      vertex 8.850001 380.073029 2.000001
      vertex 39.350002 390.823029 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 1.854447 367.925476 2.000001
      vertex 2.850001 375.073029 2.000001
      vertex 2.850001 380.073029 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 1.850001 390.823029 2.000001
      vertex 1.854447 367.925476 2.000001
      vertex 2.850001 380.073029 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 0.000001 350.073029 2.000001
      vertex 1.854447 367.925476 2.000001
      vertex 1.850001 390.823029 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 0.000001 420.073029 2.000001
      vertex 0.000001 350.073029 2.000001
      vertex 1.850001 390.823029 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 1.850001 410.823029 2.000001
      vertex 0.000001 420.073029 2.000001
      vertex 1.850001 390.823029 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 1.600001 421.673004 2.000001
      vertex 0.000001 420.073029 2.000001
      vertex 1.850001 410.823029 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 39.350002 410.823029 2.000001
      vertex 1.600001 421.673004 2.000001
      vertex 1.850001 410.823029 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 39.600002 421.673004 2.000001
      vertex 1.600001 421.673004 2.000001
      vertex 39.350002 410.823029 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 41.200001 420.073029 2.000001
      vertex 39.600002 421.673004 2.000001
      vertex 39.350002 410.823029 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 40.014111 421.618500 2.000001
      vertex 39.600002 421.673004 2.000001
      vertex 41.200001 420.073029 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 40.400002 421.458649 2.000001
      vertex 40.014111 421.618500 2.000001
      vertex 41.200001 420.073029 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 40.731373 421.204376 2.000001
      vertex 40.400002 421.458649 2.000001
      vertex 41.200001 420.073029 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 40.985641 420.873016 2.000001
      vertex 40.731373 421.204376 2.000001
      vertex 41.200001 420.073029 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 41.145481 420.487122 2.000001
      vertex 40.985641 420.873016 2.000001
      vertex 41.200001 420.073029 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 1.850001 390.823029 2.000001
      vertex 2.850001 380.073029 2.000001
      vertex 8.850001 380.073029 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 41.200001 420.073029 2.000001
      vertex 39.350002 410.823029 2.000001
      vertex 39.350002 390.823029 2.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 41.200001 350.073029 2.000001
      vertex 41.200001 420.073029 2.000001
      vertex 39.350002 390.823029 2.000001
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 39.345554 361.425476 2.000001
      vertex 41.200001 350.073029 2.000001
      vertex 39.350002 390.823029 2.000001
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 39.345554 356.425476 2.000001
      vertex 41.200001 350.073029 2.000001
      vertex 39.345554 361.425476 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 39.600002 348.473022 2.000001
      vertex 40.014111 348.527527 2.000001
      vertex 41.200001 350.073029 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 39.345554 356.425476 2.000001
      vertex 39.600002 348.473022 2.000001
      vertex 41.200001 350.073029 2.000001
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 36.845554 356.425476 2.000001
      vertex 39.600002 348.473022 2.000001
      vertex 39.345554 356.425476 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 41.200001 350.073029 2.000001
      vertex 40.014111 348.527527 2.000001
      vertex 40.400002 348.687378 2.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 40.731373 348.941650 2.000001
      vertex 41.200001 350.073029 2.000001
      vertex 40.400002 348.687378 2.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 40.985641 349.273010 2.000001
      vertex 41.200001 350.073029 2.000001
      vertex 40.731373 348.941650 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 41.200001 350.073029 2.000001
      vertex 40.985641 349.273010 2.000001
      vertex 41.145481 349.658905 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 0.000001 420.073029 2.000001
      vertex 1.600001 421.673004 2.000001
      vertex 1.185891 421.618500 2.000001
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 0.800001 421.458649 2.000001
      vertex 0.000001 420.073029 2.000001
      vertex 1.185891 421.618500 2.000001
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 0.468630 421.204376 2.000001
      vertex 0.000001 420.073029 2.000001
      vertex 0.800001 421.458649 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 0.000001 420.073029 2.000001
      vertex 0.468630 421.204376 2.000001
      vertex 0.214360 420.873016 2.000001
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 0.054520 420.487122 2.000001
      vertex 0.000001 420.073029 2.000001
      vertex 0.214360 420.873016 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 0.000001 350.073029 2.000001
      vertex 0.054520 349.658905 2.000001
      vertex 0.214360 349.273010 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 0.468630 348.941650 2.000001
      vertex 0.000001 350.073029 2.000001
      vertex 0.214360 349.273010 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 0.800001 348.687378 2.000001
      vertex 0.000001 350.073029 2.000001
      vertex 0.468630 348.941650 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 0.000001 350.073029 2.000001
      vertex 0.800001 348.687378 2.000001
      vertex 1.185891 348.527527 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 1.600001 348.473022 2.000001
      vertex 0.000001 350.073029 2.000001
      vertex 1.185891 348.527527 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 1.854447 356.425476 2.000001
      vertex 0.000001 350.073029 2.000001
      vertex 1.600001 348.473022 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 4.354447 356.425476 2.000001
      vertex 1.854447 356.425476 2.000001
      vertex 1.600001 348.473022 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 8.354447 361.425476 2.000001
      vertex 4.354447 356.425476 2.000001
      vertex 1.600001 348.473022 2.000001
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 4.354447 361.425476 2.000001
      vertex 4.354447 356.425476 2.000001
      vertex 8.354447 361.425476 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 8.354447 361.425476 2.000001
      vertex 1.600001 348.473022 2.000001
      vertex 39.600002 348.473022 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 36.845554 356.425476 2.000001
      vertex 8.354447 361.425476 2.000001
      vertex 39.600002 348.473022 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 36.845554 361.425476 2.000001
      vertex 8.354447 361.425476 2.000001
      vertex 36.845554 356.425476 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 39.350002 390.823029 2.000001
      vertex 36.845554 361.425476 2.000001
      vertex 39.345554 361.425476 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 0.000001 350.073029 2.000001
      vertex 1.854447 356.425476 2.000001
      vertex 1.854447 361.425476 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 1.854447 367.925476 2.000001
      vertex 0.000001 350.073029 2.000001
      vertex 1.854447 361.425476 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 36.845554 361.425476 2.000001
      vertex 8.850001 375.073029 2.000001
      vertex 8.354447 367.925476 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 8.354447 361.425476 2.000001
      vertex 36.845554 361.425476 2.000001
      vertex 8.354447 367.925476 2.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 4.354447 356.425476 4.000001
      vertex 4.354447 361.425476 4.000001
      vertex 1.854447 361.425476 4.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 1.854447 356.425476 4.000001
      vertex 4.354447 356.425476 4.000001
      vertex 1.854447 361.425476 4.000001
    endloop
  endfacet
  facet normal -0.000000 -1.000000 0.000000
    outer loop
      vertex 4.354447 356.425476 4.000001
      vertex 1.854447 356.425476 4.000001
      vertex 1.854447 356.425476 2.000001
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 4.354447 356.425476 2.000001
      vertex 4.354447 356.425476 4.000001
      vertex 1.854447 356.425476 2.000001
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 1.854447 356.425476 4.000001
      vertex 1.854447 361.425476 4.000001
      vertex 1.854447 361.425476 2.000001
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 1.854447 356.425476 2.000001
      vertex 1.854447 356.425476 4.000001
      vertex 1.854447 361.425476 2.000001
    endloop
  endfacet
  facet normal -0.000000 1.000000 0.000000
    outer loop
      vertex 1.854447 361.425476 4.000001
      vertex 4.354447 361.425476 4.000001
      vertex 4.354447 361.425476 2.000001
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 1.854447 361.425476 2.000001
      vertex 1.854447 361.425476 4.000001
      vertex 4.354447 361.425476 2.000001
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 1.854447 361.425476 0.000001
      vertex 1.854447 361.425476 2.000001
      vertex 4.354447 361.425476 2.000001
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 8.354447 361.425476 0.000001
      vertex 1.854447 361.425476 0.000001
      vertex 4.354447 361.425476 2.000001
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 8.354447 361.425476 2.000001
      vertex 8.354447 361.425476 0.000001
      vertex 4.354447 361.425476 2.000001
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 4.354447 361.425476 4.000001
      vertex 4.354447 356.425476 4.000001
      vertex 4.354447 356.425476 2.000001
    endloop
  endfacet
  facet normal 1.000000 0.000000 -0.000000
    outer loop
      vertex 4.354447 361.425476 2.000001
      vertex 4.354447 361.425476 4.000001
      vertex 4.354447 356.425476 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 36.845554 361.425476 4.000001
      vertex 36.845554 356.425476 4.000001
      vertex 39.345554 356.425476 4.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 39.345554 361.425476 4.000001
      vertex 36.845554 361.425476 4.000001
      vertex 39.345554 356.425476 4.000001
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 36.845554 356.425476 2.000001
      vertex 39.345554 356.425476 2.000001
      vertex 39.345554 356.425476 4.000001
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 36.845554 356.425476 4.000001
      vertex 36.845554 356.425476 2.000001
      vertex 39.345554 356.425476 4.000001
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 39.345554 356.425476 2.000001
      vertex 39.345554 361.425476 2.000001
      vertex 39.345554 361.425476 4.000001
    endloop
  endfacet
  facet normal 1.000000 -0.000000 0.000000
    outer loop
      vertex 39.345554 356.425476 4.000001
      vertex 39.345554 356.425476 2.000001
      vertex 39.345554 361.425476 4.000001
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 39.345554 361.425476 2.000001
      vertex 36.845554 361.425476 2.000001
      vertex 36.845554 361.425476 4.000001
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 39.345554 361.425476 4.000001
      vertex 39.345554 361.425476 2.000001
      vertex 36.845554 361.425476 4.000001
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 36.845554 361.425476 2.000001
      vertex 36.845554 356.425476 2.000001
      vertex 36.845554 356.425476 4.000001
    endloop
  endfacet
  facet normal -1.000000 -0.000000 -0.000000
    outer loop
      vertex 36.845554 361.425476 4.000001
      vertex 36.845554 361.425476 2.000001
      vertex 36.845554 356.425476 4.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 39.350002 410.823029 6.000001
      vertex 2.850001 410.823029 6.000001
      vertex 32.267658 398.996338 6.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 32.850002 399.073029 6.000001
      vertex 39.350002 410.823029 6.000001
      vertex 32.267658 398.996338 6.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 33.432343 398.996338 6.000001
      vertex 39.350002 410.823029 6.000001
      vertex 32.850002 399.073029 6.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 2.850001 410.823029 6.000001
      vertex 2.850001 390.823029 6.000001
      vertex 30.901443 397.948029 6.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 31.259010 398.414001 6.000001
      vertex 2.850001 410.823029 6.000001
      vertex 30.901443 397.948029 6.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 31.725000 398.771576 6.000001
      vertex 2.850001 410.823029 6.000001
      vertex 31.259010 398.414001 6.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 2.850001 390.823029 6.000001
      vertex 39.350002 390.823029 6.000001
      vertex 32.267658 394.649689 6.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 31.725000 394.874451 6.000001
      vertex 2.850001 390.823029 6.000001
      vertex 32.267658 394.649689 6.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 31.259010 395.232025 6.000001
      vertex 2.850001 390.823029 6.000001
      vertex 31.725000 394.874451 6.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 39.350002 390.823029 6.000001
      vertex 39.350002 410.823029 6.000001
      vertex 35.023335 397.405365 6.000001
    endloop
  endfacet
  facet normal -0.000000 -0.000000 1.000000
    outer loop
      vertex 35.100002 396.823029 6.000001
      vertex 39.350002 390.823029 6.000001
      vertex 35.023335 397.405365 6.000001
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 35.023335 396.240662 6.000001
      vertex 39.350002 390.823029 6.000001
      vertex 35.100002 396.823029 6.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 39.350002 390.823029 6.000001
      vertex 35.023335 396.240662 6.000001
      vertex 34.798557 395.698029 6.000001
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 34.440990 395.232025 6.000001
      vertex 39.350002 390.823029 6.000001
      vertex 34.798557 395.698029 6.000001
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 33.975002 394.874451 6.000001
      vertex 39.350002 390.823029 6.000001
      vertex 34.440990 395.232025 6.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 39.350002 390.823029 6.000001
      vertex 33.975002 394.874451 6.000001
      vertex 33.432343 394.649689 6.000001
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 32.850002 394.573029 6.000001
      vertex 39.350002 390.823029 6.000001
      vertex 33.432343 394.649689 6.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 32.267658 394.649689 6.000001
      vertex 39.350002 390.823029 6.000001
      vertex 32.850002 394.573029 6.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 2.850001 390.823029 6.000001
      vertex 31.259010 395.232025 6.000001
      vertex 30.901443 395.698029 6.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 30.676668 396.240662 6.000001
      vertex 2.850001 390.823029 6.000001
      vertex 30.901443 395.698029 6.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 30.600000 396.823029 6.000001
      vertex 2.850001 390.823029 6.000001
      vertex 30.676668 396.240662 6.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 2.850001 390.823029 6.000001
      vertex 30.600000 396.823029 6.000001
      vertex 30.676668 397.405365 6.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 30.901443 397.948029 6.000001
      vertex 2.850001 390.823029 6.000001
      vertex 30.676668 397.405365 6.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 2.850001 410.823029 6.000001
      vertex 31.725000 398.771576 6.000001
      vertex 32.267658 398.996338 6.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 39.350002 410.823029 6.000001
      vertex 33.432343 398.996338 6.000001
      vertex 33.975002 398.771576 6.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 34.440990 398.414001 6.000001
      vertex 39.350002 410.823029 6.000001
      vertex 33.975002 398.771576 6.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 34.798557 397.948029 6.000001
      vertex 39.350002 410.823029 6.000001
      vertex 34.440990 398.414001 6.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 39.350002 410.823029 6.000001
      vertex 34.798557 397.948029 6.000001
      vertex 35.023335 397.405365 6.000001
    endloop
  endfacet
  facet normal -0.000000 1.000000 0.000000
    outer loop
      vertex 2.850001 410.823029 6.000001
      vertex 39.350002 410.823029 6.000001
      vertex 39.350002 410.823029 2.000001
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 1.850001 410.823029 2.000001
      vertex 2.850001 410.823029 6.000001
      vertex 39.350002 410.823029 2.000001
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 1.850001 410.823029 9.000001
      vertex 2.850001 410.823029 6.000001
      vertex 1.850001 410.823029 2.000001
    endloop
  endfacet
  facet normal 0.000000 1.000000 -0.000000
    outer loop
      vertex 2.850001 410.823029 6.000001
      vertex 1.850001 410.823029 9.000001
      vertex 2.850001 410.823029 9.000001
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 39.350002 390.823029 2.000001
      vertex 39.350002 410.823029 2.000001
      vertex 39.350002 410.823029 6.000001
    endloop
  endfacet
  facet normal 1.000000 -0.000000 0.000000
    outer loop
      vertex 39.350002 390.823029 6.000001
      vertex 39.350002 390.823029 2.000001
      vertex 39.350002 410.823029 6.000001
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 39.350002 390.823029 2.000001
      vertex 39.350002 390.823029 6.000001
      vertex 2.850001 390.823029 6.000001
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 1.850001 390.823029 2.000001
      vertex 39.350002 390.823029 2.000001
      vertex 2.850001 390.823029 6.000001
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 1.850001 390.823029 9.000001
      vertex 1.850001 390.823029 2.000001
      vertex 2.850001 390.823029 6.000001
    endloop
  endfacet
  facet normal -0.000000 -1.000000 -0.000000
    outer loop
      vertex 2.850001 390.823029 9.000001
      vertex 1.850001 390.823029 9.000001
      vertex 2.850001 390.823029 6.000001
    endloop
  endfacet
  facet normal -0.991445 0.130522 0.000000
    outer loop
      vertex 35.100002 396.823029 2.000001
      vertex 35.023335 396.240662 2.000001
      vertex 35.023335 396.240662 6.000001
    endloop
  endfacet
  facet normal -0.991445 0.130522 0.000000
    outer loop
      vertex 35.100002 396.823029 6.000001
      vertex 35.100002 396.823029 2.000001
      vertex 35.023335 396.240662 6.000001
    endloop
  endfacet
  facet normal -0.991445 -0.130529 0.000000
    outer loop
      vertex 35.023335 397.405365 2.000001
      vertex 35.100002 396.823029 2.000001
      vertex 35.100002 396.823029 6.000001
    endloop
  endfacet
  facet normal -0.991445 -0.130529 -0.000000
    outer loop
      vertex 35.023335 397.405365 6.000001
      vertex 35.023335 397.405365 2.000001
      vertex 35.100002 396.823029 6.000001
    endloop
  endfacet
  facet normal -0.923880 -0.382681 0.000000
    outer loop
      vertex 34.798557 397.948029 2.000001
      vertex 35.023335 397.405365 2.000001
      vertex 35.023335 397.405365 6.000001
    endloop
  endfacet
  facet normal -0.923880 -0.382681 -0.000000
    outer loop
      vertex 34.798557 397.948029 6.000001
      vertex 34.798557 397.948029 2.000001
      vertex 35.023335 397.405365 6.000001
    endloop
  endfacet
  facet normal -0.793342 -0.608776 0.000000
    outer loop
      vertex 34.440990 398.414001 2.000001
      vertex 34.798557 397.948029 2.000001
      vertex 34.798557 397.948029 6.000001
    endloop
  endfacet
  facet normal -0.793342 -0.608776 -0.000000
    outer loop
      vertex 34.440990 398.414001 6.000001
      vertex 34.440990 398.414001 2.000001
      vertex 34.798557 397.948029 6.000001
    endloop
  endfacet
  facet normal -0.608771 -0.793346 0.000000
    outer loop
      vertex 33.975002 398.771576 2.000001
      vertex 34.440990 398.414001 2.000001
      vertex 34.440990 398.414001 6.000001
    endloop
  endfacet
  facet normal -0.608771 -0.793346 -0.000000
    outer loop
      vertex 33.975002 398.771576 6.000001
      vertex 33.975002 398.771576 2.000001
      vertex 34.440990 398.414001 6.000001
    endloop
  endfacet
  facet normal -0.382662 -0.923889 0.000000
    outer loop
      vertex 33.432343 398.996338 2.000001
      vertex 33.975002 398.771576 2.000001
      vertex 33.975002 398.771576 6.000001
    endloop
  endfacet
  facet normal -0.382662 -0.923889 -0.000000
    outer loop
      vertex 33.432343 398.996338 6.000001
      vertex 33.432343 398.996338 2.000001
      vertex 33.975002 398.771576 6.000001
    endloop
  endfacet
  facet normal -0.130567 -0.991440 0.000000
    outer loop
      vertex 32.850002 399.073029 2.000001
      vertex 33.432343 398.996338 2.000001
      vertex 33.432343 398.996338 6.000001
    endloop
  endfacet
  facet normal -0.130567 -0.991440 -0.000000
    outer loop
      vertex 32.850002 399.073029 6.000001
      vertex 32.850002 399.073029 2.000001
      vertex 33.432343 398.996338 6.000001
    endloop
  endfacet
  facet normal 0.130566 -0.991440 0.000000
    outer loop
      vertex 32.267658 398.996338 2.000001
      vertex 32.850002 399.073029 2.000001
      vertex 32.850002 399.073029 6.000001
    endloop
  endfacet
  facet normal 0.130566 -0.991440 0.000000
    outer loop
      vertex 32.267658 398.996338 6.000001
      vertex 32.267658 398.996338 2.000001
      vertex 32.850002 399.073029 6.000001
    endloop
  endfacet
  facet normal 0.382663 -0.923888 0.000000
    outer loop
      vertex 31.725000 398.771576 2.000001
      vertex 32.267658 398.996338 2.000001
      vertex 32.267658 398.996338 6.000001
    endloop
  endfacet
  facet normal 0.382663 -0.923888 0.000000
    outer loop
      vertex 31.725000 398.771576 6.000001
      vertex 31.725000 398.771576 2.000001
      vertex 32.267658 398.996338 6.000001
    endloop
  endfacet
  facet normal 0.608770 -0.793347 0.000000
    outer loop
      vertex 31.259010 398.414001 2.000001
      vertex 31.725000 398.771576 2.000001
      vertex 31.725000 398.771576 6.000001
    endloop
  endfacet
  facet normal 0.608770 -0.793347 0.000000
    outer loop
      vertex 31.259010 398.414001 6.000001
      vertex 31.259010 398.414001 2.000001
      vertex 31.725000 398.771576 6.000001
    endloop
  endfacet
  facet normal 0.793342 -0.608776 0.000000
    outer loop
      vertex 30.901443 397.948029 2.000001
      vertex 31.259010 398.414001 2.000001
      vertex 31.259010 398.414001 6.000001
    endloop
  endfacet
  facet normal 0.793342 -0.608776 0.000000
    outer loop
      vertex 30.901443 397.948029 6.000001
      vertex 30.901443 397.948029 2.000001
      vertex 31.259010 398.414001 6.000001
    endloop
  endfacet
  facet normal 0.923882 -0.382679 0.000000
    outer loop
      vertex 30.676668 397.405365 2.000001
      vertex 30.901443 397.948029 2.000001
      vertex 30.901443 397.948029 6.000001
    endloop
  endfacet
  facet normal 0.923882 -0.382679 0.000000
    outer loop
      vertex 30.676668 397.405365 6.000001
      vertex 30.676668 397.405365 2.000001
      vertex 30.901443 397.948029 6.000001
    endloop
  endfacet
  facet normal 0.991445 -0.130529 0.000000
    outer loop
      vertex 30.600000 396.823029 2.000001
      vertex 30.676668 397.405365 2.000001
      vertex 30.676668 397.405365 6.000001
    endloop
  endfacet
  facet normal 0.991445 -0.130529 0.000000
    outer loop
      vertex 30.600000 396.823029 6.000001
      vertex 30.600000 396.823029 2.000001
      vertex 30.676668 397.405365 6.000001
    endloop
  endfacet
  facet normal 0.991445 0.130522 0.000000
    outer loop
      vertex 30.676668 396.240662 2.000001
      vertex 30.600000 396.823029 2.000001
      vertex 30.600000 396.823029 6.000001
    endloop
  endfacet
  facet normal 0.991445 0.130522 0.000000
    outer loop
      vertex 30.676668 396.240662 6.000001
      vertex 30.676668 396.240662 2.000001
      vertex 30.600000 396.823029 6.000001
    endloop
  endfacet
  facet normal 0.923874 0.382697 0.000000
    outer loop
      vertex 30.901443 395.698029 2.000001
      vertex 30.676668 396.240662 2.000001
      vertex 30.676668 396.240662 6.000001
    endloop
  endfacet
  facet normal 0.923874 0.382697 0.000000
    outer loop
      vertex 30.901443 395.698029 6.000001
      vertex 30.901443 395.698029 2.000001
      vertex 30.676668 396.240662 6.000001
    endloop
  endfacet
  facet normal 0.793362 0.608751 0.000000
    outer loop
      vertex 31.259010 395.232025 2.000001
      vertex 30.901443 395.698029 2.000001
      vertex 30.901443 395.698029 6.000001
    endloop
  endfacet
  facet normal 0.793362 0.608751 0.000000
    outer loop
      vertex 31.259010 395.232025 6.000001
      vertex 31.259010 395.232025 2.000001
      vertex 30.901443 395.698029 6.000001
    endloop
  endfacet
  facet normal 0.608770 0.793347 0.000000
    outer loop
      vertex 31.725000 394.874451 2.000001
      vertex 31.259010 395.232025 2.000001
      vertex 31.259010 395.232025 6.000001
    endloop
  endfacet
  facet normal 0.608770 0.793347 0.000000
    outer loop
      vertex 31.725000 394.874451 6.000001
      vertex 31.725000 394.874451 2.000001
      vertex 31.259010 395.232025 6.000001
    endloop
  endfacet
  facet normal 0.382663 0.923888 0.000000
    outer loop
      vertex 32.267658 394.649689 2.000001
      vertex 31.725000 394.874451 2.000001
      vertex 31.725000 394.874451 6.000001
    endloop
  endfacet
  facet normal 0.382663 0.923888 0.000000
    outer loop
      vertex 32.267658 394.649689 6.000001
      vertex 32.267658 394.649689 2.000001
      vertex 31.725000 394.874451 6.000001
    endloop
  endfacet
  facet normal 0.130515 0.991446 0.000000
    outer loop
      vertex 32.850002 394.573029 2.000001
      vertex 32.267658 394.649689 2.000001
      vertex 32.267658 394.649689 6.000001
    endloop
  endfacet
  facet normal 0.130515 0.991446 0.000000
    outer loop
      vertex 32.850002 394.573029 6.000001
      vertex 32.850002 394.573029 2.000001
      vertex 32.267658 394.649689 6.000001
    endloop
  endfacet
  facet normal -0.130516 0.991446 0.000000
    outer loop
      vertex 33.432343 394.649689 2.000001
      vertex 32.850002 394.573029 2.000001
      vertex 32.850002 394.573029 6.000001
    endloop
  endfacet
  facet normal -0.130516 0.991446 0.000000
    outer loop
      vertex 33.432343 394.649689 6.000001
      vertex 33.432343 394.649689 2.000001
      vertex 32.850002 394.573029 6.000001
    endloop
  endfacet
  facet normal -0.382662 0.923889 0.000000
    outer loop
      vertex 33.975002 394.874451 2.000001
      vertex 33.432343 394.649689 2.000001
      vertex 33.432343 394.649689 6.000001
    endloop
  endfacet
  facet normal -0.382662 0.923889 0.000000
    outer loop
      vertex 33.975002 394.874451 6.000001
      vertex 33.975002 394.874451 2.000001
      vertex 33.432343 394.649689 6.000001
    endloop
  endfacet
  facet normal -0.608771 0.793346 0.000000
    outer loop
      vertex 34.440990 395.232025 2.000001
      vertex 33.975002 394.874451 2.000001
      vertex 33.975002 394.874451 6.000001
    endloop
  endfacet
  facet normal -0.608771 0.793346 0.000000
    outer loop
      vertex 34.440990 395.232025 6.000001
      vertex 34.440990 395.232025 2.000001
      vertex 33.975002 394.874451 6.000001
    endloop
  endfacet
  facet normal -0.793362 0.608751 0.000000
    outer loop
      vertex 34.798557 395.698029 2.000001
      vertex 34.440990 395.232025 2.000001
      vertex 34.440990 395.232025 6.000001
    endloop
  endfacet
  facet normal -0.793362 0.608751 0.000000
    outer loop
      vertex 34.798557 395.698029 6.000001
      vertex 34.798557 395.698029 2.000001
      vertex 34.440990 395.232025 6.000001
    endloop
  endfacet
  facet normal -0.923873 0.382700 0.000000
    outer loop
      vertex 35.023335 396.240662 2.000001
      vertex 34.798557 395.698029 2.000001
      vertex 34.798557 395.698029 6.000001
    endloop
  endfacet
  facet normal -0.923873 0.382700 0.000000
    outer loop
      vertex 35.023335 396.240662 6.000001
      vertex 35.023335 396.240662 2.000001
      vertex 34.798557 395.698029 6.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 35.100002 396.823029 2.000001
      vertex 35.023335 397.405365 2.000001
      vertex 30.676668 397.405365 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 30.600000 396.823029 2.000001
      vertex 35.100002 396.823029 2.000001
      vertex 30.676668 397.405365 2.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 35.023335 396.240662 2.000001
      vertex 35.100002 396.823029 2.000001
      vertex 30.600000 396.823029 2.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 30.676668 396.240662 2.000001
      vertex 35.023335 396.240662 2.000001
      vertex 30.600000 396.823029 2.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 34.798557 395.698029 2.000001
      vertex 35.023335 396.240662 2.000001
      vertex 30.676668 396.240662 2.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 30.901443 395.698029 2.000001
      vertex 34.798557 395.698029 2.000001
      vertex 30.676668 396.240662 2.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 34.440990 395.232025 2.000001
      vertex 34.798557 395.698029 2.000001
      vertex 30.901443 395.698029 2.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 31.259010 395.232025 2.000001
      vertex 34.440990 395.232025 2.000001
      vertex 30.901443 395.698029 2.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 33.975002 394.874451 2.000001
      vertex 34.440990 395.232025 2.000001
      vertex 31.259010 395.232025 2.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 31.725000 394.874451 2.000001
      vertex 33.975002 394.874451 2.000001
      vertex 31.259010 395.232025 2.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 33.432343 394.649689 2.000001
      vertex 33.975002 394.874451 2.000001
      vertex 31.725000 394.874451 2.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 32.267658 394.649689 2.000001
      vertex 33.432343 394.649689 2.000001
      vertex 31.725000 394.874451 2.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 32.850002 394.573029 2.000001
      vertex 33.432343 394.649689 2.000001
      vertex 32.267658 394.649689 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 30.901443 397.948029 2.000001
      vertex 30.676668 397.405365 2.000001
      vertex 35.023335 397.405365 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 34.798557 397.948029 2.000001
      vertex 30.901443 397.948029 2.000001
      vertex 35.023335 397.405365 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 31.259010 398.414001 2.000001
      vertex 30.901443 397.948029 2.000001
      vertex 34.798557 397.948029 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 34.440990 398.414001 2.000001
      vertex 31.259010 398.414001 2.000001
      vertex 34.798557 397.948029 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 31.725000 398.771576 2.000001
      vertex 31.259010 398.414001 2.000001
      vertex 34.440990 398.414001 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 33.975002 398.771576 2.000001
      vertex 31.725000 398.771576 2.000001
      vertex 34.440990 398.414001 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 32.267658 398.996338 2.000001
      vertex 31.725000 398.771576 2.000001
      vertex 33.975002 398.771576 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 33.432343 398.996338 2.000001
      vertex 32.267658 398.996338 2.000001
      vertex 33.975002 398.771576 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 32.850002 399.073029 2.000001
      vertex 32.267658 398.996338 2.000001
      vertex 33.432343 398.996338 2.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 2.850001 410.823029 9.000001
      vertex 1.850001 410.823029 9.000001
      vertex 1.850001 390.823029 9.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 2.850001 390.823029 9.000001
      vertex 2.850001 410.823029 9.000001
      vertex 1.850001 390.823029 9.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 8.850001 380.073029 9.000001
      vertex 2.850001 380.073029 9.000001
      vertex 2.850001 378.073029 9.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 8.850001 378.073029 9.000001
      vertex 8.850001 380.073029 9.000001
      vertex 2.850001 378.073029 9.000001
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 2.850001 390.823029 6.000001
      vertex 2.850001 410.823029 6.000001
      vertex 2.850001 410.823029 9.000001
    endloop
  endfacet
  facet normal 1.000000 -0.000000 0.000000
    outer loop
      vertex 2.850001 390.823029 9.000001
      vertex 2.850001 390.823029 6.000001
      vertex 2.850001 410.823029 9.000001
    endloop
  endfacet
  facet normal 0.000000 -0.130531 0.991444
    outer loop
      vertex 2.850001 375.849457 2.102224
      vertex 2.850001 375.073029 2.000001
      vertex 8.850001 375.073029 2.000001
    endloop
  endfacet
  facet normal 0.000000 -0.130531 0.991444
    outer loop
      vertex 8.850001 375.849457 2.102224
      vertex 2.850001 375.849457 2.102224
      vertex 8.850001 375.073029 2.000001
    endloop
  endfacet
  facet normal 0.000000 -0.382670 0.923885
    outer loop
      vertex 2.850001 376.573029 2.401925
      vertex 2.850001 375.849457 2.102224
      vertex 8.850001 375.849457 2.102224
    endloop
  endfacet
  facet normal 0.000000 -0.382670 0.923885
    outer loop
      vertex 8.850001 376.573029 2.401925
      vertex 2.850001 376.573029 2.401925
      vertex 8.850001 375.849457 2.102224
    endloop
  endfacet
  facet normal 0.000000 -0.608769 0.793347
    outer loop
      vertex 2.850001 377.194336 2.878681
      vertex 2.850001 376.573029 2.401925
      vertex 8.850001 376.573029 2.401925
    endloop
  endfacet
  facet normal 0.000000 -0.608769 0.793347
    outer loop
      vertex 8.850001 377.194336 2.878681
      vertex 2.850001 377.194336 2.878681
      vertex 8.850001 376.573029 2.401925
    endloop
  endfacet
  facet normal 0.000000 -0.793360 0.608753
    outer loop
      vertex 2.850001 377.671082 3.500001
      vertex 2.850001 377.194336 2.878681
      vertex 8.850001 377.194336 2.878681
    endloop
  endfacet
  facet normal 0.000000 -0.793360 0.608753
    outer loop
      vertex 8.850001 377.671082 3.500001
      vertex 2.850001 377.671082 3.500001
      vertex 8.850001 377.194336 2.878681
    endloop
  endfacet
  facet normal 0.000000 -0.923874 0.382696
    outer loop
      vertex 2.850001 377.970795 4.223544
      vertex 2.850001 377.671082 3.500001
      vertex 8.850001 377.671082 3.500001
    endloop
  endfacet
  facet normal 0.000000 -0.923874 0.382696
    outer loop
      vertex 8.850001 377.970795 4.223544
      vertex 2.850001 377.970795 4.223544
      vertex 8.850001 377.671082 3.500001
    endloop
  endfacet
  facet normal 0.000000 -0.991443 0.130540
    outer loop
      vertex 2.850001 378.073029 5.000001
      vertex 2.850001 377.970795 4.223544
      vertex 8.850001 377.970795 4.223544
    endloop
  endfacet
  facet normal 0.000000 -0.991443 0.130540
    outer loop
      vertex 8.850001 378.073029 5.000001
      vertex 2.850001 378.073029 5.000001
      vertex 8.850001 377.970795 4.223544
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 2.850001 378.073029 5.000001
      vertex 8.850001 378.073029 5.000001
      vertex 8.850001 378.073029 9.000001
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 2.850001 378.073029 9.000001
      vertex 2.850001 378.073029 5.000001
      vertex 8.850001 378.073029 9.000001
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 8.850001 380.073029 2.000001
      vertex 2.850001 380.073029 2.000001
      vertex 2.850001 380.073029 9.000001
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 8.850001 380.073029 9.000001
      vertex 8.850001 380.073029 2.000001
      vertex 2.850001 380.073029 9.000001
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 2.850001 378.073029 5.000001
      vertex 2.850001 378.073029 9.000001
      vertex 2.850001 380.073029 9.000001
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 2.850001 380.073029 2.000001
      vertex 2.850001 378.073029 5.000001
      vertex 2.850001 380.073029 9.000001
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 2.850001 377.970795 4.223544
      vertex 2.850001 378.073029 5.000001
      vertex 2.850001 380.073029 2.000001
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 2.850001 377.671082 3.500001
      vertex 2.850001 377.970795 4.223544
      vertex 2.850001 380.073029 2.000001
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 2.850001 377.194336 2.878681
      vertex 2.850001 377.671082 3.500001
      vertex 2.850001 380.073029 2.000001
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 2.850001 376.573029 2.401925
      vertex 2.850001 377.194336 2.878681
      vertex 2.850001 380.073029 2.000001
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 2.850001 375.849457 2.102224
      vertex 2.850001 376.573029 2.401925
      vertex 2.850001 380.073029 2.000001
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 2.850001 375.073029 2.000001
      vertex 2.850001 375.849457 2.102224
      vertex 2.850001 380.073029 2.000001
    endloop
  endfacet
  facet normal 1.000000 0.000000 -0.000000
    outer loop
      vertex 8.850001 380.073029 2.000001
      vertex 8.850001 380.073029 9.000001
      vertex 8.850001 378.073029 5.000001
    endloop
  endfacet
  facet normal 1.000000 -0.000000 0.000000
    outer loop
      vertex 8.850001 377.970795 4.223544
      vertex 8.850001 380.073029 2.000001
      vertex 8.850001 378.073029 5.000001
    endloop
  endfacet
  facet normal 1.000000 -0.000000 0.000000
    outer loop
      vertex 8.850001 377.671082 3.500001
      vertex 8.850001 380.073029 2.000001
      vertex 8.850001 377.970795 4.223544
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 8.850001 378.073029 5.000001
      vertex 8.850001 380.073029 9.000001
      vertex 8.850001 378.073029 9.000001
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 8.850001 380.073029 2.000001
      vertex 8.850001 377.671082 3.500001
      vertex 8.850001 377.194336 2.878681
    endloop
  endfacet
  facet normal 1.000000 -0.000000 0.000000
    outer loop
      vertex 8.850001 376.573029 2.401925
      vertex 8.850001 380.073029 2.000001
      vertex 8.850001 377.194336 2.878681
    endloop
  endfacet
  facet normal 1.000000 -0.000000 0.000000
    outer loop
      vertex 8.850001 375.849457 2.102224
      vertex 8.850001 380.073029 2.000001
      vertex 8.850001 376.573029 2.401925
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 8.850001 380.073029 2.000001
      vertex 8.850001 375.849457 2.102224
      vertex 8.850001 375.073029 2.000001
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 1.850001 410.823029 2.000001
      vertex 1.850001 390.823029 2.000001
      vertex 1.850001 390.823029 9.000001
    endloop
  endfacet
  facet normal -1.000000 -0.000000 -0.000000
    outer loop
      vertex 1.850001 410.823029 9.000001
      vertex 1.850001 410.823029 2.000001
      vertex 1.850001 390.823029 9.000001
    endloop
  endfacet
  facet normal 0.130493 -0.991449 0.000000
    outer loop
      vertex 40.014111 348.527527 2.000001
      vertex 39.600002 348.473022 2.000001
      vertex 39.600002 348.473022 0.000001
    endloop
  endfacet
  facet normal 0.130493 -0.991449 0.000000
    outer loop
      vertex 40.014111 348.527527 0.000001
      vertex 40.014111 348.527527 2.000001
      vertex 39.600002 348.473022 0.000001
    endloop
  endfacet
  facet normal 0.382703 -0.923871 0.000000
    outer loop
      vertex 40.400002 348.687378 2.000001
      vertex 40.014111 348.527527 2.000001
      vertex 40.014111 348.527527 0.000001
    endloop
  endfacet
  facet normal 0.382703 -0.923871 0.000000
    outer loop
      vertex 40.400002 348.687378 0.000001
      vertex 40.400002 348.687378 2.000001
      vertex 40.014111 348.527527 0.000001
    endloop
  endfacet
  facet normal 0.608765 -0.793351 0.000000
    outer loop
      vertex 40.731373 348.941650 2.000001
      vertex 40.400002 348.687378 2.000001
      vertex 40.400002 348.687378 0.000001
    endloop
  endfacet
  facet normal 0.608765 -0.793351 0.000000
    outer loop
      vertex 40.731373 348.941650 0.000001
      vertex 40.731373 348.941650 2.000001
      vertex 40.400002 348.687378 0.000001
    endloop
  endfacet
  facet normal 0.793345 -0.608772 0.000000
    outer loop
      vertex 40.985641 349.273010 2.000001
      vertex 40.731373 348.941650 2.000001
      vertex 40.731373 348.941650 0.000001
    endloop
  endfacet
  facet normal 0.793345 -0.608772 0.000000
    outer loop
      vertex 40.985641 349.273010 0.000001
      vertex 40.985641 349.273010 2.000001
      vertex 40.731373 348.941650 0.000001
    endloop
  endfacet
  facet normal 0.923882 -0.382677 0.000000
    outer loop
      vertex 41.145481 349.658905 2.000001
      vertex 40.985641 349.273010 2.000001
      vertex 40.985641 349.273010 0.000001
    endloop
  endfacet
  facet normal 0.923882 -0.382677 0.000000
    outer loop
      vertex 41.145481 349.658905 0.000001
      vertex 41.145481 349.658905 2.000001
      vertex 40.985641 349.273010 0.000001
    endloop
  endfacet
  facet normal 0.991445 -0.130524 0.000000
    outer loop
      vertex 41.200001 350.073029 2.000001
      vertex 41.145481 349.658905 2.000001
      vertex 41.145481 349.658905 0.000001
    endloop
  endfacet
  facet normal 0.991445 -0.130524 0.000000
    outer loop
      vertex 41.200001 350.073029 0.000001
      vertex 41.200001 350.073029 2.000001
      vertex 41.145481 349.658905 0.000001
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 420.073029 2.000001
      vertex 41.200001 350.073029 2.000001
      vertex 41.200001 350.073029 0.000001
    endloop
  endfacet
  facet normal 1.000000 0.000000 -0.000000
    outer loop
      vertex 41.200001 420.073029 0.000001
      vertex 41.200001 420.073029 2.000001
      vertex 41.200001 350.073029 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 1.854447 367.925476 0.000001
      vertex 4.304520 372.598083 0.000001
      vertex 4.250001 372.183990 0.000001
    endloop
  endfacet
  facet normal -0.000000 0.000000 -1.000000
    outer loop
      vertex 4.304520 371.769867 0.000001
      vertex 1.854447 367.925476 0.000001
      vertex 4.250001 372.183990 0.000001
    endloop
  endfacet
  facet normal -0.000000 0.000000 -1.000000
    outer loop
      vertex 4.464360 371.383972 0.000001
      vertex 1.854447 367.925476 0.000001
      vertex 4.304520 371.769867 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 1.854447 367.925476 0.000001
      vertex 4.464360 371.383972 0.000001
      vertex 4.718630 371.052612 0.000001
    endloop
  endfacet
  facet normal -0.000000 0.000000 -1.000000
    outer loop
      vertex 5.050001 370.798340 0.000001
      vertex 1.854447 367.925476 0.000001
      vertex 4.718630 371.052612 0.000001
    endloop
  endfacet
  facet normal -0.000000 0.000000 -1.000000
    outer loop
      vertex 5.435891 370.638489 0.000001
      vertex 1.854447 367.925476 0.000001
      vertex 5.050001 370.798340 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 8.354447 367.925476 0.000001
      vertex 1.854447 367.925476 0.000001
      vertex 5.435891 370.638489 0.000001
    endloop
  endfacet
  facet normal -0.000000 -0.000000 -1.000000
    outer loop
      vertex 5.850001 370.583984 0.000001
      vertex 8.354447 367.925476 0.000001
      vertex 5.435891 370.638489 0.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 6.264112 370.638489 0.000001
      vertex 8.354447 367.925476 0.000001
      vertex 5.850001 370.583984 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 8.354447 367.925476 0.000001
      vertex 6.264112 370.638489 0.000001
      vertex 6.650001 370.798340 0.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 6.981372 371.052612 0.000001
      vertex 8.354447 367.925476 0.000001
      vertex 6.650001 370.798340 0.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 7.235641 371.383972 0.000001
      vertex 8.354447 367.925476 0.000001
      vertex 6.981372 371.052612 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 8.354447 367.925476 0.000001
      vertex 7.235641 371.383972 0.000001
      vertex 7.395483 371.769867 0.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 7.450001 372.183990 0.000001
      vertex 8.354447 367.925476 0.000001
      vertex 7.395483 371.769867 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 7.395483 372.598083 0.000001
      vertex 8.354447 367.925476 0.000001
      vertex 7.450001 372.183990 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 7.395483 372.598083 0.000001
      vertex 7.235641 372.983978 0.000001
      vertex 39.600002 421.673004 0.000001
    endloop
  endfacet
  facet normal -0.000000 0.000000 -1.000000
    outer loop
      vertex 41.200001 420.073029 0.000001
      vertex 7.395483 372.598083 0.000001
      vertex 39.600002 421.673004 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 41.200001 350.073029 0.000001
      vertex 7.395483 372.598083 0.000001
      vertex 41.200001 420.073029 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 1.600001 421.673004 0.000001
      vertex 39.600002 421.673004 0.000001
      vertex 7.235641 372.983978 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 6.981372 373.315369 0.000001
      vertex 1.600001 421.673004 0.000001
      vertex 7.235641 372.983978 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 6.650001 373.569611 0.000001
      vertex 1.600001 421.673004 0.000001
      vertex 6.981372 373.315369 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 1.600001 421.673004 0.000001
      vertex 6.650001 373.569611 0.000001
      vertex 6.264112 373.729462 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 0.000001 420.073029 0.000001
      vertex 1.600001 421.673004 0.000001
      vertex 6.264112 373.729462 0.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 1.185891 421.618500 0.000001
      vertex 1.600001 421.673004 0.000001
      vertex 0.000001 420.073029 0.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 0.800001 421.458649 0.000001
      vertex 1.185891 421.618500 0.000001
      vertex 0.000001 420.073029 0.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 0.468630 421.204376 0.000001
      vertex 0.800001 421.458649 0.000001
      vertex 0.000001 420.073029 0.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 0.214360 420.873016 0.000001
      vertex 0.468630 421.204376 0.000001
      vertex 0.000001 420.073029 0.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 0.054520 420.487122 0.000001
      vertex 0.214360 420.873016 0.000001
      vertex 0.000001 420.073029 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 0.000001 420.073029 0.000001
      vertex 6.264112 373.729462 0.000001
      vertex 5.850001 373.783997 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 5.435891 373.729462 0.000001
      vertex 0.000001 420.073029 0.000001
      vertex 5.850001 373.783997 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 5.050001 373.569611 0.000001
      vertex 0.000001 420.073029 0.000001
      vertex 5.435891 373.729462 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 0.000001 420.073029 0.000001
      vertex 5.050001 373.569611 0.000001
      vertex 4.718630 373.315369 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 4.464360 372.983978 0.000001
      vertex 0.000001 420.073029 0.000001
      vertex 4.718630 373.315369 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 1.854447 367.925476 0.000001
      vertex 0.000001 420.073029 0.000001
      vertex 4.464360 372.983978 0.000001
    endloop
  endfacet
  facet normal -0.000000 0.000000 -1.000000
    outer loop
      vertex 4.304520 372.598083 0.000001
      vertex 1.854447 367.925476 0.000001
      vertex 4.464360 372.983978 0.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 1.854447 361.425476 0.000001
      vertex 8.354447 361.425476 0.000001
      vertex 1.600001 348.473022 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 0.000001 350.073029 0.000001
      vertex 1.854447 361.425476 0.000001
      vertex 1.600001 348.473022 0.000001
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 1.854447 367.925476 0.000001
      vertex 1.854447 361.425476 0.000001
      vertex 0.000001 350.073029 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 0.000001 420.073029 0.000001
      vertex 1.854447 367.925476 0.000001
      vertex 0.000001 350.073029 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 39.600002 348.473022 0.000001
      vertex 1.600001 348.473022 0.000001
      vertex 8.354447 361.425476 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 8.354447 367.925476 0.000001
      vertex 39.600002 348.473022 0.000001
      vertex 8.354447 361.425476 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 7.395483 372.598083 0.000001
      vertex 39.600002 348.473022 0.000001
      vertex 8.354447 367.925476 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 41.200001 350.073029 0.000001
      vertex 41.145481 349.658905 0.000001
      vertex 40.985641 349.273010 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 40.731373 348.941650 0.000001
      vertex 41.200001 350.073029 0.000001
      vertex 40.985641 349.273010 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 40.400002 348.687378 0.000001
      vertex 41.200001 350.073029 0.000001
      vertex 40.731373 348.941650 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 41.200001 350.073029 0.000001
      vertex 40.400002 348.687378 0.000001
      vertex 40.014111 348.527527 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 39.600002 348.473022 0.000001
      vertex 41.200001 350.073029 0.000001
      vertex 40.014111 348.527527 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 7.395483 372.598083 0.000001
      vertex 41.200001 350.073029 0.000001
      vertex 39.600002 348.473022 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 0.000001 350.073029 0.000001
      vertex 1.600001 348.473022 0.000001
      vertex 1.185891 348.527527 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 0.800001 348.687378 0.000001
      vertex 0.000001 350.073029 0.000001
      vertex 1.185891 348.527527 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 0.468630 348.941650 0.000001
      vertex 0.000001 350.073029 0.000001
      vertex 0.800001 348.687378 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 0.000001 350.073029 0.000001
      vertex 0.468630 348.941650 0.000001
      vertex 0.214360 349.273010 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 0.054520 349.658905 0.000001
      vertex 0.000001 350.073029 0.000001
      vertex 0.214360 349.273010 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 41.200001 420.073029 0.000001
      vertex 39.600002 421.673004 0.000001
      vertex 40.014111 421.618500 0.000001
    endloop
  endfacet
  facet normal -0.000000 -0.000000 -1.000000
    outer loop
      vertex 40.400002 421.458649 0.000001
      vertex 41.200001 420.073029 0.000001
      vertex 40.014111 421.618500 0.000001
    endloop
  endfacet
  facet normal -0.000000 -0.000000 -1.000000
    outer loop
      vertex 40.731373 421.204376 0.000001
      vertex 41.200001 420.073029 0.000001
      vertex 40.400002 421.458649 0.000001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 41.200001 420.073029 0.000001
      vertex 40.731373 421.204376 0.000001
      vertex 40.985641 420.873016 0.000001
    endloop
  endfacet
  facet normal -0.000000 -0.000000 -1.000000
    outer loop
      vertex 41.145481 420.487122 0.000001
      vertex 41.200001 420.073029 0.000001
      vertex 40.985641 420.873016 0.000001
    endloop
  endfacet
  facet normal -0.991445 -0.130522 0.000000
    outer loop
      vertex 0.054520 349.658905 2.000001
      vertex 0.000001 350.073029 2.000001
      vertex 0.000001 350.073029 0.000001
    endloop
  endfacet
  facet normal -0.991445 -0.130522 0.000000
    outer loop
      vertex 0.054520 349.658905 0.000001
      vertex 0.054520 349.658905 2.000001
      vertex 0.000001 350.073029 0.000001
    endloop
  endfacet
  facet normal -0.923881 -0.382679 0.000000
    outer loop
      vertex 0.214360 349.273010 2.000001
      vertex 0.054520 349.658905 2.000001
      vertex 0.054520 349.658905 0.000001
    endloop
  endfacet
  facet normal -0.923881 -0.382679 0.000000
    outer loop
      vertex 0.214360 349.273010 0.000001
      vertex 0.214360 349.273010 2.000001
      vertex 0.054520 349.658905 0.000001
    endloop
  endfacet
  facet normal -0.793344 -0.608774 0.000000
    outer loop
      vertex 0.468630 348.941650 2.000001
      vertex 0.214360 349.273010 2.000001
      vertex 0.214360 349.273010 0.000001
    endloop
  endfacet
  facet normal -0.793344 -0.608774 0.000000
    outer loop
      vertex 0.468630 348.941650 0.000001
      vertex 0.468630 348.941650 2.000001
      vertex 0.214360 349.273010 0.000001
    endloop
  endfacet
  facet normal -0.608765 -0.793350 0.000000
    outer loop
      vertex 0.800001 348.687378 2.000001
      vertex 0.468630 348.941650 2.000001
      vertex 0.468630 348.941650 0.000001
    endloop
  endfacet
  facet normal -0.608765 -0.793350 0.000000
    outer loop
      vertex 0.800001 348.687378 0.000001
      vertex 0.800001 348.687378 2.000001
      vertex 0.468630 348.941650 0.000001
    endloop
  endfacet
  facet normal -0.382705 -0.923871 0.000000
    outer loop
      vertex 1.185891 348.527527 2.000001
      vertex 0.800001 348.687378 2.000001
      vertex 0.800001 348.687378 0.000001
    endloop
  endfacet
  facet normal -0.382705 -0.923871 0.000000
    outer loop
      vertex 1.185891 348.527527 0.000001
      vertex 1.185891 348.527527 2.000001
      vertex 0.800001 348.687378 0.000001
    endloop
  endfacet
  facet normal -0.130493 -0.991449 0.000000
    outer loop
      vertex 1.600001 348.473022 2.000001
      vertex 1.185891 348.527527 2.000001
      vertex 1.185891 348.527527 0.000001
    endloop
  endfacet
  facet normal -0.130493 -0.991449 0.000000
    outer loop
      vertex 1.600001 348.473022 0.000001
      vertex 1.600001 348.473022 2.000001
      vertex 1.185891 348.527527 0.000001
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 420.073029 0.000001
      vertex 0.000001 350.073029 0.000001
      vertex 0.000001 350.073029 2.000001
    endloop
  endfacet
  facet normal -1.000000 -0.000000 -0.000000
    outer loop
      vertex 0.000001 420.073029 2.000001
      vertex 0.000001 420.073029 0.000001
      vertex 0.000001 350.073029 2.000001
    endloop
  endfacet
  facet normal -0.130493 0.991449 0.000000
    outer loop
      vertex 1.185891 421.618500 2.000001
      vertex 1.600001 421.673004 2.000001
      vertex 1.600001 421.673004 0.000001
    endloop
  endfacet
  facet normal -0.130493 0.991449 0.000000
    outer loop
      vertex 1.185891 421.618500 0.000001
      vertex 1.185891 421.618500 2.000001
      vertex 1.600001 421.673004 0.000001
    endloop
  endfacet
  facet normal -0.382705 0.923871 0.000000
    outer loop
      vertex 0.800001 421.458649 2.000001
      vertex 1.185891 421.618500 2.000001
      vertex 1.185891 421.618500 0.000001
    endloop
  endfacet
  facet normal -0.382705 0.923871 0.000000
    outer loop
      vertex 0.800001 421.458649 0.000001
      vertex 0.800001 421.458649 2.000001
      vertex 1.185891 421.618500 0.000001
    endloop
  endfacet
  facet normal -0.608765 0.793350 0.000000
    outer loop
      vertex 0.468630 421.204376 2.000001
      vertex 0.800001 421.458649 2.000001
      vertex 0.800001 421.458649 0.000001
    endloop
  endfacet
  facet normal -0.608765 0.793350 0.000000
    outer loop
      vertex 0.468630 421.204376 0.000001
      vertex 0.468630 421.204376 2.000001
      vertex 0.800001 421.458649 0.000001
    endloop
  endfacet
  facet normal -0.793344 0.608774 0.000000
    outer loop
      vertex 0.214360 420.873016 2.000001
      vertex 0.468630 421.204376 2.000001
      vertex 0.468630 421.204376 0.000001
    endloop
  endfacet
  facet normal -0.793344 0.608774 0.000000
    outer loop
      vertex 0.214360 420.873016 0.000001
      vertex 0.214360 420.873016 2.000001
      vertex 0.468630 421.204376 0.000001
    endloop
  endfacet
  facet normal -0.923881 0.382679 0.000000
    outer loop
      vertex 0.054520 420.487122 2.000001
      vertex 0.214360 420.873016 2.000001
      vertex 0.214360 420.873016 0.000001
    endloop
  endfacet
  facet normal -0.923881 0.382679 0.000000
    outer loop
      vertex 0.054520 420.487122 0.000001
      vertex 0.054520 420.487122 2.000001
      vertex 0.214360 420.873016 0.000001
    endloop
  endfacet
  facet normal -0.991444 0.130532 0.000000
    outer loop
      vertex 0.000001 420.073029 2.000001
      vertex 0.054520 420.487122 2.000001
      vertex 0.054520 420.487122 0.000001
    endloop
  endfacet
  facet normal -0.991444 0.130532 0.000000
    outer loop
      vertex 0.000001 420.073029 0.000001
      vertex 0.000001 420.073029 2.000001
      vertex 0.054520 420.487122 0.000001
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 39.600002 421.673004 0.000001
      vertex 1.600001 421.673004 0.000001
      vertex 1.600001 421.673004 2.000001
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 39.600002 421.673004 2.000001
      vertex 39.600002 421.673004 0.000001
      vertex 1.600001 421.673004 2.000001
    endloop
  endfacet
  facet normal 0.991444 0.130534 0.000000
    outer loop
      vertex 41.145481 420.487122 2.000001
      vertex 41.200001 420.073029 2.000001
      vertex 41.200001 420.073029 0.000001
    endloop
  endfacet
  facet normal 0.991444 0.130534 -0.000000
    outer loop
      vertex 41.145481 420.487122 0.000001
      vertex 41.145481 420.487122 2.000001
      vertex 41.200001 420.073029 0.000001
    endloop
  endfacet
  facet normal 0.923882 0.382677 0.000000
    outer loop
      vertex 40.985641 420.873016 2.000001
      vertex 41.145481 420.487122 2.000001
      vertex 41.145481 420.487122 0.000001
    endloop
  endfacet
  facet normal 0.923882 0.382677 -0.000000
    outer loop
      vertex 40.985641 420.873016 0.000001
      vertex 40.985641 420.873016 2.000001
      vertex 41.145481 420.487122 0.000001
    endloop
  endfacet
  facet normal 0.793345 0.608772 0.000000
    outer loop
      vertex 40.731373 421.204376 2.000001
      vertex 40.985641 420.873016 2.000001
      vertex 40.985641 420.873016 0.000001
    endloop
  endfacet
  facet normal 0.793345 0.608772 -0.000000
    outer loop
      vertex 40.731373 421.204376 0.000001
      vertex 40.731373 421.204376 2.000001
      vertex 40.985641 420.873016 0.000001
    endloop
  endfacet
  facet normal 0.608765 0.793351 0.000000
    outer loop
      vertex 40.400002 421.458649 2.000001
      vertex 40.731373 421.204376 2.000001
      vertex 40.731373 421.204376 0.000001
    endloop
  endfacet
  facet normal 0.608765 0.793351 -0.000000
    outer loop
      vertex 40.400002 421.458649 0.000001
      vertex 40.400002 421.458649 2.000001
      vertex 40.731373 421.204376 0.000001
    endloop
  endfacet
  facet normal 0.382703 0.923871 0.000000
    outer loop
      vertex 40.014111 421.618500 2.000001
      vertex 40.400002 421.458649 2.000001
      vertex 40.400002 421.458649 0.000001
    endloop
  endfacet
  facet normal 0.382703 0.923871 -0.000000
    outer loop
      vertex 40.014111 421.618500 0.000001
      vertex 40.014111 421.618500 2.000001
      vertex 40.400002 421.458649 0.000001
    endloop
  endfacet
  facet normal 0.130493 0.991449 0.000000
    outer loop
      vertex 39.600002 421.673004 2.000001
      vertex 40.014111 421.618500 2.000001
      vertex 40.014111 421.618500 0.000001
    endloop
  endfacet
  facet normal 0.130493 0.991449 -0.000000
    outer loop
      vertex 39.600002 421.673004 0.000001
      vertex 39.600002 421.673004 2.000001
      vertex 40.014111 421.618500 0.000001
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 1.600001 348.473022 0.000001
      vertex 39.600002 348.473022 0.000001
      vertex 39.600002 348.473022 2.000001
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 1.600001 348.473022 2.000001
      vertex 1.600001 348.473022 0.000001
      vertex 39.600002 348.473022 2.000001
    endloop
  endfacet
endsolid Mesh

```

```stl
solid Mesh
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.100001 284.484406 8.600000
      vertex 1.100001 307.884399 11.600000
      vertex 1.100001 292.884399 11.600000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.100001 291.486786 11.784000
      vertex 1.100001 284.484406 8.600000
      vertex 1.100001 292.884399 11.600000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.100001 290.184387 12.323462
      vertex 1.100001 284.484406 8.600000
      vertex 1.100001 291.486786 11.784000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.100001 284.484406 8.600000
      vertex 1.100001 290.184387 12.323462
      vertex 1.100001 289.066010 13.181623
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.100001 288.207855 14.300000
      vertex 1.100001 284.484406 8.600000
      vertex 1.100001 289.066010 13.181623
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.100001 287.668396 15.602377
      vertex 1.100001 284.484406 8.600000
      vertex 1.100001 288.207855 14.300000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.100001 284.484406 8.600000
      vertex 1.100001 287.668396 15.602377
      vertex 1.100001 287.484406 17.000000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.100001 287.484406 25.200001
      vertex 1.100001 284.484406 8.600000
      vertex 1.100001 287.484406 17.000000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.100001 284.484406 33.599998
      vertex 1.100001 284.484406 8.600000
      vertex 1.100001 287.484406 25.200001
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.100001 287.668396 26.597622
      vertex 1.100001 284.484406 33.599998
      vertex 1.100001 287.484406 25.200001
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.100001 288.207855 27.900000
      vertex 1.100001 284.484406 33.599998
      vertex 1.100001 287.668396 26.597622
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.100001 284.484406 33.599998
      vertex 1.100001 288.207855 27.900000
      vertex 1.100001 289.066010 29.018377
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.100001 290.184387 29.876537
      vertex 1.100001 284.484406 33.599998
      vertex 1.100001 289.066010 29.018377
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.100001 291.486786 30.416000
      vertex 1.100001 284.484406 33.599998
      vertex 1.100001 290.184387 29.876537
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.100001 284.484406 33.599998
      vertex 1.100001 291.486786 30.416000
      vertex 1.100001 292.884399 30.600000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.100001 307.884399 30.600000
      vertex 1.100001 284.484406 33.599998
      vertex 1.100001 292.884399 30.600000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.100001 312.884399 30.600000
      vertex 1.100001 284.484406 33.599998
      vertex 1.100001 307.884399 30.600000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.100001 307.884399 11.600000
      vertex 1.100001 312.884399 30.600000
      vertex 1.100001 307.884399 30.600000
    endloop
  endfacet
  facet normal 1.000000 0.000000 -0.000000
    outer loop
      vertex 1.100001 312.884399 11.600000
      vertex 1.100001 312.884399 30.600000
      vertex 1.100001 307.884399 11.600000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.100001 284.484406 8.600000
      vertex 1.100001 312.884399 11.600000
      vertex 1.100001 307.884399 11.600000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.100001 336.284393 8.600000
      vertex 1.100001 312.884399 11.600000
      vertex 1.100001 284.484406 8.600000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.100001 336.284393 33.599998
      vertex 1.100001 312.884399 30.600000
      vertex 1.100001 327.884399 30.600000
    endloop
  endfacet
  facet normal 1.000000 0.000000 -0.000000
    outer loop
      vertex 1.100001 329.282013 30.416000
      vertex 1.100001 336.284393 33.599998
      vertex 1.100001 327.884399 30.600000
    endloop
  endfacet
  facet normal 1.000000 0.000000 -0.000000
    outer loop
      vertex 1.100001 330.584381 29.876537
      vertex 1.100001 336.284393 33.599998
      vertex 1.100001 329.282013 30.416000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.100001 336.284393 33.599998
      vertex 1.100001 330.584381 29.876537
      vertex 1.100001 331.702759 29.018377
    endloop
  endfacet
  facet normal 1.000000 0.000000 -0.000000
    outer loop
      vertex 1.100001 332.560944 27.900000
      vertex 1.100001 336.284393 33.599998
      vertex 1.100001 331.702759 29.018377
    endloop
  endfacet
  facet normal 1.000000 0.000000 -0.000000
    outer loop
      vertex 1.100001 333.100403 26.597622
      vertex 1.100001 336.284393 33.599998
      vertex 1.100001 332.560944 27.900000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.100001 336.284393 33.599998
      vertex 1.100001 333.100403 26.597622
      vertex 1.100001 333.284393 25.200001
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.100001 333.284393 17.000000
      vertex 1.100001 336.284393 33.599998
      vertex 1.100001 333.284393 25.200001
    endloop
  endfacet
  facet normal 1.000000 0.000000 -0.000000
    outer loop
      vertex 1.100001 336.284393 8.600000
      vertex 1.100001 336.284393 33.599998
      vertex 1.100001 333.284393 17.000000
    endloop
  endfacet
  facet normal 1.000000 -0.000000 0.000000
    outer loop
      vertex 1.100001 333.100403 15.602377
      vertex 1.100001 336.284393 8.600000
      vertex 1.100001 333.284393 17.000000
    endloop
  endfacet
  facet normal 1.000000 -0.000000 0.000000
    outer loop
      vertex 1.100001 332.560944 14.300000
      vertex 1.100001 336.284393 8.600000
      vertex 1.100001 333.100403 15.602377
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.100001 336.284393 8.600000
      vertex 1.100001 332.560944 14.300000
      vertex 1.100001 331.702759 13.181623
    endloop
  endfacet
  facet normal 1.000000 -0.000000 0.000000
    outer loop
      vertex 1.100001 330.584381 12.323462
      vertex 1.100001 336.284393 8.600000
      vertex 1.100001 331.702759 13.181623
    endloop
  endfacet
  facet normal 1.000000 -0.000000 0.000000
    outer loop
      vertex 1.100001 329.282013 11.784000
      vertex 1.100001 336.284393 8.600000
      vertex 1.100001 330.584381 12.323462
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.100001 336.284393 8.600000
      vertex 1.100001 329.282013 11.784000
      vertex 1.100001 327.884399 11.600000
    endloop
  endfacet
  facet normal 1.000000 -0.000000 0.000000
    outer loop
      vertex 1.100001 312.884399 11.600000
      vertex 1.100001 336.284393 8.600000
      vertex 1.100001 327.884399 11.600000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.100001 336.284393 33.599998
      vertex 1.100001 284.484406 33.599998
      vertex 1.100001 312.884399 30.600000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.600001 276.484406 11.600000
      vertex 1.600001 284.484406 11.600000
      vertex 1.600001 284.484406 33.599998
    endloop
  endfacet
  facet normal 1.000000 -0.000000 0.000000
    outer loop
      vertex 1.600001 276.484406 33.599998
      vertex 1.600001 276.484406 11.600000
      vertex 1.600001 284.484406 33.599998
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 1.100001 307.884399 30.600000
      vertex 1.100001 292.884399 30.600000
      vertex 0.000001 292.884399 30.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 0.000001 307.884399 30.600000
      vertex 1.100001 307.884399 30.600000
      vertex 0.000001 292.884399 30.600000
    endloop
  endfacet
  facet normal 0.000000 0.130527 -0.991445
    outer loop
      vertex 0.000001 291.486786 30.416000
      vertex 0.000001 292.884399 30.600000
      vertex 1.100001 292.884399 30.600000
    endloop
  endfacet
  facet normal 0.000000 0.130527 -0.991445
    outer loop
      vertex 1.100001 291.486786 30.416000
      vertex 0.000001 291.486786 30.416000
      vertex 1.100001 292.884399 30.600000
    endloop
  endfacet
  facet normal 0.000000 0.382679 -0.923882
    outer loop
      vertex 0.000001 290.184387 29.876537
      vertex 0.000001 291.486786 30.416000
      vertex 1.100001 291.486786 30.416000
    endloop
  endfacet
  facet normal 0.000000 0.382679 -0.923882
    outer loop
      vertex 1.100001 290.184387 29.876537
      vertex 0.000001 290.184387 29.876537
      vertex 1.100001 291.486786 30.416000
    endloop
  endfacet
  facet normal 0.000000 0.608761 -0.793354
    outer loop
      vertex 0.000001 289.066010 29.018377
      vertex 0.000001 290.184387 29.876537
      vertex 1.100001 290.184387 29.876537
    endloop
  endfacet
  facet normal 0.000000 0.608761 -0.793354
    outer loop
      vertex 1.100001 289.066010 29.018377
      vertex 0.000001 289.066010 29.018377
      vertex 1.100001 290.184387 29.876537
    endloop
  endfacet
  facet normal 0.000000 0.793356 -0.608758
    outer loop
      vertex 0.000001 288.207855 27.900000
      vertex 0.000001 289.066010 29.018377
      vertex 1.100001 289.066010 29.018377
    endloop
  endfacet
  facet normal 0.000000 0.793356 -0.608758
    outer loop
      vertex 1.100001 288.207855 27.900000
      vertex 0.000001 288.207855 27.900000
      vertex 1.100001 289.066010 29.018377
    endloop
  endfacet
  facet normal 0.000000 0.923880 -0.382681
    outer loop
      vertex 0.000001 287.668396 26.597622
      vertex 0.000001 288.207855 27.900000
      vertex 1.100001 288.207855 27.900000
    endloop
  endfacet
  facet normal 0.000000 0.923880 -0.382681
    outer loop
      vertex 1.100001 287.668396 26.597622
      vertex 0.000001 287.668396 26.597622
      vertex 1.100001 288.207855 27.900000
    endloop
  endfacet
  facet normal 0.000000 0.991446 -0.130519
    outer loop
      vertex 0.000001 287.484406 25.200001
      vertex 0.000001 287.668396 26.597622
      vertex 1.100001 287.668396 26.597622
    endloop
  endfacet
  facet normal 0.000000 0.991446 -0.130519
    outer loop
      vertex 1.100001 287.484406 25.200001
      vertex 0.000001 287.484406 25.200001
      vertex 1.100001 287.668396 26.597622
    endloop
  endfacet
  facet normal -0.000000 1.000000 0.000000
    outer loop
      vertex 0.000001 287.484406 25.200001
      vertex 1.100001 287.484406 25.200001
      vertex 1.100001 287.484406 17.000000
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 0.000001 287.484406 17.000000
      vertex 0.000001 287.484406 25.200001
      vertex 1.100001 287.484406 17.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 1.100001 312.884399 11.600000
      vertex 1.100001 327.884399 11.600000
      vertex 0.000001 327.884399 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 0.000001 312.884399 11.600000
      vertex 1.100001 312.884399 11.600000
      vertex 0.000001 327.884399 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.130527 0.991445
    outer loop
      vertex 0.000001 329.282013 11.784000
      vertex 0.000001 327.884399 11.600000
      vertex 1.100001 327.884399 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.130527 0.991445
    outer loop
      vertex 1.100001 329.282013 11.784000
      vertex 0.000001 329.282013 11.784000
      vertex 1.100001 327.884399 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.382686 0.923879
    outer loop
      vertex 0.000001 330.584381 12.323462
      vertex 0.000001 329.282013 11.784000
      vertex 1.100001 329.282013 11.784000
    endloop
  endfacet
  facet normal 0.000000 -0.382686 0.923879
    outer loop
      vertex 1.100001 330.584381 12.323462
      vertex 0.000001 330.584381 12.323462
      vertex 1.100001 329.282013 11.784000
    endloop
  endfacet
  facet normal 0.000000 -0.608761 0.793353
    outer loop
      vertex 0.000001 331.702759 13.181623
      vertex 0.000001 330.584381 12.323462
      vertex 1.100001 330.584381 12.323462
    endloop
  endfacet
  facet normal 0.000000 -0.608761 0.793353
    outer loop
      vertex 1.100001 331.702759 13.181623
      vertex 0.000001 331.702759 13.181623
      vertex 1.100001 330.584381 12.323462
    endloop
  endfacet
  facet normal 0.000000 -0.793345 0.608772
    outer loop
      vertex 0.000001 332.560944 14.300000
      vertex 0.000001 331.702759 13.181623
      vertex 1.100001 331.702759 13.181623
    endloop
  endfacet
  facet normal 0.000000 -0.793345 0.608772
    outer loop
      vertex 1.100001 332.560944 14.300000
      vertex 0.000001 332.560944 14.300000
      vertex 1.100001 331.702759 13.181623
    endloop
  endfacet
  facet normal 0.000000 -0.923880 0.382682
    outer loop
      vertex 0.000001 333.100403 15.602377
      vertex 0.000001 332.560944 14.300000
      vertex 1.100001 332.560944 14.300000
    endloop
  endfacet
  facet normal 0.000000 -0.923880 0.382682
    outer loop
      vertex 1.100001 333.100403 15.602377
      vertex 0.000001 333.100403 15.602377
      vertex 1.100001 332.560944 14.300000
    endloop
  endfacet
  facet normal 0.000000 -0.991446 0.130519
    outer loop
      vertex 0.000001 333.284393 17.000000
      vertex 0.000001 333.100403 15.602377
      vertex 1.100001 333.100403 15.602377
    endloop
  endfacet
  facet normal 0.000000 -0.991446 0.130519
    outer loop
      vertex 1.100001 333.284393 17.000000
      vertex 0.000001 333.284393 17.000000
      vertex 1.100001 333.100403 15.602377
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 0.000001 333.284393 17.000000
      vertex 1.100001 333.284393 17.000000
      vertex 1.100001 333.284393 25.200001
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 0.000001 333.284393 25.200001
      vertex 0.000001 333.284393 17.000000
      vertex 1.100001 333.284393 25.200001
    endloop
  endfacet
  facet normal -0.991445 0.000000 -0.130525
    outer loop
      vertex 23.600000 344.884399 21.000000
      vertex 23.463705 344.884399 22.035276
      vertex 23.463705 346.484406 22.035276
    endloop
  endfacet
  facet normal -0.991445 -0.000000 -0.130525
    outer loop
      vertex 23.600000 346.484406 21.000000
      vertex 23.600000 344.884399 21.000000
      vertex 23.463705 346.484406 22.035276
    endloop
  endfacet
  facet normal -0.991445 0.000000 0.130525
    outer loop
      vertex 23.463705 344.884399 19.964724
      vertex 23.600000 344.884399 21.000000
      vertex 23.600000 346.484406 21.000000
    endloop
  endfacet
  facet normal -0.991445 0.000000 0.130525
    outer loop
      vertex 23.463705 346.484406 19.964724
      vertex 23.463705 344.884399 19.964724
      vertex 23.600000 346.484406 21.000000
    endloop
  endfacet
  facet normal -0.923879 0.000000 0.382684
    outer loop
      vertex 23.064102 344.884399 19.000000
      vertex 23.463705 344.884399 19.964724
      vertex 23.463705 346.484406 19.964724
    endloop
  endfacet
  facet normal -0.923879 0.000000 0.382684
    outer loop
      vertex 23.064102 346.484406 19.000000
      vertex 23.064102 344.884399 19.000000
      vertex 23.463705 346.484406 19.964724
    endloop
  endfacet
  facet normal -0.793353 0.000000 0.608761
    outer loop
      vertex 22.428429 344.884399 18.171574
      vertex 23.064102 344.884399 19.000000
      vertex 23.064102 346.484406 19.000000
    endloop
  endfacet
  facet normal -0.793353 0.000000 0.608761
    outer loop
      vertex 22.428429 346.484406 18.171574
      vertex 22.428429 344.884399 18.171574
      vertex 23.064102 346.484406 19.000000
    endloop
  endfacet
  facet normal -0.608761 0.000000 0.793353
    outer loop
      vertex 21.600000 344.884399 17.535898
      vertex 22.428429 344.884399 18.171574
      vertex 22.428429 346.484406 18.171574
    endloop
  endfacet
  facet normal -0.608761 0.000000 0.793353
    outer loop
      vertex 21.600000 346.484406 17.535898
      vertex 21.600000 344.884399 17.535898
      vertex 22.428429 346.484406 18.171574
    endloop
  endfacet
  facet normal -0.382683 0.000000 0.923880
    outer loop
      vertex 20.635277 344.884399 17.136297
      vertex 21.600000 344.884399 17.535898
      vertex 21.600000 346.484406 17.535898
    endloop
  endfacet
  facet normal -0.382683 0.000000 0.923880
    outer loop
      vertex 20.635277 346.484406 17.136297
      vertex 20.635277 344.884399 17.136297
      vertex 21.600000 346.484406 17.535898
    endloop
  endfacet
  facet normal -0.130527 0.000000 0.991445
    outer loop
      vertex 19.600000 344.884399 17.000000
      vertex 20.635277 344.884399 17.136297
      vertex 20.635277 346.484406 17.136297
    endloop
  endfacet
  facet normal -0.130527 0.000000 0.991445
    outer loop
      vertex 19.600000 346.484406 17.000000
      vertex 19.600000 344.884399 17.000000
      vertex 20.635277 346.484406 17.136297
    endloop
  endfacet
  facet normal 0.130527 0.000000 0.991445
    outer loop
      vertex 18.564724 344.884399 17.136297
      vertex 19.600000 344.884399 17.000000
      vertex 19.600000 346.484406 17.000000
    endloop
  endfacet
  facet normal 0.130527 0.000000 0.991445
    outer loop
      vertex 18.564724 346.484406 17.136297
      vertex 18.564724 344.884399 17.136297
      vertex 19.600000 346.484406 17.000000
    endloop
  endfacet
  facet normal 0.382683 0.000000 0.923880
    outer loop
      vertex 17.600000 344.884399 17.535898
      vertex 18.564724 344.884399 17.136297
      vertex 18.564724 346.484406 17.136297
    endloop
  endfacet
  facet normal 0.382683 0.000000 0.923880
    outer loop
      vertex 17.600000 346.484406 17.535898
      vertex 17.600000 344.884399 17.535898
      vertex 18.564724 346.484406 17.136297
    endloop
  endfacet
  facet normal 0.608762 0.000000 0.793353
    outer loop
      vertex 16.771574 344.884399 18.171574
      vertex 17.600000 344.884399 17.535898
      vertex 17.600000 346.484406 17.535898
    endloop
  endfacet
  facet normal 0.608762 0.000000 0.793353
    outer loop
      vertex 16.771574 346.484406 18.171574
      vertex 16.771574 344.884399 18.171574
      vertex 17.600000 346.484406 17.535898
    endloop
  endfacet
  facet normal 0.793353 0.000000 0.608762
    outer loop
      vertex 16.135899 344.884399 19.000000
      vertex 16.771574 344.884399 18.171574
      vertex 16.771574 346.484406 18.171574
    endloop
  endfacet
  facet normal 0.793353 0.000000 0.608762
    outer loop
      vertex 16.135899 346.484406 19.000000
      vertex 16.135899 344.884399 19.000000
      vertex 16.771574 346.484406 18.171574
    endloop
  endfacet
  facet normal 0.923880 0.000000 0.382683
    outer loop
      vertex 15.736298 344.884399 19.964724
      vertex 16.135899 344.884399 19.000000
      vertex 16.135899 346.484406 19.000000
    endloop
  endfacet
  facet normal 0.923880 0.000000 0.382683
    outer loop
      vertex 15.736298 346.484406 19.964724
      vertex 15.736298 344.884399 19.964724
      vertex 16.135899 346.484406 19.000000
    endloop
  endfacet
  facet normal 0.991445 0.000000 0.130526
    outer loop
      vertex 15.600001 344.884399 21.000000
      vertex 15.736298 344.884399 19.964724
      vertex 15.736298 346.484406 19.964724
    endloop
  endfacet
  facet normal 0.991445 0.000000 0.130526
    outer loop
      vertex 15.600001 346.484406 21.000000
      vertex 15.600001 344.884399 21.000000
      vertex 15.736298 346.484406 19.964724
    endloop
  endfacet
  facet normal 0.991445 0.000000 -0.130526
    outer loop
      vertex 15.736298 344.884399 22.035276
      vertex 15.600001 344.884399 21.000000
      vertex 15.600001 346.484406 21.000000
    endloop
  endfacet
  facet normal 0.991445 0.000000 -0.130526
    outer loop
      vertex 15.736298 346.484406 22.035276
      vertex 15.736298 344.884399 22.035276
      vertex 15.600001 346.484406 21.000000
    endloop
  endfacet
  facet normal 0.923880 0.000000 -0.382683
    outer loop
      vertex 16.135899 344.884399 23.000000
      vertex 15.736298 344.884399 22.035276
      vertex 15.736298 346.484406 22.035276
    endloop
  endfacet
  facet normal 0.923880 0.000000 -0.382683
    outer loop
      vertex 16.135899 346.484406 23.000000
      vertex 16.135899 344.884399 23.000000
      vertex 15.736298 346.484406 22.035276
    endloop
  endfacet
  facet normal 0.793353 0.000000 -0.608762
    outer loop
      vertex 16.771574 344.884399 23.828426
      vertex 16.135899 344.884399 23.000000
      vertex 16.135899 346.484406 23.000000
    endloop
  endfacet
  facet normal 0.793353 0.000000 -0.608762
    outer loop
      vertex 16.771574 346.484406 23.828426
      vertex 16.771574 344.884399 23.828426
      vertex 16.135899 346.484406 23.000000
    endloop
  endfacet
  facet normal 0.608762 0.000000 -0.793353
    outer loop
      vertex 17.600000 344.884399 24.464102
      vertex 16.771574 344.884399 23.828426
      vertex 16.771574 346.484406 23.828426
    endloop
  endfacet
  facet normal 0.608762 0.000000 -0.793353
    outer loop
      vertex 17.600000 346.484406 24.464102
      vertex 17.600000 344.884399 24.464102
      vertex 16.771574 346.484406 23.828426
    endloop
  endfacet
  facet normal 0.382683 0.000000 -0.923880
    outer loop
      vertex 18.564724 344.884399 24.863703
      vertex 17.600000 344.884399 24.464102
      vertex 17.600000 346.484406 24.464102
    endloop
  endfacet
  facet normal 0.382683 0.000000 -0.923880
    outer loop
      vertex 18.564724 346.484406 24.863703
      vertex 18.564724 344.884399 24.863703
      vertex 17.600000 346.484406 24.464102
    endloop
  endfacet
  facet normal 0.130527 0.000000 -0.991445
    outer loop
      vertex 19.600000 344.884399 25.000000
      vertex 18.564724 344.884399 24.863703
      vertex 18.564724 346.484406 24.863703
    endloop
  endfacet
  facet normal 0.130527 0.000000 -0.991445
    outer loop
      vertex 19.600000 346.484406 25.000000
      vertex 19.600000 344.884399 25.000000
      vertex 18.564724 346.484406 24.863703
    endloop
  endfacet
  facet normal -0.130527 0.000000 -0.991445
    outer loop
      vertex 20.635277 344.884399 24.863703
      vertex 19.600000 344.884399 25.000000
      vertex 19.600000 346.484406 25.000000
    endloop
  endfacet
  facet normal -0.130527 -0.000000 -0.991445
    outer loop
      vertex 20.635277 346.484406 24.863703
      vertex 20.635277 344.884399 24.863703
      vertex 19.600000 346.484406 25.000000
    endloop
  endfacet
  facet normal -0.382683 0.000000 -0.923880
    outer loop
      vertex 21.600000 344.884399 24.464102
      vertex 20.635277 344.884399 24.863703
      vertex 20.635277 346.484406 24.863703
    endloop
  endfacet
  facet normal -0.382683 -0.000000 -0.923880
    outer loop
      vertex 21.600000 346.484406 24.464102
      vertex 21.600000 344.884399 24.464102
      vertex 20.635277 346.484406 24.863703
    endloop
  endfacet
  facet normal -0.608761 0.000000 -0.793353
    outer loop
      vertex 22.428429 344.884399 23.828426
      vertex 21.600000 344.884399 24.464102
      vertex 21.600000 346.484406 24.464102
    endloop
  endfacet
  facet normal -0.608761 -0.000000 -0.793353
    outer loop
      vertex 22.428429 346.484406 23.828426
      vertex 22.428429 344.884399 23.828426
      vertex 21.600000 346.484406 24.464102
    endloop
  endfacet
  facet normal -0.793353 0.000000 -0.608761
    outer loop
      vertex 23.064102 344.884399 23.000000
      vertex 22.428429 344.884399 23.828426
      vertex 22.428429 346.484406 23.828426
    endloop
  endfacet
  facet normal -0.793353 -0.000000 -0.608761
    outer loop
      vertex 23.064102 346.484406 23.000000
      vertex 23.064102 344.884399 23.000000
      vertex 22.428429 346.484406 23.828426
    endloop
  endfacet
  facet normal -0.923879 0.000000 -0.382684
    outer loop
      vertex 23.463705 344.884399 22.035276
      vertex 23.064102 344.884399 23.000000
      vertex 23.064102 346.484406 23.000000
    endloop
  endfacet
  facet normal -0.923879 -0.000000 -0.382684
    outer loop
      vertex 23.463705 346.484406 22.035276
      vertex 23.463705 344.884399 22.035276
      vertex 23.064102 346.484406 23.000000
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 0.000001 307.884399 11.600000
      vertex 1.100001 307.884399 11.600000
      vertex 1.100001 307.884399 30.600000
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 0.000001 307.884399 30.600000
      vertex 0.000001 307.884399 11.600000
      vertex 1.100001 307.884399 30.600000
    endloop
  endfacet
  facet normal -0.000000 1.000000 0.000000
    outer loop
      vertex 0.000001 312.884399 30.600000
      vertex 1.100001 312.884399 30.600000
      vertex 1.100001 312.884399 11.600000
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 0.000001 312.884399 11.600000
      vertex 0.000001 312.884399 30.600000
      vertex 1.100001 312.884399 11.600000
    endloop
  endfacet
  facet normal -0.991445 -0.130528 0.000000
    outer loop
      vertex 7.850001 281.384399 11.600000
      vertex 7.773334 281.966736 11.600000
      vertex 7.773334 281.966736 7.000000
    endloop
  endfacet
  facet normal -0.991445 -0.130528 0.000000
    outer loop
      vertex 7.850001 281.384399 7.000000
      vertex 7.850001 281.384399 11.600000
      vertex 7.773334 281.966736 7.000000
    endloop
  endfacet
  facet normal -0.991445 0.130528 0.000000
    outer loop
      vertex 7.773334 280.802063 11.600000
      vertex 7.850001 281.384399 11.600000
      vertex 7.850001 281.384399 7.000000
    endloop
  endfacet
  facet normal -0.991445 0.130528 0.000000
    outer loop
      vertex 7.773334 280.802063 7.000000
      vertex 7.773334 280.802063 11.600000
      vertex 7.850001 281.384399 7.000000
    endloop
  endfacet
  facet normal -0.923881 0.382679 0.000000
    outer loop
      vertex 7.548558 280.259399 11.600000
      vertex 7.773334 280.802063 11.600000
      vertex 7.773334 280.802063 7.000000
    endloop
  endfacet
  facet normal -0.923881 0.382679 0.000000
    outer loop
      vertex 7.548558 280.259399 7.000000
      vertex 7.548558 280.259399 11.600000
      vertex 7.773334 280.802063 7.000000
    endloop
  endfacet
  facet normal -0.793362 0.608751 0.000000
    outer loop
      vertex 7.190991 279.793396 11.600000
      vertex 7.548558 280.259399 11.600000
      vertex 7.548558 280.259399 7.000000
    endloop
  endfacet
  facet normal -0.793362 0.608751 0.000000
    outer loop
      vertex 7.190991 279.793396 7.000000
      vertex 7.190991 279.793396 11.600000
      vertex 7.548558 280.259399 7.000000
    endloop
  endfacet
  facet normal -0.608737 0.793372 0.000000
    outer loop
      vertex 6.725001 279.435852 11.600000
      vertex 7.190991 279.793396 11.600000
      vertex 7.190991 279.793396 7.000000
    endloop
  endfacet
  facet normal -0.608737 0.793372 0.000000
    outer loop
      vertex 6.725001 279.435852 7.000000
      vertex 6.725001 279.435852 11.600000
      vertex 7.190991 279.793396 7.000000
    endloop
  endfacet
  facet normal -0.382708 0.923870 0.000000
    outer loop
      vertex 6.182344 279.211060 11.600000
      vertex 6.725001 279.435852 11.600000
      vertex 6.725001 279.435852 7.000000
    endloop
  endfacet
  facet normal -0.382708 0.923870 0.000000
    outer loop
      vertex 6.182344 279.211060 7.000000
      vertex 6.182344 279.211060 11.600000
      vertex 6.725001 279.435852 7.000000
    endloop
  endfacet
  facet normal -0.130515 0.991446 0.000000
    outer loop
      vertex 5.600001 279.134399 11.600000
      vertex 6.182344 279.211060 11.600000
      vertex 6.182344 279.211060 7.000000
    endloop
  endfacet
  facet normal -0.130515 0.991446 0.000000
    outer loop
      vertex 5.600001 279.134399 7.000000
      vertex 5.600001 279.134399 11.600000
      vertex 6.182344 279.211060 7.000000
    endloop
  endfacet
  facet normal 0.130515 0.991446 0.000000
    outer loop
      vertex 5.017658 279.211060 11.600000
      vertex 5.600001 279.134399 11.600000
      vertex 5.600001 279.134399 7.000000
    endloop
  endfacet
  facet normal 0.130515 0.991446 -0.000000
    outer loop
      vertex 5.017658 279.211060 7.000000
      vertex 5.017658 279.211060 11.600000
      vertex 5.600001 279.134399 7.000000
    endloop
  endfacet
  facet normal 0.382707 0.923870 0.000000
    outer loop
      vertex 4.475001 279.435852 11.600000
      vertex 5.017658 279.211060 11.600000
      vertex 5.017658 279.211060 7.000000
    endloop
  endfacet
  facet normal 0.382707 0.923870 -0.000000
    outer loop
      vertex 4.475001 279.435852 7.000000
      vertex 4.475001 279.435852 11.600000
      vertex 5.017658 279.211060 7.000000
    endloop
  endfacet
  facet normal 0.608737 0.793372 0.000000
    outer loop
      vertex 4.009011 279.793396 11.600000
      vertex 4.475001 279.435852 11.600000
      vertex 4.475001 279.435852 7.000000
    endloop
  endfacet
  facet normal 0.608737 0.793372 -0.000000
    outer loop
      vertex 4.009011 279.793396 7.000000
      vertex 4.009011 279.793396 11.600000
      vertex 4.475001 279.435852 7.000000
    endloop
  endfacet
  facet normal 0.793362 0.608751 0.000000
    outer loop
      vertex 3.651444 280.259399 11.600000
      vertex 4.009011 279.793396 11.600000
      vertex 4.009011 279.793396 7.000000
    endloop
  endfacet
  facet normal 0.793362 0.608751 -0.000000
    outer loop
      vertex 3.651444 280.259399 7.000000
      vertex 3.651444 280.259399 11.600000
      vertex 4.009011 279.793396 7.000000
    endloop
  endfacet
  facet normal 0.923881 0.382680 0.000000
    outer loop
      vertex 3.426668 280.802063 11.600000
      vertex 3.651444 280.259399 11.600000
      vertex 3.651444 280.259399 7.000000
    endloop
  endfacet
  facet normal 0.923881 0.382680 -0.000000
    outer loop
      vertex 3.426668 280.802063 7.000000
      vertex 3.426668 280.802063 11.600000
      vertex 3.651444 280.259399 7.000000
    endloop
  endfacet
  facet normal 0.991445 0.130528 0.000000
    outer loop
      vertex 3.350001 281.384399 11.600000
      vertex 3.426668 280.802063 11.600000
      vertex 3.426668 280.802063 7.000000
    endloop
  endfacet
  facet normal 0.991445 0.130528 -0.000000
    outer loop
      vertex 3.350001 281.384399 7.000000
      vertex 3.350001 281.384399 11.600000
      vertex 3.426668 280.802063 7.000000
    endloop
  endfacet
  facet normal 0.991445 -0.130528 0.000000
    outer loop
      vertex 3.426668 281.966736 11.600000
      vertex 3.350001 281.384399 11.600000
      vertex 3.350001 281.384399 7.000000
    endloop
  endfacet
  facet normal 0.991445 -0.130528 0.000000
    outer loop
      vertex 3.426668 281.966736 7.000000
      vertex 3.426668 281.966736 11.600000
      vertex 3.350001 281.384399 7.000000
    endloop
  endfacet
  facet normal 0.923881 -0.382680 0.000000
    outer loop
      vertex 3.651444 282.509399 11.600000
      vertex 3.426668 281.966736 11.600000
      vertex 3.426668 281.966736 7.000000
    endloop
  endfacet
  facet normal 0.923881 -0.382680 0.000000
    outer loop
      vertex 3.651444 282.509399 7.000000
      vertex 3.651444 282.509399 11.600000
      vertex 3.426668 281.966736 7.000000
    endloop
  endfacet
  facet normal 0.793342 -0.608776 0.000000
    outer loop
      vertex 4.009011 282.975372 11.600000
      vertex 3.651444 282.509399 11.600000
      vertex 3.651444 282.509399 7.000000
    endloop
  endfacet
  facet normal 0.793342 -0.608776 0.000000
    outer loop
      vertex 4.009011 282.975372 7.000000
      vertex 4.009011 282.975372 11.600000
      vertex 3.651444 282.509399 7.000000
    endloop
  endfacet
  facet normal 0.608770 -0.793347 0.000000
    outer loop
      vertex 4.475001 283.332947 11.600000
      vertex 4.009011 282.975372 11.600000
      vertex 4.009011 282.975372 7.000000
    endloop
  endfacet
  facet normal 0.608770 -0.793347 0.000000
    outer loop
      vertex 4.475001 283.332947 7.000000
      vertex 4.475001 283.332947 11.600000
      vertex 4.009011 282.975372 7.000000
    endloop
  endfacet
  facet normal 0.382707 -0.923870 0.000000
    outer loop
      vertex 5.017658 283.557739 11.600000
      vertex 4.475001 283.332947 11.600000
      vertex 4.475001 283.332947 7.000000
    endloop
  endfacet
  facet normal 0.382707 -0.923870 0.000000
    outer loop
      vertex 5.017658 283.557739 7.000000
      vertex 5.017658 283.557739 11.600000
      vertex 4.475001 283.332947 7.000000
    endloop
  endfacet
  facet normal 0.130515 -0.991446 0.000000
    outer loop
      vertex 5.600001 283.634399 11.600000
      vertex 5.017658 283.557739 11.600000
      vertex 5.017658 283.557739 7.000000
    endloop
  endfacet
  facet normal 0.130515 -0.991446 0.000000
    outer loop
      vertex 5.600001 283.634399 7.000000
      vertex 5.600001 283.634399 11.600000
      vertex 5.017658 283.557739 7.000000
    endloop
  endfacet
  facet normal -0.130515 -0.991446 0.000000
    outer loop
      vertex 6.182344 283.557739 11.600000
      vertex 5.600001 283.634399 11.600000
      vertex 5.600001 283.634399 7.000000
    endloop
  endfacet
  facet normal -0.130515 -0.991446 0.000000
    outer loop
      vertex 6.182344 283.557739 7.000000
      vertex 6.182344 283.557739 11.600000
      vertex 5.600001 283.634399 7.000000
    endloop
  endfacet
  facet normal -0.382708 -0.923870 0.000000
    outer loop
      vertex 6.725001 283.332947 11.600000
      vertex 6.182344 283.557739 11.600000
      vertex 6.182344 283.557739 7.000000
    endloop
  endfacet
  facet normal -0.382708 -0.923870 0.000000
    outer loop
      vertex 6.725001 283.332947 7.000000
      vertex 6.725001 283.332947 11.600000
      vertex 6.182344 283.557739 7.000000
    endloop
  endfacet
  facet normal -0.608769 -0.793347 0.000000
    outer loop
      vertex 7.190991 282.975372 11.600000
      vertex 6.725001 283.332947 11.600000
      vertex 6.725001 283.332947 7.000000
    endloop
  endfacet
  facet normal -0.608769 -0.793347 0.000000
    outer loop
      vertex 7.190991 282.975372 7.000000
      vertex 7.190991 282.975372 11.600000
      vertex 6.725001 283.332947 7.000000
    endloop
  endfacet
  facet normal -0.793342 -0.608776 0.000000
    outer loop
      vertex 7.548558 282.509399 11.600000
      vertex 7.190991 282.975372 11.600000
      vertex 7.190991 282.975372 7.000000
    endloop
  endfacet
  facet normal -0.793342 -0.608776 0.000000
    outer loop
      vertex 7.548558 282.509399 7.000000
      vertex 7.548558 282.509399 11.600000
      vertex 7.190991 282.975372 7.000000
    endloop
  endfacet
  facet normal -0.923881 -0.382679 0.000000
    outer loop
      vertex 7.773334 281.966736 11.600000
      vertex 7.548558 282.509399 11.600000
      vertex 7.548558 282.509399 7.000000
    endloop
  endfacet
  facet normal -0.923881 -0.382679 0.000000
    outer loop
      vertex 7.773334 281.966736 7.000000
      vertex 7.773334 281.966736 11.600000
      vertex 7.548558 282.509399 7.000000
    endloop
  endfacet
  facet normal -0.991445 -0.130528 0.000000
    outer loop
      vertex 7.850001 339.384399 11.600000
      vertex 7.773334 339.966736 11.600000
      vertex 7.773334 339.966736 7.000000
    endloop
  endfacet
  facet normal -0.991445 -0.130528 0.000000
    outer loop
      vertex 7.850001 339.384399 7.000000
      vertex 7.850001 339.384399 11.600000
      vertex 7.773334 339.966736 7.000000
    endloop
  endfacet
  facet normal -0.991445 0.130528 0.000000
    outer loop
      vertex 7.773334 338.802063 11.600000
      vertex 7.850001 339.384399 11.600000
      vertex 7.850001 339.384399 7.000000
    endloop
  endfacet
  facet normal -0.991445 0.130528 0.000000
    outer loop
      vertex 7.773334 338.802063 7.000000
      vertex 7.773334 338.802063 11.600000
      vertex 7.850001 339.384399 7.000000
    endloop
  endfacet
  facet normal -0.923881 0.382679 0.000000
    outer loop
      vertex 7.548558 338.259399 11.600000
      vertex 7.773334 338.802063 11.600000
      vertex 7.773334 338.802063 7.000000
    endloop
  endfacet
  facet normal -0.923881 0.382679 0.000000
    outer loop
      vertex 7.548558 338.259399 7.000000
      vertex 7.548558 338.259399 11.600000
      vertex 7.773334 338.802063 7.000000
    endloop
  endfacet
  facet normal -0.793362 0.608751 0.000000
    outer loop
      vertex 7.190991 337.793396 11.600000
      vertex 7.548558 338.259399 11.600000
      vertex 7.548558 338.259399 7.000000
    endloop
  endfacet
  facet normal -0.793362 0.608751 0.000000
    outer loop
      vertex 7.190991 337.793396 7.000000
      vertex 7.190991 337.793396 11.600000
      vertex 7.548558 338.259399 7.000000
    endloop
  endfacet
  facet normal -0.608737 0.793372 0.000000
    outer loop
      vertex 6.725001 337.435852 11.600000
      vertex 7.190991 337.793396 11.600000
      vertex 7.190991 337.793396 7.000000
    endloop
  endfacet
  facet normal -0.608737 0.793372 0.000000
    outer loop
      vertex 6.725001 337.435852 7.000000
      vertex 6.725001 337.435852 11.600000
      vertex 7.190991 337.793396 7.000000
    endloop
  endfacet
  facet normal -0.382708 0.923870 0.000000
    outer loop
      vertex 6.182344 337.211060 11.600000
      vertex 6.725001 337.435852 11.600000
      vertex 6.725001 337.435852 7.000000
    endloop
  endfacet
  facet normal -0.382708 0.923870 0.000000
    outer loop
      vertex 6.182344 337.211060 7.000000
      vertex 6.182344 337.211060 11.600000
      vertex 6.725001 337.435852 7.000000
    endloop
  endfacet
  facet normal -0.130515 0.991446 0.000000
    outer loop
      vertex 5.600001 337.134399 11.600000
      vertex 6.182344 337.211060 11.600000
      vertex 6.182344 337.211060 7.000000
    endloop
  endfacet
  facet normal -0.130515 0.991446 0.000000
    outer loop
      vertex 5.600001 337.134399 7.000000
      vertex 5.600001 337.134399 11.600000
      vertex 6.182344 337.211060 7.000000
    endloop
  endfacet
  facet normal 0.130515 0.991446 0.000000
    outer loop
      vertex 5.017658 337.211060 11.600000
      vertex 5.600001 337.134399 11.600000
      vertex 5.600001 337.134399 7.000000
    endloop
  endfacet
  facet normal 0.130515 0.991446 -0.000000
    outer loop
      vertex 5.017658 337.211060 7.000000
      vertex 5.017658 337.211060 11.600000
      vertex 5.600001 337.134399 7.000000
    endloop
  endfacet
  facet normal 0.382707 0.923870 0.000000
    outer loop
      vertex 4.475001 337.435852 11.600000
      vertex 5.017658 337.211060 11.600000
      vertex 5.017658 337.211060 7.000000
    endloop
  endfacet
  facet normal 0.382707 0.923870 -0.000000
    outer loop
      vertex 4.475001 337.435852 7.000000
      vertex 4.475001 337.435852 11.600000
      vertex 5.017658 337.211060 7.000000
    endloop
  endfacet
  facet normal 0.608737 0.793372 0.000000
    outer loop
      vertex 4.009011 337.793396 11.600000
      vertex 4.475001 337.435852 11.600000
      vertex 4.475001 337.435852 7.000000
    endloop
  endfacet
  facet normal 0.608737 0.793372 -0.000000
    outer loop
      vertex 4.009011 337.793396 7.000000
      vertex 4.009011 337.793396 11.600000
      vertex 4.475001 337.435852 7.000000
    endloop
  endfacet
  facet normal 0.793362 0.608751 0.000000
    outer loop
      vertex 3.651444 338.259399 11.600000
      vertex 4.009011 337.793396 11.600000
      vertex 4.009011 337.793396 7.000000
    endloop
  endfacet
  facet normal 0.793362 0.608751 -0.000000
    outer loop
      vertex 3.651444 338.259399 7.000000
      vertex 3.651444 338.259399 11.600000
      vertex 4.009011 337.793396 7.000000
    endloop
  endfacet
  facet normal 0.923881 0.382680 0.000000
    outer loop
      vertex 3.426668 338.802063 11.600000
      vertex 3.651444 338.259399 11.600000
      vertex 3.651444 338.259399 7.000000
    endloop
  endfacet
  facet normal 0.923881 0.382680 -0.000000
    outer loop
      vertex 3.426668 338.802063 7.000000
      vertex 3.426668 338.802063 11.600000
      vertex 3.651444 338.259399 7.000000
    endloop
  endfacet
  facet normal 0.991445 0.130528 0.000000
    outer loop
      vertex 3.350001 339.384399 11.600000
      vertex 3.426668 338.802063 11.600000
      vertex 3.426668 338.802063 7.000000
    endloop
  endfacet
  facet normal 0.991445 0.130528 -0.000000
    outer loop
      vertex 3.350001 339.384399 7.000000
      vertex 3.350001 339.384399 11.600000
      vertex 3.426668 338.802063 7.000000
    endloop
  endfacet
  facet normal 0.991445 -0.130528 0.000000
    outer loop
      vertex 3.426668 339.966736 11.600000
      vertex 3.350001 339.384399 11.600000
      vertex 3.350001 339.384399 7.000000
    endloop
  endfacet
  facet normal 0.991445 -0.130528 0.000000
    outer loop
      vertex 3.426668 339.966736 7.000000
      vertex 3.426668 339.966736 11.600000
      vertex 3.350001 339.384399 7.000000
    endloop
  endfacet
  facet normal 0.923881 -0.382680 0.000000
    outer loop
      vertex 3.651444 340.509399 11.600000
      vertex 3.426668 339.966736 11.600000
      vertex 3.426668 339.966736 7.000000
    endloop
  endfacet
  facet normal 0.923881 -0.382680 0.000000
    outer loop
      vertex 3.651444 340.509399 7.000000
      vertex 3.651444 340.509399 11.600000
      vertex 3.426668 339.966736 7.000000
    endloop
  endfacet
  facet normal 0.793342 -0.608776 0.000000
    outer loop
      vertex 4.009011 340.975372 11.600000
      vertex 3.651444 340.509399 11.600000
      vertex 3.651444 340.509399 7.000000
    endloop
  endfacet
  facet normal 0.793342 -0.608776 0.000000
    outer loop
      vertex 4.009011 340.975372 7.000000
      vertex 4.009011 340.975372 11.600000
      vertex 3.651444 340.509399 7.000000
    endloop
  endfacet
  facet normal 0.608770 -0.793347 0.000000
    outer loop
      vertex 4.475001 341.332947 11.600000
      vertex 4.009011 340.975372 11.600000
      vertex 4.009011 340.975372 7.000000
    endloop
  endfacet
  facet normal 0.608770 -0.793347 0.000000
    outer loop
      vertex 4.475001 341.332947 7.000000
      vertex 4.475001 341.332947 11.600000
      vertex 4.009011 340.975372 7.000000
    endloop
  endfacet
  facet normal 0.382707 -0.923870 0.000000
    outer loop
      vertex 5.017658 341.557739 11.600000
      vertex 4.475001 341.332947 11.600000
      vertex 4.475001 341.332947 7.000000
    endloop
  endfacet
  facet normal 0.382707 -0.923870 0.000000
    outer loop
      vertex 5.017658 341.557739 7.000000
      vertex 5.017658 341.557739 11.600000
      vertex 4.475001 341.332947 7.000000
    endloop
  endfacet
  facet normal 0.130515 -0.991446 0.000000
    outer loop
      vertex 5.600001 341.634399 11.600000
      vertex 5.017658 341.557739 11.600000
      vertex 5.017658 341.557739 7.000000
    endloop
  endfacet
  facet normal 0.130515 -0.991446 0.000000
    outer loop
      vertex 5.600001 341.634399 7.000000
      vertex 5.600001 341.634399 11.600000
      vertex 5.017658 341.557739 7.000000
    endloop
  endfacet
  facet normal -0.130515 -0.991446 0.000000
    outer loop
      vertex 6.182344 341.557739 11.600000
      vertex 5.600001 341.634399 11.600000
      vertex 5.600001 341.634399 7.000000
    endloop
  endfacet
  facet normal -0.130515 -0.991446 0.000000
    outer loop
      vertex 6.182344 341.557739 7.000000
      vertex 6.182344 341.557739 11.600000
      vertex 5.600001 341.634399 7.000000
    endloop
  endfacet
  facet normal -0.382708 -0.923870 0.000000
    outer loop
      vertex 6.725001 341.332947 11.600000
      vertex 6.182344 341.557739 11.600000
      vertex 6.182344 341.557739 7.000000
    endloop
  endfacet
  facet normal -0.382708 -0.923870 0.000000
    outer loop
      vertex 6.725001 341.332947 7.000000
      vertex 6.725001 341.332947 11.600000
      vertex 6.182344 341.557739 7.000000
    endloop
  endfacet
  facet normal -0.608769 -0.793347 0.000000
    outer loop
      vertex 7.190991 340.975372 11.600000
      vertex 6.725001 341.332947 11.600000
      vertex 6.725001 341.332947 7.000000
    endloop
  endfacet
  facet normal -0.608769 -0.793347 0.000000
    outer loop
      vertex 7.190991 340.975372 7.000000
      vertex 7.190991 340.975372 11.600000
      vertex 6.725001 341.332947 7.000000
    endloop
  endfacet
  facet normal -0.793342 -0.608776 0.000000
    outer loop
      vertex 7.548558 340.509399 11.600000
      vertex 7.190991 340.975372 11.600000
      vertex 7.190991 340.975372 7.000000
    endloop
  endfacet
  facet normal -0.793342 -0.608776 0.000000
    outer loop
      vertex 7.548558 340.509399 7.000000
      vertex 7.548558 340.509399 11.600000
      vertex 7.190991 340.975372 7.000000
    endloop
  endfacet
  facet normal -0.923881 -0.382679 0.000000
    outer loop
      vertex 7.773334 339.966736 11.600000
      vertex 7.548558 340.509399 11.600000
      vertex 7.548558 340.509399 7.000000
    endloop
  endfacet
  facet normal -0.923881 -0.382679 0.000000
    outer loop
      vertex 7.773334 339.966736 7.000000
      vertex 7.773334 339.966736 11.600000
      vertex 7.548558 340.509399 7.000000
    endloop
  endfacet
  facet normal -0.991445 -0.130526 0.000000
    outer loop
      vertex 30.850000 339.384399 11.600000
      vertex 30.773335 339.966736 11.600000
      vertex 30.773335 339.966736 7.000000
    endloop
  endfacet
  facet normal -0.991445 -0.130526 0.000000
    outer loop
      vertex 30.850000 339.384399 7.000000
      vertex 30.850000 339.384399 11.600000
      vertex 30.773335 339.966736 7.000000
    endloop
  endfacet
  facet normal -0.991445 0.130526 0.000000
    outer loop
      vertex 30.773335 338.802063 11.600000
      vertex 30.850000 339.384399 11.600000
      vertex 30.850000 339.384399 7.000000
    endloop
  endfacet
  facet normal -0.991445 0.130526 0.000000
    outer loop
      vertex 30.773335 338.802063 7.000000
      vertex 30.773335 338.802063 11.600000
      vertex 30.850000 339.384399 7.000000
    endloop
  endfacet
  facet normal -0.923880 0.382681 0.000000
    outer loop
      vertex 30.548557 338.259399 11.600000
      vertex 30.773335 338.802063 11.600000
      vertex 30.773335 338.802063 7.000000
    endloop
  endfacet
  facet normal -0.923880 0.382681 0.000000
    outer loop
      vertex 30.548557 338.259399 7.000000
      vertex 30.548557 338.259399 11.600000
      vertex 30.773335 338.802063 7.000000
    endloop
  endfacet
  facet normal -0.793362 0.608751 0.000000
    outer loop
      vertex 30.190990 337.793396 11.600000
      vertex 30.548557 338.259399 11.600000
      vertex 30.548557 338.259399 7.000000
    endloop
  endfacet
  facet normal -0.793362 0.608751 0.000000
    outer loop
      vertex 30.190990 337.793396 7.000000
      vertex 30.190990 337.793396 11.600000
      vertex 30.548557 338.259399 7.000000
    endloop
  endfacet
  facet normal -0.608737 0.793372 0.000000
    outer loop
      vertex 29.725000 337.435852 11.600000
      vertex 30.190990 337.793396 11.600000
      vertex 30.190990 337.793396 7.000000
    endloop
  endfacet
  facet normal -0.608737 0.793372 0.000000
    outer loop
      vertex 29.725000 337.435852 7.000000
      vertex 29.725000 337.435852 11.600000
      vertex 30.190990 337.793396 7.000000
    endloop
  endfacet
  facet normal -0.382708 0.923869 0.000000
    outer loop
      vertex 29.182344 337.211060 11.600000
      vertex 29.725000 337.435852 11.600000
      vertex 29.725000 337.435852 7.000000
    endloop
  endfacet
  facet normal -0.382708 0.923869 0.000000
    outer loop
      vertex 29.182344 337.211060 7.000000
      vertex 29.182344 337.211060 11.600000
      vertex 29.725000 337.435852 7.000000
    endloop
  endfacet
  facet normal -0.130515 0.991446 0.000000
    outer loop
      vertex 28.600000 337.134399 11.600000
      vertex 29.182344 337.211060 11.600000
      vertex 29.182344 337.211060 7.000000
    endloop
  endfacet
  facet normal -0.130515 0.991446 0.000000
    outer loop
      vertex 28.600000 337.134399 7.000000
      vertex 28.600000 337.134399 11.600000
      vertex 29.182344 337.211060 7.000000
    endloop
  endfacet
  facet normal 0.130515 0.991446 0.000000
    outer loop
      vertex 28.017658 337.211060 11.600000
      vertex 28.600000 337.134399 11.600000
      vertex 28.600000 337.134399 7.000000
    endloop
  endfacet
  facet normal 0.130515 0.991446 -0.000000
    outer loop
      vertex 28.017658 337.211060 7.000000
      vertex 28.017658 337.211060 11.600000
      vertex 28.600000 337.134399 7.000000
    endloop
  endfacet
  facet normal 0.382707 0.923870 0.000000
    outer loop
      vertex 27.475000 337.435852 11.600000
      vertex 28.017658 337.211060 11.600000
      vertex 28.017658 337.211060 7.000000
    endloop
  endfacet
  facet normal 0.382707 0.923870 -0.000000
    outer loop
      vertex 27.475000 337.435852 7.000000
      vertex 27.475000 337.435852 11.600000
      vertex 28.017658 337.211060 7.000000
    endloop
  endfacet
  facet normal 0.608737 0.793372 0.000000
    outer loop
      vertex 27.009010 337.793396 11.600000
      vertex 27.475000 337.435852 11.600000
      vertex 27.475000 337.435852 7.000000
    endloop
  endfacet
  facet normal 0.608737 0.793372 -0.000000
    outer loop
      vertex 27.009010 337.793396 7.000000
      vertex 27.009010 337.793396 11.600000
      vertex 27.475000 337.435852 7.000000
    endloop
  endfacet
  facet normal 0.793362 0.608751 0.000000
    outer loop
      vertex 26.651443 338.259399 11.600000
      vertex 27.009010 337.793396 11.600000
      vertex 27.009010 337.793396 7.000000
    endloop
  endfacet
  facet normal 0.793362 0.608751 -0.000000
    outer loop
      vertex 26.651443 338.259399 7.000000
      vertex 26.651443 338.259399 11.600000
      vertex 27.009010 337.793396 7.000000
    endloop
  endfacet
  facet normal 0.923881 0.382679 0.000000
    outer loop
      vertex 26.426668 338.802063 11.600000
      vertex 26.651443 338.259399 11.600000
      vertex 26.651443 338.259399 7.000000
    endloop
  endfacet
  facet normal 0.923881 0.382679 -0.000000
    outer loop
      vertex 26.426668 338.802063 7.000000
      vertex 26.426668 338.802063 11.600000
      vertex 26.651443 338.259399 7.000000
    endloop
  endfacet
  facet normal 0.991444 0.130529 0.000000
    outer loop
      vertex 26.350000 339.384399 11.600000
      vertex 26.426668 338.802063 11.600000
      vertex 26.426668 338.802063 7.000000
    endloop
  endfacet
  facet normal 0.991444 0.130529 -0.000000
    outer loop
      vertex 26.350000 339.384399 7.000000
      vertex 26.350000 339.384399 11.600000
      vertex 26.426668 338.802063 7.000000
    endloop
  endfacet
  facet normal 0.991444 -0.130529 0.000000
    outer loop
      vertex 26.426668 339.966736 11.600000
      vertex 26.350000 339.384399 11.600000
      vertex 26.350000 339.384399 7.000000
    endloop
  endfacet
  facet normal 0.991444 -0.130529 0.000000
    outer loop
      vertex 26.426668 339.966736 7.000000
      vertex 26.426668 339.966736 11.600000
      vertex 26.350000 339.384399 7.000000
    endloop
  endfacet
  facet normal 0.923881 -0.382679 0.000000
    outer loop
      vertex 26.651443 340.509399 11.600000
      vertex 26.426668 339.966736 11.600000
      vertex 26.426668 339.966736 7.000000
    endloop
  endfacet
  facet normal 0.923881 -0.382679 0.000000
    outer loop
      vertex 26.651443 340.509399 7.000000
      vertex 26.651443 340.509399 11.600000
      vertex 26.426668 339.966736 7.000000
    endloop
  endfacet
  facet normal 0.793342 -0.608776 0.000000
    outer loop
      vertex 27.009010 340.975372 11.600000
      vertex 26.651443 340.509399 11.600000
      vertex 26.651443 340.509399 7.000000
    endloop
  endfacet
  facet normal 0.793342 -0.608776 0.000000
    outer loop
      vertex 27.009010 340.975372 7.000000
      vertex 27.009010 340.975372 11.600000
      vertex 26.651443 340.509399 7.000000
    endloop
  endfacet
  facet normal 0.608770 -0.793347 0.000000
    outer loop
      vertex 27.475000 341.332947 11.600000
      vertex 27.009010 340.975372 11.600000
      vertex 27.009010 340.975372 7.000000
    endloop
  endfacet
  facet normal 0.608770 -0.793347 0.000000
    outer loop
      vertex 27.475000 341.332947 7.000000
      vertex 27.475000 341.332947 11.600000
      vertex 27.009010 340.975372 7.000000
    endloop
  endfacet
  facet normal 0.382707 -0.923870 0.000000
    outer loop
      vertex 28.017658 341.557739 11.600000
      vertex 27.475000 341.332947 11.600000
      vertex 27.475000 341.332947 7.000000
    endloop
  endfacet
  facet normal 0.382707 -0.923870 0.000000
    outer loop
      vertex 28.017658 341.557739 7.000000
      vertex 28.017658 341.557739 11.600000
      vertex 27.475000 341.332947 7.000000
    endloop
  endfacet
  facet normal 0.130515 -0.991446 0.000000
    outer loop
      vertex 28.600000 341.634399 11.600000
      vertex 28.017658 341.557739 11.600000
      vertex 28.017658 341.557739 7.000000
    endloop
  endfacet
  facet normal 0.130515 -0.991446 0.000000
    outer loop
      vertex 28.600000 341.634399 7.000000
      vertex 28.600000 341.634399 11.600000
      vertex 28.017658 341.557739 7.000000
    endloop
  endfacet
  facet normal -0.130515 -0.991446 0.000000
    outer loop
      vertex 29.182344 341.557739 11.600000
      vertex 28.600000 341.634399 11.600000
      vertex 28.600000 341.634399 7.000000
    endloop
  endfacet
  facet normal -0.130515 -0.991446 0.000000
    outer loop
      vertex 29.182344 341.557739 7.000000
      vertex 29.182344 341.557739 11.600000
      vertex 28.600000 341.634399 7.000000
    endloop
  endfacet
  facet normal -0.382708 -0.923869 0.000000
    outer loop
      vertex 29.725000 341.332947 11.600000
      vertex 29.182344 341.557739 11.600000
      vertex 29.182344 341.557739 7.000000
    endloop
  endfacet
  facet normal -0.382708 -0.923869 0.000000
    outer loop
      vertex 29.725000 341.332947 7.000000
      vertex 29.725000 341.332947 11.600000
      vertex 29.182344 341.557739 7.000000
    endloop
  endfacet
  facet normal -0.608770 -0.793347 0.000000
    outer loop
      vertex 30.190990 340.975372 11.600000
      vertex 29.725000 341.332947 11.600000
      vertex 29.725000 341.332947 7.000000
    endloop
  endfacet
  facet normal -0.608770 -0.793347 0.000000
    outer loop
      vertex 30.190990 340.975372 7.000000
      vertex 30.190990 340.975372 11.600000
      vertex 29.725000 341.332947 7.000000
    endloop
  endfacet
  facet normal -0.793342 -0.608776 0.000000
    outer loop
      vertex 30.548557 340.509399 11.600000
      vertex 30.190990 340.975372 11.600000
      vertex 30.190990 340.975372 7.000000
    endloop
  endfacet
  facet normal -0.793342 -0.608776 0.000000
    outer loop
      vertex 30.548557 340.509399 7.000000
      vertex 30.548557 340.509399 11.600000
      vertex 30.190990 340.975372 7.000000
    endloop
  endfacet
  facet normal -0.923880 -0.382681 0.000000
    outer loop
      vertex 30.773335 339.966736 11.600000
      vertex 30.548557 340.509399 11.600000
      vertex 30.548557 340.509399 7.000000
    endloop
  endfacet
  facet normal -0.923880 -0.382681 0.000000
    outer loop
      vertex 30.773335 339.966736 7.000000
      vertex 30.773335 339.966736 11.600000
      vertex 30.548557 340.509399 7.000000
    endloop
  endfacet
  facet normal -0.991445 -0.130526 0.000000
    outer loop
      vertex 30.850000 281.384399 11.600000
      vertex 30.773335 281.966736 11.600000
      vertex 30.773335 281.966736 7.000000
    endloop
  endfacet
  facet normal -0.991445 -0.130526 0.000000
    outer loop
      vertex 30.850000 281.384399 7.000000
      vertex 30.850000 281.384399 11.600000
      vertex 30.773335 281.966736 7.000000
    endloop
  endfacet
  facet normal -0.991445 0.130526 0.000000
    outer loop
      vertex 30.773335 280.802063 11.600000
      vertex 30.850000 281.384399 11.600000
      vertex 30.850000 281.384399 7.000000
    endloop
  endfacet
  facet normal -0.991445 0.130526 0.000000
    outer loop
      vertex 30.773335 280.802063 7.000000
      vertex 30.773335 280.802063 11.600000
      vertex 30.850000 281.384399 7.000000
    endloop
  endfacet
  facet normal -0.923880 0.382681 0.000000
    outer loop
      vertex 30.548557 280.259399 11.600000
      vertex 30.773335 280.802063 11.600000
      vertex 30.773335 280.802063 7.000000
    endloop
  endfacet
  facet normal -0.923880 0.382681 0.000000
    outer loop
      vertex 30.548557 280.259399 7.000000
      vertex 30.548557 280.259399 11.600000
      vertex 30.773335 280.802063 7.000000
    endloop
  endfacet
  facet normal -0.793362 0.608751 0.000000
    outer loop
      vertex 30.190990 279.793396 11.600000
      vertex 30.548557 280.259399 11.600000
      vertex 30.548557 280.259399 7.000000
    endloop
  endfacet
  facet normal -0.793362 0.608751 0.000000
    outer loop
      vertex 30.190990 279.793396 7.000000
      vertex 30.190990 279.793396 11.600000
      vertex 30.548557 280.259399 7.000000
    endloop
  endfacet
  facet normal -0.608737 0.793372 0.000000
    outer loop
      vertex 29.725000 279.435852 11.600000
      vertex 30.190990 279.793396 11.600000
      vertex 30.190990 279.793396 7.000000
    endloop
  endfacet
  facet normal -0.608737 0.793372 0.000000
    outer loop
      vertex 29.725000 279.435852 7.000000
      vertex 29.725000 279.435852 11.600000
      vertex 30.190990 279.793396 7.000000
    endloop
  endfacet
  facet normal -0.382708 0.923869 0.000000
    outer loop
      vertex 29.182344 279.211060 11.600000
      vertex 29.725000 279.435852 11.600000
      vertex 29.725000 279.435852 7.000000
    endloop
  endfacet
  facet normal -0.382708 0.923869 0.000000
    outer loop
      vertex 29.182344 279.211060 7.000000
      vertex 29.182344 279.211060 11.600000
      vertex 29.725000 279.435852 7.000000
    endloop
  endfacet
  facet normal -0.130515 0.991446 0.000000
    outer loop
      vertex 28.600000 279.134399 11.600000
      vertex 29.182344 279.211060 11.600000
      vertex 29.182344 279.211060 7.000000
    endloop
  endfacet
  facet normal -0.130515 0.991446 0.000000
    outer loop
      vertex 28.600000 279.134399 7.000000
      vertex 28.600000 279.134399 11.600000
      vertex 29.182344 279.211060 7.000000
    endloop
  endfacet
  facet normal 0.130515 0.991446 0.000000
    outer loop
      vertex 28.017658 279.211060 11.600000
      vertex 28.600000 279.134399 11.600000
      vertex 28.600000 279.134399 7.000000
    endloop
  endfacet
  facet normal 0.130515 0.991446 -0.000000
    outer loop
      vertex 28.017658 279.211060 7.000000
      vertex 28.017658 279.211060 11.600000
      vertex 28.600000 279.134399 7.000000
    endloop
  endfacet
  facet normal 0.382707 0.923870 0.000000
    outer loop
      vertex 27.475000 279.435852 11.600000
      vertex 28.017658 279.211060 11.600000
      vertex 28.017658 279.211060 7.000000
    endloop
  endfacet
  facet normal 0.382707 0.923870 -0.000000
    outer loop
      vertex 27.475000 279.435852 7.000000
      vertex 27.475000 279.435852 11.600000
      vertex 28.017658 279.211060 7.000000
    endloop
  endfacet
  facet normal 0.608737 0.793372 0.000000
    outer loop
      vertex 27.009010 279.793396 11.600000
      vertex 27.475000 279.435852 11.600000
      vertex 27.475000 279.435852 7.000000
    endloop
  endfacet
  facet normal 0.608737 0.793372 -0.000000
    outer loop
      vertex 27.009010 279.793396 7.000000
      vertex 27.009010 279.793396 11.600000
      vertex 27.475000 279.435852 7.000000
    endloop
  endfacet
  facet normal 0.793362 0.608751 0.000000
    outer loop
      vertex 26.651443 280.259399 11.600000
      vertex 27.009010 279.793396 11.600000
      vertex 27.009010 279.793396 7.000000
    endloop
  endfacet
  facet normal 0.793362 0.608751 -0.000000
    outer loop
      vertex 26.651443 280.259399 7.000000
      vertex 26.651443 280.259399 11.600000
      vertex 27.009010 279.793396 7.000000
    endloop
  endfacet
  facet normal 0.923881 0.382679 0.000000
    outer loop
      vertex 26.426668 280.802063 11.600000
      vertex 26.651443 280.259399 11.600000
      vertex 26.651443 280.259399 7.000000
    endloop
  endfacet
  facet normal 0.923881 0.382679 -0.000000
    outer loop
      vertex 26.426668 280.802063 7.000000
      vertex 26.426668 280.802063 11.600000
      vertex 26.651443 280.259399 7.000000
    endloop
  endfacet
  facet normal 0.991444 0.130529 0.000000
    outer loop
      vertex 26.350000 281.384399 11.600000
      vertex 26.426668 280.802063 11.600000
      vertex 26.426668 280.802063 7.000000
    endloop
  endfacet
  facet normal 0.991444 0.130529 -0.000000
    outer loop
      vertex 26.350000 281.384399 7.000000
      vertex 26.350000 281.384399 11.600000
      vertex 26.426668 280.802063 7.000000
    endloop
  endfacet
  facet normal 0.991444 -0.130529 0.000000
    outer loop
      vertex 26.426668 281.966736 11.600000
      vertex 26.350000 281.384399 11.600000
      vertex 26.350000 281.384399 7.000000
    endloop
  endfacet
  facet normal 0.991444 -0.130529 0.000000
    outer loop
      vertex 26.426668 281.966736 7.000000
      vertex 26.426668 281.966736 11.600000
      vertex 26.350000 281.384399 7.000000
    endloop
  endfacet
  facet normal 0.923881 -0.382679 0.000000
    outer loop
      vertex 26.651443 282.509399 11.600000
      vertex 26.426668 281.966736 11.600000
      vertex 26.426668 281.966736 7.000000
    endloop
  endfacet
  facet normal 0.923881 -0.382679 0.000000
    outer loop
      vertex 26.651443 282.509399 7.000000
      vertex 26.651443 282.509399 11.600000
      vertex 26.426668 281.966736 7.000000
    endloop
  endfacet
  facet normal 0.793342 -0.608776 0.000000
    outer loop
      vertex 27.009010 282.975372 11.600000
      vertex 26.651443 282.509399 11.600000
      vertex 26.651443 282.509399 7.000000
    endloop
  endfacet
  facet normal 0.793342 -0.608776 0.000000
    outer loop
      vertex 27.009010 282.975372 7.000000
      vertex 27.009010 282.975372 11.600000
      vertex 26.651443 282.509399 7.000000
    endloop
  endfacet
  facet normal 0.608770 -0.793347 0.000000
    outer loop
      vertex 27.475000 283.332947 11.600000
      vertex 27.009010 282.975372 11.600000
      vertex 27.009010 282.975372 7.000000
    endloop
  endfacet
  facet normal 0.608770 -0.793347 0.000000
    outer loop
      vertex 27.475000 283.332947 7.000000
      vertex 27.475000 283.332947 11.600000
      vertex 27.009010 282.975372 7.000000
    endloop
  endfacet
  facet normal 0.382707 -0.923870 0.000000
    outer loop
      vertex 28.017658 283.557739 11.600000
      vertex 27.475000 283.332947 11.600000
      vertex 27.475000 283.332947 7.000000
    endloop
  endfacet
  facet normal 0.382707 -0.923870 0.000000
    outer loop
      vertex 28.017658 283.557739 7.000000
      vertex 28.017658 283.557739 11.600000
      vertex 27.475000 283.332947 7.000000
    endloop
  endfacet
  facet normal 0.130515 -0.991446 0.000000
    outer loop
      vertex 28.600000 283.634399 11.600000
      vertex 28.017658 283.557739 11.600000
      vertex 28.017658 283.557739 7.000000
    endloop
  endfacet
  facet normal 0.130515 -0.991446 0.000000
    outer loop
      vertex 28.600000 283.634399 7.000000
      vertex 28.600000 283.634399 11.600000
      vertex 28.017658 283.557739 7.000000
    endloop
  endfacet
  facet normal -0.130515 -0.991446 0.000000
    outer loop
      vertex 29.182344 283.557739 11.600000
      vertex 28.600000 283.634399 11.600000
      vertex 28.600000 283.634399 7.000000
    endloop
  endfacet
  facet normal -0.130515 -0.991446 0.000000
    outer loop
      vertex 29.182344 283.557739 7.000000
      vertex 29.182344 283.557739 11.600000
      vertex 28.600000 283.634399 7.000000
    endloop
  endfacet
  facet normal -0.382708 -0.923869 0.000000
    outer loop
      vertex 29.725000 283.332947 11.600000
      vertex 29.182344 283.557739 11.600000
      vertex 29.182344 283.557739 7.000000
    endloop
  endfacet
  facet normal -0.382708 -0.923869 0.000000
    outer loop
      vertex 29.725000 283.332947 7.000000
      vertex 29.725000 283.332947 11.600000
      vertex 29.182344 283.557739 7.000000
    endloop
  endfacet
  facet normal -0.608770 -0.793347 0.000000
    outer loop
      vertex 30.190990 282.975372 11.600000
      vertex 29.725000 283.332947 11.600000
      vertex 29.725000 283.332947 7.000000
    endloop
  endfacet
  facet normal -0.608770 -0.793347 0.000000
    outer loop
      vertex 30.190990 282.975372 7.000000
      vertex 30.190990 282.975372 11.600000
      vertex 29.725000 283.332947 7.000000
    endloop
  endfacet
  facet normal -0.793342 -0.608776 0.000000
    outer loop
      vertex 30.548557 282.509399 11.600000
      vertex 30.190990 282.975372 11.600000
      vertex 30.190990 282.975372 7.000000
    endloop
  endfacet
  facet normal -0.793342 -0.608776 0.000000
    outer loop
      vertex 30.548557 282.509399 7.000000
      vertex 30.548557 282.509399 11.600000
      vertex 30.190990 282.975372 7.000000
    endloop
  endfacet
  facet normal -0.923880 -0.382681 0.000000
    outer loop
      vertex 30.773335 281.966736 11.600000
      vertex 30.548557 282.509399 11.600000
      vertex 30.548557 282.509399 7.000000
    endloop
  endfacet
  facet normal -0.923880 -0.382681 0.000000
    outer loop
      vertex 30.773335 281.966736 7.000000
      vertex 30.773335 281.966736 11.600000
      vertex 30.548557 282.509399 7.000000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 307.884399 30.600000
      vertex 0.000001 292.884399 30.600000
      vertex 0.000001 276.484406 33.599998
    endloop
  endfacet
  facet normal -1.000000 -0.000000 -0.000000
    outer loop
      vertex 0.000001 343.284393 33.599998
      vertex 0.000001 307.884399 30.600000
      vertex 0.000001 276.484406 33.599998
    endloop
  endfacet
  facet normal -1.000000 -0.000000 -0.000000
    outer loop
      vertex 0.000001 312.884399 30.600000
      vertex 0.000001 307.884399 30.600000
      vertex 0.000001 343.284393 33.599998
    endloop
  endfacet
  facet normal -1.000000 -0.000000 0.000000
    outer loop
      vertex 0.000001 327.884399 30.600000
      vertex 0.000001 312.884399 30.600000
      vertex 0.000001 343.284393 33.599998
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 329.282013 30.416000
      vertex 0.000001 327.884399 30.600000
      vertex 0.000001 343.284393 33.599998
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 330.584381 29.876537
      vertex 0.000001 329.282013 30.416000
      vertex 0.000001 343.284393 33.599998
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 331.702759 29.018377
      vertex 0.000001 330.584381 29.876537
      vertex 0.000001 343.284393 33.599998
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 332.560944 27.900000
      vertex 0.000001 331.702759 29.018377
      vertex 0.000001 343.284393 33.599998
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 333.100403 26.597622
      vertex 0.000001 332.560944 27.900000
      vertex 0.000001 343.284393 33.599998
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 333.284393 25.200001
      vertex 0.000001 333.100403 26.597622
      vertex 0.000001 343.284393 33.599998
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 333.284393 17.000000
      vertex 0.000001 333.284393 25.200001
      vertex 0.000001 343.284393 33.599998
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 343.284393 7.000000
      vertex 0.000001 333.284393 17.000000
      vertex 0.000001 343.284393 33.599998
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 333.100403 15.602377
      vertex 0.000001 333.284393 17.000000
      vertex 0.000001 343.284393 7.000000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 332.560944 14.300000
      vertex 0.000001 333.100403 15.602377
      vertex 0.000001 343.284393 7.000000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 331.702759 13.181623
      vertex 0.000001 332.560944 14.300000
      vertex 0.000001 343.284393 7.000000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 330.584381 12.323462
      vertex 0.000001 331.702759 13.181623
      vertex 0.000001 343.284393 7.000000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 329.282013 11.784000
      vertex 0.000001 330.584381 12.323462
      vertex 0.000001 343.284393 7.000000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 327.884399 11.600000
      vertex 0.000001 329.282013 11.784000
      vertex 0.000001 343.284393 7.000000
    endloop
  endfacet
  facet normal -1.000000 -0.000000 -0.000000
    outer loop
      vertex 0.000001 312.884399 11.600000
      vertex 0.000001 327.884399 11.600000
      vertex 0.000001 343.284393 7.000000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 307.884399 11.600000
      vertex 0.000001 312.884399 11.600000
      vertex 0.000001 343.284393 7.000000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 307.884399 30.600000
      vertex 0.000001 312.884399 11.600000
      vertex 0.000001 307.884399 11.600000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 276.484406 33.599998
      vertex 0.000001 292.884399 30.600000
      vertex 0.000001 291.486786 30.416000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 290.184387 29.876537
      vertex 0.000001 276.484406 33.599998
      vertex 0.000001 291.486786 30.416000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 289.066010 29.018377
      vertex 0.000001 276.484406 33.599998
      vertex 0.000001 290.184387 29.876537
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 276.484406 33.599998
      vertex 0.000001 289.066010 29.018377
      vertex 0.000001 288.207855 27.900000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 287.668396 26.597622
      vertex 0.000001 276.484406 33.599998
      vertex 0.000001 288.207855 27.900000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 287.484406 25.200001
      vertex 0.000001 276.484406 33.599998
      vertex 0.000001 287.668396 26.597622
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 276.484406 33.599998
      vertex 0.000001 287.484406 25.200001
      vertex 0.000001 287.484406 17.000000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 276.484406 7.000000
      vertex 0.000001 276.484406 33.599998
      vertex 0.000001 287.484406 17.000000
    endloop
  endfacet
  facet normal -1.000000 -0.000000 0.000000
    outer loop
      vertex 0.000001 287.668396 15.602377
      vertex 0.000001 276.484406 7.000000
      vertex 0.000001 287.484406 17.000000
    endloop
  endfacet
  facet normal -1.000000 -0.000000 0.000000
    outer loop
      vertex 0.000001 288.207855 14.300000
      vertex 0.000001 276.484406 7.000000
      vertex 0.000001 287.668396 15.602377
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 276.484406 7.000000
      vertex 0.000001 288.207855 14.300000
      vertex 0.000001 289.066010 13.181623
    endloop
  endfacet
  facet normal -1.000000 -0.000000 0.000000
    outer loop
      vertex 0.000001 290.184387 12.323462
      vertex 0.000001 276.484406 7.000000
      vertex 0.000001 289.066010 13.181623
    endloop
  endfacet
  facet normal -1.000000 -0.000000 0.000000
    outer loop
      vertex 0.000001 291.486786 11.784000
      vertex 0.000001 276.484406 7.000000
      vertex 0.000001 290.184387 12.323462
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 276.484406 7.000000
      vertex 0.000001 291.486786 11.784000
      vertex 0.000001 292.884399 11.600000
    endloop
  endfacet
  facet normal -1.000000 0.000000 -0.000000
    outer loop
      vertex 0.000001 307.884399 11.600000
      vertex 0.000001 276.484406 7.000000
      vertex 0.000001 292.884399 11.600000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 343.284393 7.000000
      vertex 0.000001 276.484406 7.000000
      vertex 0.000001 307.884399 11.600000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 0.000001 307.884399 30.600000
      vertex 0.000001 312.884399 30.600000
      vertex 0.000001 312.884399 11.600000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 276.484406 33.599998
      vertex 41.200001 276.484406 7.000000
      vertex 41.200001 287.484406 17.000000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 287.484406 25.200001
      vertex 41.200001 276.484406 33.599998
      vertex 41.200001 287.484406 17.000000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 287.668396 26.597622
      vertex 41.200001 276.484406 33.599998
      vertex 41.200001 287.484406 25.200001
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 276.484406 7.000000
      vertex 41.200001 343.284393 7.000000
      vertex 41.200001 326.940277 10.525556
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 304.984406 11.600000
      vertex 41.200001 276.484406 7.000000
      vertex 41.200001 326.940277 10.525556
    endloop
  endfacet
  facet normal 1.000000 -0.000000 0.000000
    outer loop
      vertex 41.200001 292.884399 11.600000
      vertex 41.200001 276.484406 7.000000
      vertex 41.200001 304.984406 11.600000
    endloop
  endfacet
  facet normal 1.000000 0.000000 -0.000000
    outer loop
      vertex 41.200001 343.284393 7.000000
      vertex 41.200001 343.284393 33.599998
      vertex 41.200001 337.858826 17.644114
    endloop
  endfacet
  facet normal 1.000000 -0.000000 -0.000000
    outer loop
      vertex 41.200001 337.884399 17.450001
      vertex 41.200001 343.284393 7.000000
      vertex 41.200001 337.858826 17.644114
    endloop
  endfacet
  facet normal 1.000000 -0.000000 0.000000
    outer loop
      vertex 41.200001 337.884399 11.250000
      vertex 41.200001 343.284393 7.000000
      vertex 41.200001 337.884399 17.450001
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 343.284393 33.599998
      vertex 41.200001 276.484406 33.599998
      vertex 41.200001 304.984406 30.600000
    endloop
  endfacet
  facet normal 1.000000 0.000000 -0.000000
    outer loop
      vertex 41.200001 306.382019 30.416000
      vertex 41.200001 343.284393 33.599998
      vertex 41.200001 304.984406 30.600000
    endloop
  endfacet
  facet normal 1.000000 0.000000 -0.000000
    outer loop
      vertex 41.200001 307.684387 29.876537
      vertex 41.200001 343.284393 33.599998
      vertex 41.200001 306.382019 30.416000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 276.484406 33.599998
      vertex 41.200001 287.668396 26.597622
      vertex 41.200001 288.207855 27.900000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 289.066010 29.018377
      vertex 41.200001 276.484406 33.599998
      vertex 41.200001 288.207855 27.900000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 290.184387 29.876537
      vertex 41.200001 276.484406 33.599998
      vertex 41.200001 289.066010 29.018377
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 276.484406 33.599998
      vertex 41.200001 290.184387 29.876537
      vertex 41.200001 291.486786 30.416000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 292.884399 30.600000
      vertex 41.200001 276.484406 33.599998
      vertex 41.200001 291.486786 30.416000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 304.984406 30.600000
      vertex 41.200001 276.484406 33.599998
      vertex 41.200001 292.884399 30.600000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 343.284393 33.599998
      vertex 41.200001 307.684387 29.876537
      vertex 41.200001 308.802765 29.018377
    endloop
  endfacet
  facet normal 1.000000 0.000000 -0.000000
    outer loop
      vertex 41.200001 309.660919 27.900000
      vertex 41.200001 343.284393 33.599998
      vertex 41.200001 308.802765 29.018377
    endloop
  endfacet
  facet normal 1.000000 0.000000 -0.000000
    outer loop
      vertex 41.200001 310.200409 26.597622
      vertex 41.200001 343.284393 33.599998
      vertex 41.200001 309.660919 27.900000
    endloop
  endfacet
  facet normal 1.000000 0.000000 -0.000000
    outer loop
      vertex 41.200001 327.134399 18.200001
      vertex 41.200001 343.284393 33.599998
      vertex 41.200001 310.200409 26.597622
    endloop
  endfacet
  facet normal 1.000000 -0.000000 -0.000000
    outer loop
      vertex 41.200001 310.384399 25.200001
      vertex 41.200001 327.134399 18.200001
      vertex 41.200001 310.200409 26.597622
    endloop
  endfacet
  facet normal 1.000000 0.000000 -0.000000
    outer loop
      vertex 41.200001 326.940277 18.174444
      vertex 41.200001 327.134399 18.200001
      vertex 41.200001 310.384399 25.200001
    endloop
  endfacet
  facet normal 1.000000 0.000000 -0.000000
    outer loop
      vertex 41.200001 326.759399 18.099520
      vertex 41.200001 326.940277 18.174444
      vertex 41.200001 310.384399 25.200001
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 310.384399 17.000000
      vertex 41.200001 326.759399 18.099520
      vertex 41.200001 310.384399 25.200001
    endloop
  endfacet
  facet normal 1.000000 0.000000 -0.000000
    outer loop
      vertex 41.200001 326.604065 17.980330
      vertex 41.200001 326.759399 18.099520
      vertex 41.200001 310.384399 17.000000
    endloop
  endfacet
  facet normal 1.000000 0.000000 -0.000000
    outer loop
      vertex 41.200001 326.484863 17.825001
      vertex 41.200001 326.604065 17.980330
      vertex 41.200001 310.384399 17.000000
    endloop
  endfacet
  facet normal 1.000000 0.000000 -0.000000
    outer loop
      vertex 41.200001 326.409943 17.644114
      vertex 41.200001 326.484863 17.825001
      vertex 41.200001 310.384399 17.000000
    endloop
  endfacet
  facet normal 1.000000 0.000000 -0.000000
    outer loop
      vertex 41.200001 326.384399 17.450001
      vertex 41.200001 326.409943 17.644114
      vertex 41.200001 310.384399 17.000000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 310.200409 15.602377
      vertex 41.200001 326.384399 17.450001
      vertex 41.200001 310.384399 17.000000
    endloop
  endfacet
  facet normal 1.000000 0.000000 -0.000000
    outer loop
      vertex 41.200001 326.384399 11.250000
      vertex 41.200001 326.384399 17.450001
      vertex 41.200001 310.200409 15.602377
    endloop
  endfacet
  facet normal 1.000000 -0.000000 0.000000
    outer loop
      vertex 41.200001 309.660919 14.300000
      vertex 41.200001 326.384399 11.250000
      vertex 41.200001 310.200409 15.602377
    endloop
  endfacet
  facet normal 1.000000 -0.000000 0.000000
    outer loop
      vertex 41.200001 308.802765 13.181623
      vertex 41.200001 326.384399 11.250000
      vertex 41.200001 309.660919 14.300000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 326.384399 11.250000
      vertex 41.200001 308.802765 13.181623
      vertex 41.200001 307.684387 12.323462
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 326.409943 11.055885
      vertex 41.200001 326.384399 11.250000
      vertex 41.200001 307.684387 12.323462
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 326.484863 10.875000
      vertex 41.200001 326.409943 11.055885
      vertex 41.200001 307.684387 12.323462
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 326.604065 10.719670
      vertex 41.200001 326.484863 10.875000
      vertex 41.200001 307.684387 12.323462
    endloop
  endfacet
  facet normal 1.000000 -0.000000 0.000000
    outer loop
      vertex 41.200001 306.382019 11.784000
      vertex 41.200001 326.604065 10.719670
      vertex 41.200001 307.684387 12.323462
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 326.759399 10.600481
      vertex 41.200001 326.604065 10.719670
      vertex 41.200001 306.382019 11.784000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 326.940277 10.525556
      vertex 41.200001 326.759399 10.600481
      vertex 41.200001 306.382019 11.784000
    endloop
  endfacet
  facet normal 1.000000 -0.000000 0.000000
    outer loop
      vertex 41.200001 304.984406 11.600000
      vertex 41.200001 326.940277 10.525556
      vertex 41.200001 306.382019 11.784000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 276.484406 7.000000
      vertex 41.200001 292.884399 11.600000
      vertex 41.200001 291.486786 11.784000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 290.184387 12.323462
      vertex 41.200001 276.484406 7.000000
      vertex 41.200001 291.486786 11.784000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 289.066010 13.181623
      vertex 41.200001 276.484406 7.000000
      vertex 41.200001 290.184387 12.323462
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 276.484406 7.000000
      vertex 41.200001 289.066010 13.181623
      vertex 41.200001 288.207855 14.300000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 287.668396 15.602377
      vertex 41.200001 276.484406 7.000000
      vertex 41.200001 288.207855 14.300000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 287.484406 17.000000
      vertex 41.200001 276.484406 7.000000
      vertex 41.200001 287.668396 15.602377
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 343.284393 33.599998
      vertex 41.200001 327.134399 18.200001
      vertex 41.200001 337.134399 18.200001
    endloop
  endfacet
  facet normal 1.000000 0.000000 -0.000000
    outer loop
      vertex 41.200001 337.328522 18.174444
      vertex 41.200001 343.284393 33.599998
      vertex 41.200001 337.134399 18.200001
    endloop
  endfacet
  facet normal 1.000000 0.000000 -0.000000
    outer loop
      vertex 41.200001 337.509399 18.099520
      vertex 41.200001 343.284393 33.599998
      vertex 41.200001 337.328522 18.174444
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 343.284393 33.599998
      vertex 41.200001 337.509399 18.099520
      vertex 41.200001 337.664734 17.980330
    endloop
  endfacet
  facet normal 1.000000 0.000000 -0.000000
    outer loop
      vertex 41.200001 337.783905 17.825001
      vertex 41.200001 343.284393 33.599998
      vertex 41.200001 337.664734 17.980330
    endloop
  endfacet
  facet normal 1.000000 0.000000 -0.000000
    outer loop
      vertex 41.200001 337.858826 17.644114
      vertex 41.200001 343.284393 33.599998
      vertex 41.200001 337.783905 17.825001
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 343.284393 7.000000
      vertex 41.200001 337.884399 11.250000
      vertex 41.200001 337.858826 11.055885
    endloop
  endfacet
  facet normal 1.000000 -0.000000 0.000000
    outer loop
      vertex 41.200001 337.783905 10.875000
      vertex 41.200001 343.284393 7.000000
      vertex 41.200001 337.858826 11.055885
    endloop
  endfacet
  facet normal 1.000000 -0.000000 0.000000
    outer loop
      vertex 41.200001 337.664734 10.719670
      vertex 41.200001 343.284393 7.000000
      vertex 41.200001 337.783905 10.875000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 343.284393 7.000000
      vertex 41.200001 337.664734 10.719670
      vertex 41.200001 337.509399 10.600481
    endloop
  endfacet
  facet normal 1.000000 -0.000000 0.000000
    outer loop
      vertex 41.200001 337.328522 10.525556
      vertex 41.200001 343.284393 7.000000
      vertex 41.200001 337.509399 10.600481
    endloop
  endfacet
  facet normal 1.000000 -0.000000 0.000000
    outer loop
      vertex 41.200001 337.134399 10.500000
      vertex 41.200001 343.284393 7.000000
      vertex 41.200001 337.328522 10.525556
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 343.284393 7.000000
      vertex 41.200001 337.134399 10.500000
      vertex 41.200001 327.134399 10.500000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 41.200001 326.940277 10.525556
      vertex 41.200001 343.284393 7.000000
      vertex 41.200001 327.134399 10.500000
    endloop
  endfacet
  facet normal -0.991445 -0.130528 0.000000
    outer loop
      vertex 36.416000 329.282013 7.000000
      vertex 36.600002 327.884399 7.000000
      vertex 36.600002 327.884399 8.600000
    endloop
  endfacet
  facet normal -0.991445 -0.130528 -0.000000
    outer loop
      vertex 36.416000 329.282013 8.600000
      vertex 36.416000 329.282013 7.000000
      vertex 36.600002 327.884399 8.600000
    endloop
  endfacet
  facet normal -0.923878 -0.382686 0.000000
    outer loop
      vertex 35.876537 330.584381 7.000000
      vertex 36.416000 329.282013 7.000000
      vertex 36.416000 329.282013 8.600000
    endloop
  endfacet
  facet normal -0.923878 -0.382686 -0.000000
    outer loop
      vertex 35.876537 330.584381 8.600000
      vertex 35.876537 330.584381 7.000000
      vertex 36.416000 329.282013 8.600000
    endloop
  endfacet
  facet normal -0.793354 -0.608760 0.000000
    outer loop
      vertex 35.018379 331.702759 7.000000
      vertex 35.876537 330.584381 7.000000
      vertex 35.876537 330.584381 8.600000
    endloop
  endfacet
  facet normal -0.793354 -0.608760 -0.000000
    outer loop
      vertex 35.018379 331.702759 8.600000
      vertex 35.018379 331.702759 7.000000
      vertex 35.876537 330.584381 8.600000
    endloop
  endfacet
  facet normal -0.608772 -0.793345 0.000000
    outer loop
      vertex 33.900002 332.560944 7.000000
      vertex 35.018379 331.702759 7.000000
      vertex 35.018379 331.702759 8.600000
    endloop
  endfacet
  facet normal -0.608772 -0.793345 -0.000000
    outer loop
      vertex 33.900002 332.560944 8.600000
      vertex 33.900002 332.560944 7.000000
      vertex 35.018379 331.702759 8.600000
    endloop
  endfacet
  facet normal -0.382682 -0.923880 0.000000
    outer loop
      vertex 32.597626 333.100403 7.000000
      vertex 33.900002 332.560944 7.000000
      vertex 33.900002 332.560944 8.600000
    endloop
  endfacet
  facet normal -0.382682 -0.923880 -0.000000
    outer loop
      vertex 32.597626 333.100403 8.600000
      vertex 32.597626 333.100403 7.000000
      vertex 33.900002 332.560944 8.600000
    endloop
  endfacet
  facet normal -0.130519 -0.991446 0.000000
    outer loop
      vertex 31.200001 333.284393 7.000000
      vertex 32.597626 333.100403 7.000000
      vertex 32.597626 333.100403 8.600000
    endloop
  endfacet
  facet normal -0.130519 -0.991446 -0.000000
    outer loop
      vertex 31.200001 333.284393 8.600000
      vertex 31.200001 333.284393 7.000000
      vertex 32.597626 333.100403 8.600000
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 10.000001 333.284393 7.000000
      vertex 31.200001 333.284393 7.000000
      vertex 31.200001 333.284393 8.600000
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 10.000001 333.284393 8.600000
      vertex 10.000001 333.284393 7.000000
      vertex 31.200001 333.284393 8.600000
    endloop
  endfacet
  facet normal -0.130519 0.991446 0.000000
    outer loop
      vertex 32.597626 287.668396 7.000000
      vertex 31.200001 287.484406 7.000000
      vertex 31.200001 287.484406 8.600000
    endloop
  endfacet
  facet normal -0.130519 0.991446 0.000000
    outer loop
      vertex 32.597626 287.668396 8.600000
      vertex 32.597626 287.668396 7.000000
      vertex 31.200001 287.484406 8.600000
    endloop
  endfacet
  facet normal -0.382682 0.923880 0.000000
    outer loop
      vertex 33.900002 288.207855 7.000000
      vertex 32.597626 287.668396 7.000000
      vertex 32.597626 287.668396 8.600000
    endloop
  endfacet
  facet normal -0.382682 0.923880 0.000000
    outer loop
      vertex 33.900002 288.207855 8.600000
      vertex 33.900002 288.207855 7.000000
      vertex 32.597626 287.668396 8.600000
    endloop
  endfacet
  facet normal -0.608758 0.793356 0.000000
    outer loop
      vertex 35.018379 289.066010 7.000000
      vertex 33.900002 288.207855 7.000000
      vertex 33.900002 288.207855 8.600000
    endloop
  endfacet
  facet normal -0.608758 0.793356 0.000000
    outer loop
      vertex 35.018379 289.066010 8.600000
      vertex 35.018379 289.066010 7.000000
      vertex 33.900002 288.207855 8.600000
    endloop
  endfacet
  facet normal -0.793354 0.608760 0.000000
    outer loop
      vertex 35.876537 290.184387 7.000000
      vertex 35.018379 289.066010 7.000000
      vertex 35.018379 289.066010 8.600000
    endloop
  endfacet
  facet normal -0.793354 0.608760 0.000000
    outer loop
      vertex 35.876537 290.184387 8.600000
      vertex 35.876537 290.184387 7.000000
      vertex 35.018379 289.066010 8.600000
    endloop
  endfacet
  facet normal -0.923882 0.382678 0.000000
    outer loop
      vertex 36.416000 291.486786 7.000000
      vertex 35.876537 290.184387 7.000000
      vertex 35.876537 290.184387 8.600000
    endloop
  endfacet
  facet normal -0.923882 0.382678 0.000000
    outer loop
      vertex 36.416000 291.486786 8.600000
      vertex 36.416000 291.486786 7.000000
      vertex 35.876537 290.184387 8.600000
    endloop
  endfacet
  facet normal -0.991445 0.130528 0.000000
    outer loop
      vertex 36.600002 292.884399 7.000000
      vertex 36.416000 291.486786 7.000000
      vertex 36.416000 291.486786 8.600000
    endloop
  endfacet
  facet normal -0.991445 0.130528 0.000000
    outer loop
      vertex 36.600002 292.884399 8.600000
      vertex 36.600002 292.884399 7.000000
      vertex 36.416000 291.486786 8.600000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 36.600002 292.884399 8.600000
      vertex 36.600002 327.884399 8.600000
      vertex 36.600002 327.884399 7.000000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 36.600002 292.884399 7.000000
      vertex 36.600002 292.884399 8.600000
      vertex 36.600002 327.884399 7.000000
    endloop
  endfacet
  facet normal 0.991445 0.130527 0.000000
    outer loop
      vertex 4.784001 291.486786 7.000000
      vertex 4.600001 292.884399 7.000000
      vertex 4.600001 292.884399 8.600000
    endloop
  endfacet
  facet normal 0.991445 0.130527 0.000000
    outer loop
      vertex 4.784001 291.486786 8.600000
      vertex 4.784001 291.486786 7.000000
      vertex 4.600001 292.884399 8.600000
    endloop
  endfacet
  facet normal 0.923882 0.382678 0.000000
    outer loop
      vertex 5.323464 290.184387 7.000000
      vertex 4.784001 291.486786 7.000000
      vertex 4.784001 291.486786 8.600000
    endloop
  endfacet
  facet normal 0.923882 0.382678 0.000000
    outer loop
      vertex 5.323464 290.184387 8.600000
      vertex 5.323464 290.184387 7.000000
      vertex 4.784001 291.486786 8.600000
    endloop
  endfacet
  facet normal 0.793354 0.608761 0.000000
    outer loop
      vertex 6.181624 289.066010 7.000000
      vertex 5.323464 290.184387 7.000000
      vertex 5.323464 290.184387 8.600000
    endloop
  endfacet
  facet normal 0.793354 0.608761 0.000000
    outer loop
      vertex 6.181624 289.066010 8.600000
      vertex 6.181624 289.066010 7.000000
      vertex 5.323464 290.184387 8.600000
    endloop
  endfacet
  facet normal 0.608759 0.793356 0.000000
    outer loop
      vertex 7.300001 288.207855 7.000000
      vertex 6.181624 289.066010 7.000000
      vertex 6.181624 289.066010 8.600000
    endloop
  endfacet
  facet normal 0.608759 0.793356 0.000000
    outer loop
      vertex 7.300001 288.207855 8.600000
      vertex 7.300001 288.207855 7.000000
      vertex 6.181624 289.066010 8.600000
    endloop
  endfacet
  facet normal 0.382682 0.923880 0.000000
    outer loop
      vertex 8.602378 287.668396 7.000000
      vertex 7.300001 288.207855 7.000000
      vertex 7.300001 288.207855 8.600000
    endloop
  endfacet
  facet normal 0.382682 0.923880 0.000000
    outer loop
      vertex 8.602378 287.668396 8.600000
      vertex 8.602378 287.668396 7.000000
      vertex 7.300001 288.207855 8.600000
    endloop
  endfacet
  facet normal 0.130519 0.991446 0.000000
    outer loop
      vertex 10.000001 287.484406 7.000000
      vertex 8.602378 287.668396 7.000000
      vertex 8.602378 287.668396 8.600000
    endloop
  endfacet
  facet normal 0.130519 0.991446 0.000000
    outer loop
      vertex 10.000001 287.484406 8.600000
      vertex 10.000001 287.484406 7.000000
      vertex 8.602378 287.668396 8.600000
    endloop
  endfacet
  facet normal -0.000000 1.000000 0.000000
    outer loop
      vertex 10.000001 287.484406 8.600000
      vertex 31.200001 287.484406 8.600000
      vertex 31.200001 287.484406 7.000000
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 10.000001 287.484406 7.000000
      vertex 10.000001 287.484406 8.600000
      vertex 31.200001 287.484406 7.000000
    endloop
  endfacet
  facet normal 0.130519 -0.991446 0.000000
    outer loop
      vertex 8.602378 333.100403 7.000000
      vertex 10.000001 333.284393 7.000000
      vertex 10.000001 333.284393 8.600000
    endloop
  endfacet
  facet normal 0.130519 -0.991446 0.000000
    outer loop
      vertex 8.602378 333.100403 8.600000
      vertex 8.602378 333.100403 7.000000
      vertex 10.000001 333.284393 8.600000
    endloop
  endfacet
  facet normal 0.382682 -0.923880 0.000000
    outer loop
      vertex 7.300001 332.560944 7.000000
      vertex 8.602378 333.100403 7.000000
      vertex 8.602378 333.100403 8.600000
    endloop
  endfacet
  facet normal 0.382682 -0.923880 0.000000
    outer loop
      vertex 7.300001 332.560944 8.600000
      vertex 7.300001 332.560944 7.000000
      vertex 8.602378 333.100403 8.600000
    endloop
  endfacet
  facet normal 0.608772 -0.793345 0.000000
    outer loop
      vertex 6.181624 331.702759 7.000000
      vertex 7.300001 332.560944 7.000000
      vertex 7.300001 332.560944 8.600000
    endloop
  endfacet
  facet normal 0.608772 -0.793345 0.000000
    outer loop
      vertex 6.181624 331.702759 8.600000
      vertex 6.181624 331.702759 7.000000
      vertex 7.300001 332.560944 8.600000
    endloop
  endfacet
  facet normal 0.793354 -0.608761 0.000000
    outer loop
      vertex 5.323464 330.584381 7.000000
      vertex 6.181624 331.702759 7.000000
      vertex 6.181624 331.702759 8.600000
    endloop
  endfacet
  facet normal 0.793354 -0.608761 0.000000
    outer loop
      vertex 5.323464 330.584381 8.600000
      vertex 5.323464 330.584381 7.000000
      vertex 6.181624 331.702759 8.600000
    endloop
  endfacet
  facet normal 0.923879 -0.382686 0.000000
    outer loop
      vertex 4.784001 329.282013 7.000000
      vertex 5.323464 330.584381 7.000000
      vertex 5.323464 330.584381 8.600000
    endloop
  endfacet
  facet normal 0.923879 -0.382686 0.000000
    outer loop
      vertex 4.784001 329.282013 8.600000
      vertex 4.784001 329.282013 7.000000
      vertex 5.323464 330.584381 8.600000
    endloop
  endfacet
  facet normal 0.991445 -0.130527 0.000000
    outer loop
      vertex 4.600001 327.884399 7.000000
      vertex 4.784001 329.282013 7.000000
      vertex 4.784001 329.282013 8.600000
    endloop
  endfacet
  facet normal 0.991445 -0.130527 0.000000
    outer loop
      vertex 4.600001 327.884399 8.600000
      vertex 4.600001 327.884399 7.000000
      vertex 4.784001 329.282013 8.600000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 4.600001 327.884399 8.600000
      vertex 4.600001 292.884399 8.600000
      vertex 4.600001 292.884399 7.000000
    endloop
  endfacet
  facet normal 1.000000 0.000000 -0.000000
    outer loop
      vertex 4.600001 327.884399 7.000000
      vertex 4.600001 327.884399 8.600000
      vertex 4.600001 292.884399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.991446 0.130519
    outer loop
      vertex 39.600002 287.668396 15.602377
      vertex 39.600002 287.484406 17.000000
      vertex 41.200001 287.484406 17.000000
    endloop
  endfacet
  facet normal 0.000000 0.991446 0.130519
    outer loop
      vertex 41.200001 287.668396 15.602377
      vertex 39.600002 287.668396 15.602377
      vertex 41.200001 287.484406 17.000000
    endloop
  endfacet
  facet normal 0.000000 0.923880 0.382682
    outer loop
      vertex 39.600002 288.207855 14.300000
      vertex 39.600002 287.668396 15.602377
      vertex 41.200001 287.668396 15.602377
    endloop
  endfacet
  facet normal 0.000000 0.923880 0.382682
    outer loop
      vertex 41.200001 288.207855 14.300000
      vertex 39.600002 288.207855 14.300000
      vertex 41.200001 287.668396 15.602377
    endloop
  endfacet
  facet normal 0.000000 0.793355 0.608759
    outer loop
      vertex 39.600002 289.066010 13.181623
      vertex 39.600002 288.207855 14.300000
      vertex 41.200001 288.207855 14.300000
    endloop
  endfacet
  facet normal 0.000000 0.793355 0.608759
    outer loop
      vertex 41.200001 289.066010 13.181623
      vertex 39.600002 289.066010 13.181623
      vertex 41.200001 288.207855 14.300000
    endloop
  endfacet
  facet normal 0.000000 0.608761 0.793353
    outer loop
      vertex 39.600002 290.184387 12.323462
      vertex 39.600002 289.066010 13.181623
      vertex 41.200001 289.066010 13.181623
    endloop
  endfacet
  facet normal 0.000000 0.608761 0.793353
    outer loop
      vertex 41.200001 290.184387 12.323462
      vertex 39.600002 290.184387 12.323462
      vertex 41.200001 289.066010 13.181623
    endloop
  endfacet
  facet normal 0.000000 0.382678 0.923882
    outer loop
      vertex 39.600002 291.486786 11.784000
      vertex 39.600002 290.184387 12.323462
      vertex 41.200001 290.184387 12.323462
    endloop
  endfacet
  facet normal 0.000000 0.382678 0.923882
    outer loop
      vertex 41.200001 291.486786 11.784000
      vertex 39.600002 291.486786 11.784000
      vertex 41.200001 290.184387 12.323462
    endloop
  endfacet
  facet normal 0.000000 0.130527 0.991445
    outer loop
      vertex 39.600002 292.884399 11.600000
      vertex 39.600002 291.486786 11.784000
      vertex 41.200001 291.486786 11.784000
    endloop
  endfacet
  facet normal 0.000000 0.130527 0.991445
    outer loop
      vertex 41.200001 292.884399 11.600000
      vertex 39.600002 292.884399 11.600000
      vertex 41.200001 291.486786 11.784000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 39.600002 304.984406 11.600000
      vertex 39.600002 292.884399 11.600000
      vertex 41.200001 292.884399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 41.200001 304.984406 11.600000
      vertex 39.600002 304.984406 11.600000
      vertex 41.200001 292.884399 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.991446 0.130519
    outer loop
      vertex 41.200001 310.200409 15.602377
      vertex 41.200001 310.384399 17.000000
      vertex 39.600002 310.384399 17.000000
    endloop
  endfacet
  facet normal 0.000000 -0.991446 0.130519
    outer loop
      vertex 39.600002 310.200409 15.602377
      vertex 41.200001 310.200409 15.602377
      vertex 39.600002 310.384399 17.000000
    endloop
  endfacet
  facet normal 0.000000 -0.923873 0.382700
    outer loop
      vertex 41.200001 309.660919 14.300000
      vertex 41.200001 310.200409 15.602377
      vertex 39.600002 310.200409 15.602377
    endloop
  endfacet
  facet normal 0.000000 -0.923873 0.382700
    outer loop
      vertex 39.600002 309.660919 14.300000
      vertex 41.200001 309.660919 14.300000
      vertex 39.600002 310.200409 15.602377
    endloop
  endfacet
  facet normal 0.000000 -0.793355 0.608759
    outer loop
      vertex 41.200001 308.802765 13.181623
      vertex 41.200001 309.660919 14.300000
      vertex 39.600002 309.660919 14.300000
    endloop
  endfacet
  facet normal 0.000000 -0.793355 0.608759
    outer loop
      vertex 39.600002 308.802765 13.181623
      vertex 41.200001 308.802765 13.181623
      vertex 39.600002 309.660919 14.300000
    endloop
  endfacet
  facet normal 0.000000 -0.608761 0.793353
    outer loop
      vertex 41.200001 307.684387 12.323462
      vertex 41.200001 308.802765 13.181623
      vertex 39.600002 308.802765 13.181623
    endloop
  endfacet
  facet normal 0.000000 -0.608761 0.793353
    outer loop
      vertex 39.600002 307.684387 12.323462
      vertex 41.200001 307.684387 12.323462
      vertex 39.600002 308.802765 13.181623
    endloop
  endfacet
  facet normal 0.000000 -0.382686 0.923879
    outer loop
      vertex 41.200001 306.382019 11.784000
      vertex 41.200001 307.684387 12.323462
      vertex 39.600002 307.684387 12.323462
    endloop
  endfacet
  facet normal 0.000000 -0.382686 0.923879
    outer loop
      vertex 39.600002 306.382019 11.784000
      vertex 41.200001 306.382019 11.784000
      vertex 39.600002 307.684387 12.323462
    endloop
  endfacet
  facet normal 0.000000 -0.130527 0.991445
    outer loop
      vertex 41.200001 304.984406 11.600000
      vertex 41.200001 306.382019 11.784000
      vertex 39.600002 306.382019 11.784000
    endloop
  endfacet
  facet normal 0.000000 -0.130527 0.991445
    outer loop
      vertex 39.600002 304.984406 11.600000
      vertex 41.200001 304.984406 11.600000
      vertex 39.600002 306.382019 11.784000
    endloop
  endfacet
  facet normal 0.000000 -0.991446 -0.130519
    outer loop
      vertex 39.600002 310.200409 26.597622
      vertex 39.600002 310.384399 25.200001
      vertex 41.200001 310.384399 25.200001
    endloop
  endfacet
  facet normal -0.000000 -0.991446 -0.130519
    outer loop
      vertex 41.200001 310.200409 26.597622
      vertex 39.600002 310.200409 26.597622
      vertex 41.200001 310.384399 25.200001
    endloop
  endfacet
  facet normal 0.000000 -0.923873 -0.382700
    outer loop
      vertex 39.600002 309.660919 27.900000
      vertex 39.600002 310.200409 26.597622
      vertex 41.200001 310.200409 26.597622
    endloop
  endfacet
  facet normal -0.000000 -0.923873 -0.382700
    outer loop
      vertex 41.200001 309.660919 27.900000
      vertex 39.600002 309.660919 27.900000
      vertex 41.200001 310.200409 26.597622
    endloop
  endfacet
  facet normal 0.000000 -0.793356 -0.608758
    outer loop
      vertex 39.600002 308.802765 29.018377
      vertex 39.600002 309.660919 27.900000
      vertex 41.200001 309.660919 27.900000
    endloop
  endfacet
  facet normal -0.000000 -0.793356 -0.608758
    outer loop
      vertex 41.200001 308.802765 29.018377
      vertex 39.600002 308.802765 29.018377
      vertex 41.200001 309.660919 27.900000
    endloop
  endfacet
  facet normal 0.000000 -0.608761 -0.793354
    outer loop
      vertex 39.600002 307.684387 29.876537
      vertex 39.600002 308.802765 29.018377
      vertex 41.200001 308.802765 29.018377
    endloop
  endfacet
  facet normal -0.000000 -0.608761 -0.793354
    outer loop
      vertex 41.200001 307.684387 29.876537
      vertex 39.600002 307.684387 29.876537
      vertex 41.200001 308.802765 29.018377
    endloop
  endfacet
  facet normal 0.000000 -0.382686 -0.923878
    outer loop
      vertex 39.600002 306.382019 30.416000
      vertex 39.600002 307.684387 29.876537
      vertex 41.200001 307.684387 29.876537
    endloop
  endfacet
  facet normal -0.000000 -0.382686 -0.923878
    outer loop
      vertex 41.200001 306.382019 30.416000
      vertex 39.600002 306.382019 30.416000
      vertex 41.200001 307.684387 29.876537
    endloop
  endfacet
  facet normal 0.000000 -0.130527 -0.991445
    outer loop
      vertex 39.600002 304.984406 30.600000
      vertex 39.600002 306.382019 30.416000
      vertex 41.200001 306.382019 30.416000
    endloop
  endfacet
  facet normal -0.000000 -0.130527 -0.991445
    outer loop
      vertex 41.200001 304.984406 30.600000
      vertex 39.600002 304.984406 30.600000
      vertex 41.200001 306.382019 30.416000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 39.600002 292.884399 30.600000
      vertex 39.600002 304.984406 30.600000
      vertex 41.200001 304.984406 30.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 41.200001 292.884399 30.600000
      vertex 39.600002 292.884399 30.600000
      vertex 41.200001 304.984406 30.600000
    endloop
  endfacet
  facet normal 0.000000 0.991446 -0.130519
    outer loop
      vertex 41.200001 287.668396 26.597622
      vertex 41.200001 287.484406 25.200001
      vertex 39.600002 287.484406 25.200001
    endloop
  endfacet
  facet normal 0.000000 0.991446 -0.130519
    outer loop
      vertex 39.600002 287.668396 26.597622
      vertex 41.200001 287.668396 26.597622
      vertex 39.600002 287.484406 25.200001
    endloop
  endfacet
  facet normal 0.000000 0.923880 -0.382681
    outer loop
      vertex 41.200001 288.207855 27.900000
      vertex 41.200001 287.668396 26.597622
      vertex 39.600002 287.668396 26.597622
    endloop
  endfacet
  facet normal 0.000000 0.923880 -0.382681
    outer loop
      vertex 39.600002 288.207855 27.900000
      vertex 41.200001 288.207855 27.900000
      vertex 39.600002 287.668396 26.597622
    endloop
  endfacet
  facet normal 0.000000 0.793356 -0.608758
    outer loop
      vertex 41.200001 289.066010 29.018377
      vertex 41.200001 288.207855 27.900000
      vertex 39.600002 288.207855 27.900000
    endloop
  endfacet
  facet normal 0.000000 0.793356 -0.608758
    outer loop
      vertex 39.600002 289.066010 29.018377
      vertex 41.200001 289.066010 29.018377
      vertex 39.600002 288.207855 27.900000
    endloop
  endfacet
  facet normal 0.000000 0.608761 -0.793354
    outer loop
      vertex 41.200001 290.184387 29.876537
      vertex 41.200001 289.066010 29.018377
      vertex 39.600002 289.066010 29.018377
    endloop
  endfacet
  facet normal 0.000000 0.608761 -0.793354
    outer loop
      vertex 39.600002 290.184387 29.876537
      vertex 41.200001 290.184387 29.876537
      vertex 39.600002 289.066010 29.018377
    endloop
  endfacet
  facet normal 0.000000 0.382679 -0.923882
    outer loop
      vertex 41.200001 291.486786 30.416000
      vertex 41.200001 290.184387 29.876537
      vertex 39.600002 290.184387 29.876537
    endloop
  endfacet
  facet normal 0.000000 0.382679 -0.923882
    outer loop
      vertex 39.600002 291.486786 30.416000
      vertex 41.200001 291.486786 30.416000
      vertex 39.600002 290.184387 29.876537
    endloop
  endfacet
  facet normal 0.000000 0.130527 -0.991445
    outer loop
      vertex 41.200001 292.884399 30.600000
      vertex 41.200001 291.486786 30.416000
      vertex 39.600002 291.486786 30.416000
    endloop
  endfacet
  facet normal 0.000000 0.130527 -0.991445
    outer loop
      vertex 39.600002 292.884399 30.600000
      vertex 41.200001 292.884399 30.600000
      vertex 39.600002 291.486786 30.416000
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 39.600002 310.384399 17.000000
      vertex 41.200001 310.384399 17.000000
      vertex 41.200001 310.384399 25.200001
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 39.600002 310.384399 25.200001
      vertex 39.600002 310.384399 17.000000
      vertex 41.200001 310.384399 25.200001
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 41.200001 287.484406 17.000000
      vertex 39.600002 287.484406 17.000000
      vertex 39.600002 287.484406 25.200001
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 41.200001 287.484406 25.200001
      vertex 41.200001 287.484406 17.000000
      vertex 39.600002 287.484406 25.200001
    endloop
  endfacet
  facet normal 0.000000 0.991446 0.130519
    outer loop
      vertex 0.000001 287.668396 15.602377
      vertex 0.000001 287.484406 17.000000
      vertex 1.100001 287.484406 17.000000
    endloop
  endfacet
  facet normal 0.000000 0.991446 0.130519
    outer loop
      vertex 1.100001 287.668396 15.602377
      vertex 0.000001 287.668396 15.602377
      vertex 1.100001 287.484406 17.000000
    endloop
  endfacet
  facet normal 0.000000 0.923880 0.382682
    outer loop
      vertex 0.000001 288.207855 14.300000
      vertex 0.000001 287.668396 15.602377
      vertex 1.100001 287.668396 15.602377
    endloop
  endfacet
  facet normal 0.000000 0.923880 0.382682
    outer loop
      vertex 1.100001 288.207855 14.300000
      vertex 0.000001 288.207855 14.300000
      vertex 1.100001 287.668396 15.602377
    endloop
  endfacet
  facet normal 0.000000 0.793356 0.608759
    outer loop
      vertex 0.000001 289.066010 13.181623
      vertex 0.000001 288.207855 14.300000
      vertex 1.100001 288.207855 14.300000
    endloop
  endfacet
  facet normal 0.000000 0.793356 0.608759
    outer loop
      vertex 1.100001 289.066010 13.181623
      vertex 0.000001 289.066010 13.181623
      vertex 1.100001 288.207855 14.300000
    endloop
  endfacet
  facet normal 0.000000 0.608761 0.793353
    outer loop
      vertex 0.000001 290.184387 12.323462
      vertex 0.000001 289.066010 13.181623
      vertex 1.100001 289.066010 13.181623
    endloop
  endfacet
  facet normal 0.000000 0.608761 0.793353
    outer loop
      vertex 1.100001 290.184387 12.323462
      vertex 0.000001 290.184387 12.323462
      vertex 1.100001 289.066010 13.181623
    endloop
  endfacet
  facet normal 0.000000 0.382678 0.923882
    outer loop
      vertex 0.000001 291.486786 11.784000
      vertex 0.000001 290.184387 12.323462
      vertex 1.100001 290.184387 12.323462
    endloop
  endfacet
  facet normal 0.000000 0.382678 0.923882
    outer loop
      vertex 1.100001 291.486786 11.784000
      vertex 0.000001 291.486786 11.784000
      vertex 1.100001 290.184387 12.323462
    endloop
  endfacet
  facet normal 0.000000 0.130527 0.991445
    outer loop
      vertex 0.000001 292.884399 11.600000
      vertex 0.000001 291.486786 11.784000
      vertex 1.100001 291.486786 11.784000
    endloop
  endfacet
  facet normal 0.000000 0.130527 0.991445
    outer loop
      vertex 1.100001 292.884399 11.600000
      vertex 0.000001 292.884399 11.600000
      vertex 1.100001 291.486786 11.784000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 1.100001 292.884399 11.600000
      vertex 1.100001 307.884399 11.600000
      vertex 0.000001 307.884399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 0.000001 292.884399 11.600000
      vertex 1.100001 292.884399 11.600000
      vertex 0.000001 307.884399 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.991446 -0.130519
    outer loop
      vertex 0.000001 333.100403 26.597622
      vertex 0.000001 333.284393 25.200001
      vertex 1.100001 333.284393 25.200001
    endloop
  endfacet
  facet normal -0.000000 -0.991446 -0.130519
    outer loop
      vertex 1.100001 333.100403 26.597622
      vertex 0.000001 333.100403 26.597622
      vertex 1.100001 333.284393 25.200001
    endloop
  endfacet
  facet normal 0.000000 -0.923880 -0.382681
    outer loop
      vertex 0.000001 332.560944 27.900000
      vertex 0.000001 333.100403 26.597622
      vertex 1.100001 333.100403 26.597622
    endloop
  endfacet
  facet normal -0.000000 -0.923880 -0.382681
    outer loop
      vertex 1.100001 332.560944 27.900000
      vertex 0.000001 332.560944 27.900000
      vertex 1.100001 333.100403 26.597622
    endloop
  endfacet
  facet normal 0.000000 -0.793345 -0.608772
    outer loop
      vertex 0.000001 331.702759 29.018377
      vertex 0.000001 332.560944 27.900000
      vertex 1.100001 332.560944 27.900000
    endloop
  endfacet
  facet normal -0.000000 -0.793345 -0.608772
    outer loop
      vertex 1.100001 331.702759 29.018377
      vertex 0.000001 331.702759 29.018377
      vertex 1.100001 332.560944 27.900000
    endloop
  endfacet
  facet normal 0.000000 -0.608761 -0.793354
    outer loop
      vertex 0.000001 330.584381 29.876537
      vertex 0.000001 331.702759 29.018377
      vertex 1.100001 331.702759 29.018377
    endloop
  endfacet
  facet normal -0.000000 -0.608761 -0.793354
    outer loop
      vertex 1.100001 330.584381 29.876537
      vertex 0.000001 330.584381 29.876537
      vertex 1.100001 331.702759 29.018377
    endloop
  endfacet
  facet normal 0.000000 -0.382686 -0.923878
    outer loop
      vertex 0.000001 329.282013 30.416000
      vertex 0.000001 330.584381 29.876537
      vertex 1.100001 330.584381 29.876537
    endloop
  endfacet
  facet normal -0.000000 -0.382686 -0.923878
    outer loop
      vertex 1.100001 329.282013 30.416000
      vertex 0.000001 329.282013 30.416000
      vertex 1.100001 330.584381 29.876537
    endloop
  endfacet
  facet normal 0.000000 -0.130527 -0.991445
    outer loop
      vertex 0.000001 327.884399 30.600000
      vertex 0.000001 329.282013 30.416000
      vertex 1.100001 329.282013 30.416000
    endloop
  endfacet
  facet normal -0.000000 -0.130527 -0.991445
    outer loop
      vertex 1.100001 327.884399 30.600000
      vertex 0.000001 327.884399 30.600000
      vertex 1.100001 329.282013 30.416000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 1.100001 327.884399 30.600000
      vertex 1.100001 312.884399 30.600000
      vertex 0.000001 312.884399 30.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 0.000001 327.884399 30.600000
      vertex 1.100001 327.884399 30.600000
      vertex 0.000001 312.884399 30.600000
    endloop
  endfacet
  facet normal -0.130528 0.991445 0.000000
    outer loop
      vertex 2.371780 346.375366 33.599998
      vertex 3.200001 346.484406 33.599998
      vertex 3.200001 346.484406 7.000000
    endloop
  endfacet
  facet normal -0.130528 0.991445 0.000000
    outer loop
      vertex 2.371780 346.375366 7.000000
      vertex 2.371780 346.375366 33.599998
      vertex 3.200001 346.484406 7.000000
    endloop
  endfacet
  facet normal -0.382705 0.923871 0.000000
    outer loop
      vertex 1.600001 346.055664 33.599998
      vertex 2.371780 346.375366 33.599998
      vertex 2.371780 346.375366 7.000000
    endloop
  endfacet
  facet normal -0.382705 0.923871 0.000000
    outer loop
      vertex 1.600001 346.055664 7.000000
      vertex 1.600001 346.055664 33.599998
      vertex 2.371780 346.375366 7.000000
    endloop
  endfacet
  facet normal -0.608742 0.793368 0.000000
    outer loop
      vertex 0.937259 345.547150 33.599998
      vertex 1.600001 346.055664 33.599998
      vertex 1.600001 346.055664 7.000000
    endloop
  endfacet
  facet normal -0.608742 0.793368 0.000000
    outer loop
      vertex 0.937259 345.547150 7.000000
      vertex 0.937259 345.547150 33.599998
      vertex 1.600001 346.055664 7.000000
    endloop
  endfacet
  facet normal -0.793357 0.608756 0.000000
    outer loop
      vertex 0.428720 344.884399 33.599998
      vertex 0.937259 345.547150 33.599998
      vertex 0.937259 345.547150 7.000000
    endloop
  endfacet
  facet normal -0.793357 0.608756 0.000000
    outer loop
      vertex 0.428720 344.884399 7.000000
      vertex 0.428720 344.884399 33.599998
      vertex 0.937259 345.547150 7.000000
    endloop
  endfacet
  facet normal -0.923881 0.382679 0.000000
    outer loop
      vertex 0.109038 344.112610 33.599998
      vertex 0.428720 344.884399 33.599998
      vertex 0.428720 344.884399 7.000000
    endloop
  endfacet
  facet normal -0.923881 0.382679 0.000000
    outer loop
      vertex 0.109038 344.112610 7.000000
      vertex 0.109038 344.112610 33.599998
      vertex 0.428720 344.884399 7.000000
    endloop
  endfacet
  facet normal -0.991445 0.130527 0.000000
    outer loop
      vertex 0.000001 343.284393 33.599998
      vertex 0.109038 344.112610 33.599998
      vertex 0.109038 344.112610 7.000000
    endloop
  endfacet
  facet normal -0.991445 0.130527 0.000000
    outer loop
      vertex 0.000001 343.284393 7.000000
      vertex 0.000001 343.284393 33.599998
      vertex 0.109038 344.112610 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 10.000001 287.484406 7.000000
      vertex 7.773334 280.802063 7.000000
      vertex 7.850001 281.384399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 7.773334 281.966736 7.000000
      vertex 10.000001 287.484406 7.000000
      vertex 7.850001 281.384399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 7.548558 282.509399 7.000000
      vertex 10.000001 287.484406 7.000000
      vertex 7.773334 281.966736 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 8.602378 287.668396 7.000000
      vertex 10.000001 287.484406 7.000000
      vertex 7.548558 282.509399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 7.190991 282.975372 7.000000
      vertex 8.602378 287.668396 7.000000
      vertex 7.548558 282.509399 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 7.300001 288.207855 7.000000
      vertex 8.602378 287.668396 7.000000
      vertex 7.190991 282.975372 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 6.725001 283.332947 7.000000
      vertex 7.300001 288.207855 7.000000
      vertex 7.190991 282.975372 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 6.182344 283.557739 7.000000
      vertex 7.300001 288.207855 7.000000
      vertex 6.725001 283.332947 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 6.181624 289.066010 7.000000
      vertex 7.300001 288.207855 7.000000
      vertex 6.182344 283.557739 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 5.600001 283.634399 7.000000
      vertex 6.181624 289.066010 7.000000
      vertex 6.182344 283.557739 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 5.017658 283.557739 7.000000
      vertex 6.181624 289.066010 7.000000
      vertex 5.600001 283.634399 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 5.323464 290.184387 7.000000
      vertex 6.181624 289.066010 7.000000
      vertex 5.017658 283.557739 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 4.475001 283.332947 7.000000
      vertex 5.323464 290.184387 7.000000
      vertex 5.017658 283.557739 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 4.009011 282.975372 7.000000
      vertex 5.323464 290.184387 7.000000
      vertex 4.475001 283.332947 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 4.784001 291.486786 7.000000
      vertex 5.323464 290.184387 7.000000
      vertex 4.009011 282.975372 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 3.651444 282.509399 7.000000
      vertex 4.784001 291.486786 7.000000
      vertex 4.009011 282.975372 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 4.600001 292.884399 7.000000
      vertex 4.784001 291.486786 7.000000
      vertex 3.651444 282.509399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 3.426668 281.966736 7.000000
      vertex 4.600001 292.884399 7.000000
      vertex 3.651444 282.509399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 0.000001 276.484406 7.000000
      vertex 4.600001 292.884399 7.000000
      vertex 3.426668 281.966736 7.000000
    endloop
  endfacet
  facet normal -0.000000 0.000000 -1.000000
    outer loop
      vertex 3.350001 281.384399 7.000000
      vertex 0.000001 276.484406 7.000000
      vertex 3.426668 281.966736 7.000000
    endloop
  endfacet
  facet normal -0.000000 0.000000 -1.000000
    outer loop
      vertex 3.426668 280.802063 7.000000
      vertex 0.000001 276.484406 7.000000
      vertex 3.350001 281.384399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 0.000001 276.484406 7.000000
      vertex 3.426668 280.802063 7.000000
      vertex 3.651444 280.259399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 0.937259 274.221649 7.000000
      vertex 0.000001 276.484406 7.000000
      vertex 3.651444 280.259399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 0.428720 274.884399 7.000000
      vertex 0.000001 276.484406 7.000000
      vertex 0.937259 274.221649 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 3.651444 280.259399 7.000000
      vertex 4.009011 279.793396 7.000000
      vertex 2.371780 273.393433 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 1.600001 273.713104 7.000000
      vertex 3.651444 280.259399 7.000000
      vertex 2.371780 273.393433 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 0.937259 274.221649 7.000000
      vertex 3.651444 280.259399 7.000000
      vertex 1.600001 273.713104 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 3.200001 273.284393 7.000000
      vertex 2.371780 273.393433 7.000000
      vertex 4.009011 279.793396 7.000000
    endloop
  endfacet
  facet normal -0.000000 0.000000 -1.000000
    outer loop
      vertex 4.475001 279.435852 7.000000
      vertex 3.200001 273.284393 7.000000
      vertex 4.009011 279.793396 7.000000
    endloop
  endfacet
  facet normal -0.000000 0.000000 -1.000000
    outer loop
      vertex 5.017658 279.211060 7.000000
      vertex 3.200001 273.284393 7.000000
      vertex 4.475001 279.435852 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 3.200001 273.284393 7.000000
      vertex 5.017658 279.211060 7.000000
      vertex 5.600001 279.134399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 6.182344 279.211060 7.000000
      vertex 3.200001 273.284393 7.000000
      vertex 5.600001 279.134399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 6.725001 279.435852 7.000000
      vertex 3.200001 273.284393 7.000000
      vertex 6.182344 279.211060 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 3.200001 273.284393 7.000000
      vertex 6.725001 279.435852 7.000000
      vertex 7.190991 279.793396 7.000000
    endloop
  endfacet
  facet normal -0.000000 0.000000 -1.000000
    outer loop
      vertex 27.009010 279.793396 7.000000
      vertex 3.200001 273.284393 7.000000
      vertex 7.190991 279.793396 7.000000
    endloop
  endfacet
  facet normal -0.000000 0.000000 -1.000000
    outer loop
      vertex 27.475000 279.435852 7.000000
      vertex 3.200001 273.284393 7.000000
      vertex 27.009010 279.793396 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 26.651443 280.259399 7.000000
      vertex 27.009010 279.793396 7.000000
      vertex 7.190991 279.793396 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 7.548558 280.259399 7.000000
      vertex 26.651443 280.259399 7.000000
      vertex 7.190991 279.793396 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 26.426668 280.802063 7.000000
      vertex 26.651443 280.259399 7.000000
      vertex 7.548558 280.259399 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 7.773334 280.802063 7.000000
      vertex 26.426668 280.802063 7.000000
      vertex 7.548558 280.259399 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 10.000001 287.484406 7.000000
      vertex 26.426668 280.802063 7.000000
      vertex 7.773334 280.802063 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 10.000001 333.284393 7.000000
      vertex 7.773334 338.802063 7.000000
      vertex 7.850001 339.384399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 7.773334 339.966736 7.000000
      vertex 10.000001 333.284393 7.000000
      vertex 7.850001 339.384399 7.000000
    endloop
  endfacet
  facet normal -0.000000 0.000000 -1.000000
    outer loop
      vertex 26.426668 339.966736 7.000000
      vertex 10.000001 333.284393 7.000000
      vertex 7.773334 339.966736 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 26.651443 340.509399 7.000000
      vertex 26.426668 339.966736 7.000000
      vertex 7.773334 339.966736 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 7.548558 340.509399 7.000000
      vertex 26.651443 340.509399 7.000000
      vertex 7.773334 339.966736 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 27.009010 340.975372 7.000000
      vertex 26.651443 340.509399 7.000000
      vertex 7.548558 340.509399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 7.190991 340.975372 7.000000
      vertex 27.009010 340.975372 7.000000
      vertex 7.548558 340.509399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 3.200001 346.484406 7.000000
      vertex 27.009010 340.975372 7.000000
      vertex 7.190991 340.975372 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 6.725001 341.332947 7.000000
      vertex 3.200001 346.484406 7.000000
      vertex 7.190991 340.975372 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 6.182344 341.557739 7.000000
      vertex 3.200001 346.484406 7.000000
      vertex 6.725001 341.332947 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 3.200001 346.484406 7.000000
      vertex 6.182344 341.557739 7.000000
      vertex 5.600001 341.634399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 5.017658 341.557739 7.000000
      vertex 3.200001 346.484406 7.000000
      vertex 5.600001 341.634399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 4.475001 341.332947 7.000000
      vertex 3.200001 346.484406 7.000000
      vertex 5.017658 341.557739 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 3.200001 346.484406 7.000000
      vertex 4.475001 341.332947 7.000000
      vertex 4.009011 340.975372 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 2.371780 346.375366 7.000000
      vertex 3.200001 346.484406 7.000000
      vertex 4.009011 340.975372 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 3.651444 340.509399 7.000000
      vertex 2.371780 346.375366 7.000000
      vertex 4.009011 340.975372 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 1.600001 346.055664 7.000000
      vertex 2.371780 346.375366 7.000000
      vertex 3.651444 340.509399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 0.937259 345.547150 7.000000
      vertex 1.600001 346.055664 7.000000
      vertex 3.651444 340.509399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 0.000001 343.284393 7.000000
      vertex 0.937259 345.547150 7.000000
      vertex 3.651444 340.509399 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 0.428720 344.884399 7.000000
      vertex 0.937259 345.547150 7.000000
      vertex 0.000001 343.284393 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 0.109038 344.112610 7.000000
      vertex 0.428720 344.884399 7.000000
      vertex 0.000001 343.284393 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 0.000001 343.284393 7.000000
      vertex 3.651444 340.509399 7.000000
      vertex 3.426668 339.966736 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 3.350001 339.384399 7.000000
      vertex 0.000001 343.284393 7.000000
      vertex 3.426668 339.966736 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 3.426668 338.802063 7.000000
      vertex 0.000001 343.284393 7.000000
      vertex 3.350001 339.384399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 4.600001 327.884399 7.000000
      vertex 0.000001 343.284393 7.000000
      vertex 3.426668 338.802063 7.000000
    endloop
  endfacet
  facet normal -0.000000 -0.000000 -1.000000
    outer loop
      vertex 3.651444 338.259399 7.000000
      vertex 4.600001 327.884399 7.000000
      vertex 3.426668 338.802063 7.000000
    endloop
  endfacet
  facet normal -0.000000 0.000000 -1.000000
    outer loop
      vertex 4.784001 329.282013 7.000000
      vertex 4.600001 327.884399 7.000000
      vertex 3.651444 338.259399 7.000000
    endloop
  endfacet
  facet normal -0.000000 -0.000000 -1.000000
    outer loop
      vertex 4.009011 337.793396 7.000000
      vertex 4.784001 329.282013 7.000000
      vertex 3.651444 338.259399 7.000000
    endloop
  endfacet
  facet normal -0.000000 0.000000 -1.000000
    outer loop
      vertex 5.323464 330.584381 7.000000
      vertex 4.784001 329.282013 7.000000
      vertex 4.009011 337.793396 7.000000
    endloop
  endfacet
  facet normal -0.000000 -0.000000 -1.000000
    outer loop
      vertex 4.475001 337.435852 7.000000
      vertex 5.323464 330.584381 7.000000
      vertex 4.009011 337.793396 7.000000
    endloop
  endfacet
  facet normal -0.000000 -0.000000 -1.000000
    outer loop
      vertex 5.017658 337.211060 7.000000
      vertex 5.323464 330.584381 7.000000
      vertex 4.475001 337.435852 7.000000
    endloop
  endfacet
  facet normal -0.000000 0.000000 -1.000000
    outer loop
      vertex 6.181624 331.702759 7.000000
      vertex 5.323464 330.584381 7.000000
      vertex 5.017658 337.211060 7.000000
    endloop
  endfacet
  facet normal -0.000000 -0.000000 -1.000000
    outer loop
      vertex 5.600001 337.134399 7.000000
      vertex 6.181624 331.702759 7.000000
      vertex 5.017658 337.211060 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 6.182344 337.211060 7.000000
      vertex 6.181624 331.702759 7.000000
      vertex 5.600001 337.134399 7.000000
    endloop
  endfacet
  facet normal -0.000000 0.000000 -1.000000
    outer loop
      vertex 7.300001 332.560944 7.000000
      vertex 6.181624 331.702759 7.000000
      vertex 6.182344 337.211060 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 6.725001 337.435852 7.000000
      vertex 7.300001 332.560944 7.000000
      vertex 6.182344 337.211060 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 7.190991 337.793396 7.000000
      vertex 7.300001 332.560944 7.000000
      vertex 6.725001 337.435852 7.000000
    endloop
  endfacet
  facet normal -0.000000 0.000000 -1.000000
    outer loop
      vertex 8.602378 333.100403 7.000000
      vertex 7.300001 332.560944 7.000000
      vertex 7.190991 337.793396 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 7.548558 338.259399 7.000000
      vertex 8.602378 333.100403 7.000000
      vertex 7.190991 337.793396 7.000000
    endloop
  endfacet
  facet normal -0.000000 0.000000 -1.000000
    outer loop
      vertex 10.000001 333.284393 7.000000
      vertex 8.602378 333.100403 7.000000
      vertex 7.548558 338.259399 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 7.773334 338.802063 7.000000
      vertex 10.000001 333.284393 7.000000
      vertex 7.548558 338.259399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 30.850000 339.384399 7.000000
      vertex 30.773335 339.966736 7.000000
      vertex 38.000000 346.484406 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 33.900002 332.560944 7.000000
      vertex 30.850000 339.384399 7.000000
      vertex 38.000000 346.484406 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 32.597626 333.100403 7.000000
      vertex 30.850000 339.384399 7.000000
      vertex 33.900002 332.560944 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 38.000000 346.484406 7.000000
      vertex 30.773335 339.966736 7.000000
      vertex 30.548557 340.509399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 30.190990 340.975372 7.000000
      vertex 38.000000 346.484406 7.000000
      vertex 30.548557 340.509399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 29.725000 341.332947 7.000000
      vertex 38.000000 346.484406 7.000000
      vertex 30.190990 340.975372 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 38.000000 346.484406 7.000000
      vertex 29.725000 341.332947 7.000000
      vertex 29.182344 341.557739 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 28.600000 341.634399 7.000000
      vertex 38.000000 346.484406 7.000000
      vertex 29.182344 341.557739 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 28.017658 341.557739 7.000000
      vertex 38.000000 346.484406 7.000000
      vertex 28.600000 341.634399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 3.200001 346.484406 7.000000
      vertex 38.000000 346.484406 7.000000
      vertex 28.017658 341.557739 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 27.475000 341.332947 7.000000
      vertex 3.200001 346.484406 7.000000
      vertex 28.017658 341.557739 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 27.009010 340.975372 7.000000
      vertex 3.200001 346.484406 7.000000
      vertex 27.475000 341.332947 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 10.000001 333.284393 7.000000
      vertex 26.426668 339.966736 7.000000
      vertex 26.350000 339.384399 7.000000
    endloop
  endfacet
  facet normal -0.000000 0.000000 -1.000000
    outer loop
      vertex 26.426668 338.802063 7.000000
      vertex 10.000001 333.284393 7.000000
      vertex 26.350000 339.384399 7.000000
    endloop
  endfacet
  facet normal -0.000000 0.000000 -1.000000
    outer loop
      vertex 26.651443 338.259399 7.000000
      vertex 10.000001 333.284393 7.000000
      vertex 26.426668 338.802063 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 10.000001 333.284393 7.000000
      vertex 26.651443 338.259399 7.000000
      vertex 27.009010 337.793396 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 31.200001 333.284393 7.000000
      vertex 10.000001 333.284393 7.000000
      vertex 27.009010 337.793396 7.000000
    endloop
  endfacet
  facet normal -0.000000 -0.000000 -1.000000
    outer loop
      vertex 27.475000 337.435852 7.000000
      vertex 31.200001 333.284393 7.000000
      vertex 27.009010 337.793396 7.000000
    endloop
  endfacet
  facet normal -0.000000 -0.000000 -1.000000
    outer loop
      vertex 28.017658 337.211060 7.000000
      vertex 31.200001 333.284393 7.000000
      vertex 27.475000 337.435852 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 31.200001 333.284393 7.000000
      vertex 28.017658 337.211060 7.000000
      vertex 28.600000 337.134399 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 29.182344 337.211060 7.000000
      vertex 31.200001 333.284393 7.000000
      vertex 28.600000 337.134399 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 29.725000 337.435852 7.000000
      vertex 31.200001 333.284393 7.000000
      vertex 29.182344 337.211060 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 31.200001 333.284393 7.000000
      vertex 29.725000 337.435852 7.000000
      vertex 30.190990 337.793396 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 30.548557 338.259399 7.000000
      vertex 31.200001 333.284393 7.000000
      vertex 30.190990 337.793396 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 32.597626 333.100403 7.000000
      vertex 31.200001 333.284393 7.000000
      vertex 30.548557 338.259399 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 30.773335 338.802063 7.000000
      vertex 32.597626 333.100403 7.000000
      vertex 30.548557 338.259399 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 30.850000 339.384399 7.000000
      vertex 32.597626 333.100403 7.000000
      vertex 30.773335 338.802063 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 30.850000 281.384399 7.000000
      vertex 30.773335 281.966736 7.000000
      vertex 32.597626 287.668396 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 33.900002 288.207855 7.000000
      vertex 30.850000 281.384399 7.000000
      vertex 32.597626 287.668396 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 38.000000 273.284393 7.000000
      vertex 30.850000 281.384399 7.000000
      vertex 33.900002 288.207855 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 35.018379 289.066010 7.000000
      vertex 38.000000 273.284393 7.000000
      vertex 33.900002 288.207855 7.000000
    endloop
  endfacet
  facet normal -0.000000 0.000000 -1.000000
    outer loop
      vertex 41.200001 276.484406 7.000000
      vertex 38.000000 273.284393 7.000000
      vertex 35.018379 289.066010 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 35.876537 290.184387 7.000000
      vertex 41.200001 276.484406 7.000000
      vertex 35.018379 289.066010 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 36.416000 291.486786 7.000000
      vertex 41.200001 276.484406 7.000000
      vertex 35.876537 290.184387 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 32.597626 287.668396 7.000000
      vertex 30.773335 281.966736 7.000000
      vertex 30.548557 282.509399 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 31.200001 287.484406 7.000000
      vertex 32.597626 287.668396 7.000000
      vertex 30.548557 282.509399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 30.190990 282.975372 7.000000
      vertex 31.200001 287.484406 7.000000
      vertex 30.548557 282.509399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 29.725000 283.332947 7.000000
      vertex 31.200001 287.484406 7.000000
      vertex 30.190990 282.975372 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 31.200001 287.484406 7.000000
      vertex 29.725000 283.332947 7.000000
      vertex 29.182344 283.557739 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 28.600000 283.634399 7.000000
      vertex 31.200001 287.484406 7.000000
      vertex 29.182344 283.557739 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 28.017658 283.557739 7.000000
      vertex 31.200001 287.484406 7.000000
      vertex 28.600000 283.634399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 31.200001 287.484406 7.000000
      vertex 28.017658 283.557739 7.000000
      vertex 27.475000 283.332947 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 27.009010 282.975372 7.000000
      vertex 31.200001 287.484406 7.000000
      vertex 27.475000 283.332947 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 10.000001 287.484406 7.000000
      vertex 31.200001 287.484406 7.000000
      vertex 27.009010 282.975372 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 26.651443 282.509399 7.000000
      vertex 10.000001 287.484406 7.000000
      vertex 27.009010 282.975372 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 26.426668 281.966736 7.000000
      vertex 10.000001 287.484406 7.000000
      vertex 26.651443 282.509399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 10.000001 287.484406 7.000000
      vertex 26.426668 281.966736 7.000000
      vertex 26.350000 281.384399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 26.426668 280.802063 7.000000
      vertex 10.000001 287.484406 7.000000
      vertex 26.350000 281.384399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 3.200001 273.284393 7.000000
      vertex 27.475000 279.435852 7.000000
      vertex 28.017658 279.211060 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 38.000000 273.284393 7.000000
      vertex 3.200001 273.284393 7.000000
      vertex 28.017658 279.211060 7.000000
    endloop
  endfacet
  facet normal -0.000000 -0.000000 -1.000000
    outer loop
      vertex 28.600000 279.134399 7.000000
      vertex 38.000000 273.284393 7.000000
      vertex 28.017658 279.211060 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 29.182344 279.211060 7.000000
      vertex 38.000000 273.284393 7.000000
      vertex 28.600000 279.134399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 38.000000 273.284393 7.000000
      vertex 29.182344 279.211060 7.000000
      vertex 29.725000 279.435852 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 30.190990 279.793396 7.000000
      vertex 38.000000 273.284393 7.000000
      vertex 29.725000 279.435852 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 30.548557 280.259399 7.000000
      vertex 38.000000 273.284393 7.000000
      vertex 30.190990 279.793396 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 38.000000 273.284393 7.000000
      vertex 30.548557 280.259399 7.000000
      vertex 30.773335 280.802063 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 30.850000 281.384399 7.000000
      vertex 38.000000 273.284393 7.000000
      vertex 30.773335 280.802063 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 0.000001 343.284393 7.000000
      vertex 4.600001 327.884399 7.000000
      vertex 4.600001 292.884399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 0.000001 276.484406 7.000000
      vertex 0.000001 343.284393 7.000000
      vertex 4.600001 292.884399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 41.200001 276.484406 7.000000
      vertex 36.416000 291.486786 7.000000
      vertex 36.600002 292.884399 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 41.200001 343.284393 7.000000
      vertex 41.200001 276.484406 7.000000
      vertex 36.600002 292.884399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 36.600002 327.884399 7.000000
      vertex 41.200001 343.284393 7.000000
      vertex 36.600002 292.884399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 36.416000 329.282013 7.000000
      vertex 41.200001 343.284393 7.000000
      vertex 36.600002 327.884399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 41.200001 343.284393 7.000000
      vertex 36.416000 329.282013 7.000000
      vertex 35.876537 330.584381 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 35.018379 331.702759 7.000000
      vertex 41.200001 343.284393 7.000000
      vertex 35.876537 330.584381 7.000000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 -1.000000
    outer loop
      vertex 38.000000 346.484406 7.000000
      vertex 41.200001 343.284393 7.000000
      vertex 35.018379 331.702759 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 33.900002 332.560944 7.000000
      vertex 38.000000 346.484406 7.000000
      vertex 35.018379 331.702759 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 41.200001 343.284393 7.000000
      vertex 38.000000 346.484406 7.000000
      vertex 38.828220 346.375366 7.000000
    endloop
  endfacet
  facet normal -0.000000 -0.000000 -1.000000
    outer loop
      vertex 39.600002 346.055664 7.000000
      vertex 41.200001 343.284393 7.000000
      vertex 38.828220 346.375366 7.000000
    endloop
  endfacet
  facet normal -0.000000 -0.000000 -1.000000
    outer loop
      vertex 40.262741 345.547150 7.000000
      vertex 41.200001 343.284393 7.000000
      vertex 39.600002 346.055664 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 41.200001 343.284393 7.000000
      vertex 40.262741 345.547150 7.000000
      vertex 40.771282 344.884399 7.000000
    endloop
  endfacet
  facet normal -0.000000 -0.000000 -1.000000
    outer loop
      vertex 41.090965 344.112610 7.000000
      vertex 41.200001 343.284393 7.000000
      vertex 40.771282 344.884399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 41.200001 276.484406 7.000000
      vertex 41.090965 275.656189 7.000000
      vertex 40.771282 274.884399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 40.262741 274.221649 7.000000
      vertex 41.200001 276.484406 7.000000
      vertex 40.771282 274.884399 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 39.600002 273.713104 7.000000
      vertex 41.200001 276.484406 7.000000
      vertex 40.262741 274.221649 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 41.200001 276.484406 7.000000
      vertex 39.600002 273.713104 7.000000
      vertex 38.828220 273.393433 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 38.000000 273.284393 7.000000
      vertex 41.200001 276.484406 7.000000
      vertex 38.828220 273.393433 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 0.000001 276.484406 7.000000
      vertex 0.428720 274.884399 7.000000
      vertex 0.109038 275.656189 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 1.100001 336.284393 33.599998
      vertex 1.600001 336.284393 33.599998
      vertex 1.600001 343.284393 33.599998
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 0.000001 343.284393 33.599998
      vertex 1.100001 336.284393 33.599998
      vertex 1.600001 343.284393 33.599998
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 1.100001 284.484406 33.599998
      vertex 1.100001 336.284393 33.599998
      vertex 0.000001 343.284393 33.599998
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 0.000001 276.484406 33.599998
      vertex 1.100001 284.484406 33.599998
      vertex 0.000001 343.284393 33.599998
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 1.600001 276.484406 33.599998
      vertex 1.100001 284.484406 33.599998
      vertex 0.000001 276.484406 33.599998
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 0.109038 275.656189 33.599998
      vertex 1.600001 276.484406 33.599998
      vertex 0.000001 276.484406 33.599998
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 0.428720 274.884399 33.599998
      vertex 1.600001 276.484406 33.599998
      vertex 0.109038 275.656189 33.599998
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 1.600001 343.284393 33.599998
      vertex 1.654520 343.698517 33.599998
      vertex 0.428720 344.884399 33.599998
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 0.109038 344.112610 33.599998
      vertex 1.600001 343.284393 33.599998
      vertex 0.428720 344.884399 33.599998
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 0.000001 343.284393 33.599998
      vertex 1.600001 343.284393 33.599998
      vertex 0.109038 344.112610 33.599998
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 0.937259 345.547150 33.599998
      vertex 0.428720 344.884399 33.599998
      vertex 1.654520 343.698517 33.599998
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 1.814360 344.084381 33.599998
      vertex 0.937259 345.547150 33.599998
      vertex 1.654520 343.698517 33.599998
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 1.600001 346.055664 33.599998
      vertex 0.937259 345.547150 33.599998
      vertex 1.814360 344.084381 33.599998
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 2.068630 344.415771 33.599998
      vertex 1.600001 346.055664 33.599998
      vertex 1.814360 344.084381 33.599998
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 2.400001 344.670044 33.599998
      vertex 1.600001 346.055664 33.599998
      vertex 2.068630 344.415771 33.599998
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 2.371780 346.375366 33.599998
      vertex 1.600001 346.055664 33.599998
      vertex 2.400001 344.670044 33.599998
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 2.785891 344.829865 33.599998
      vertex 2.371780 346.375366 33.599998
      vertex 2.400001 344.670044 33.599998
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 3.200001 346.484406 33.599998
      vertex 2.371780 346.375366 33.599998
      vertex 2.785891 344.829865 33.599998
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 3.200001 344.884399 33.599998
      vertex 3.200001 346.484406 33.599998
      vertex 2.785891 344.829865 33.599998
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 38.000000 346.484406 33.599998
      vertex 3.200001 346.484406 33.599998
      vertex 3.200001 344.884399 33.599998
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 38.000000 344.884399 33.599998
      vertex 38.000000 346.484406 33.599998
      vertex 3.200001 344.884399 33.599998
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 38.414112 344.829865 33.599998
      vertex 38.000000 346.484406 33.599998
      vertex 38.000000 344.884399 33.599998
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 38.828220 346.375366 33.599998
      vertex 38.000000 346.484406 33.599998
      vertex 38.414112 344.829865 33.599998
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 38.799999 344.670044 33.599998
      vertex 38.828220 346.375366 33.599998
      vertex 38.414112 344.829865 33.599998
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 39.600002 346.055664 33.599998
      vertex 38.828220 346.375366 33.599998
      vertex 38.799999 344.670044 33.599998
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 39.131371 344.415771 33.599998
      vertex 39.600002 346.055664 33.599998
      vertex 38.799999 344.670044 33.599998
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 39.385643 344.084381 33.599998
      vertex 39.600002 346.055664 33.599998
      vertex 39.131371 344.415771 33.599998
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 40.262741 345.547150 33.599998
      vertex 39.600002 346.055664 33.599998
      vertex 39.385643 344.084381 33.599998
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 39.545483 343.698517 33.599998
      vertex 40.262741 345.547150 33.599998
      vertex 39.385643 344.084381 33.599998
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 40.771282 344.884399 33.599998
      vertex 40.262741 345.547150 33.599998
      vertex 39.545483 343.698517 33.599998
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 39.600002 343.284393 33.599998
      vertex 40.771282 344.884399 33.599998
      vertex 39.545483 343.698517 33.599998
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 41.090965 344.112610 33.599998
      vertex 40.771282 344.884399 33.599998
      vertex 39.600002 343.284393 33.599998
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 41.200001 343.284393 33.599998
      vertex 41.090965 344.112610 33.599998
      vertex 39.600002 343.284393 33.599998
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 39.600002 276.484406 33.599998
      vertex 41.200001 343.284393 33.599998
      vertex 39.600002 343.284393 33.599998
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 41.200001 276.484406 33.599998
      vertex 41.200001 343.284393 33.599998
      vertex 39.600002 276.484406 33.599998
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 41.090965 275.656189 33.599998
      vertex 41.200001 276.484406 33.599998
      vertex 39.600002 276.484406 33.599998
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 40.771282 274.884399 33.599998
      vertex 41.090965 275.656189 33.599998
      vertex 39.600002 276.484406 33.599998
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 39.545483 276.070282 33.599998
      vertex 40.771282 274.884399 33.599998
      vertex 39.600002 276.484406 33.599998
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 40.262741 274.221649 33.599998
      vertex 40.771282 274.884399 33.599998
      vertex 39.545483 276.070282 33.599998
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 39.385643 275.684387 33.599998
      vertex 40.262741 274.221649 33.599998
      vertex 39.545483 276.070282 33.599998
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 39.600002 273.713104 33.599998
      vertex 40.262741 274.221649 33.599998
      vertex 39.385643 275.684387 33.599998
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 39.131371 275.353027 33.599998
      vertex 39.600002 273.713104 33.599998
      vertex 39.385643 275.684387 33.599998
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 38.799999 275.098755 33.599998
      vertex 39.600002 273.713104 33.599998
      vertex 39.131371 275.353027 33.599998
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 38.828220 273.393433 33.599998
      vertex 39.600002 273.713104 33.599998
      vertex 38.799999 275.098755 33.599998
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 38.414112 274.938904 33.599998
      vertex 38.828220 273.393433 33.599998
      vertex 38.799999 275.098755 33.599998
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 38.000000 273.284393 33.599998
      vertex 38.828220 273.393433 33.599998
      vertex 38.414112 274.938904 33.599998
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 38.000000 274.884399 33.599998
      vertex 38.000000 273.284393 33.599998
      vertex 38.414112 274.938904 33.599998
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 3.200001 273.284393 33.599998
      vertex 38.000000 273.284393 33.599998
      vertex 38.000000 274.884399 33.599998
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 3.200001 274.884399 33.599998
      vertex 3.200001 273.284393 33.599998
      vertex 38.000000 274.884399 33.599998
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 2.785891 274.938904 33.599998
      vertex 3.200001 273.284393 33.599998
      vertex 3.200001 274.884399 33.599998
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 2.371780 273.393433 33.599998
      vertex 3.200001 273.284393 33.599998
      vertex 2.785891 274.938904 33.599998
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 2.400001 275.098755 33.599998
      vertex 2.371780 273.393433 33.599998
      vertex 2.785891 274.938904 33.599998
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 1.600001 273.713104 33.599998
      vertex 2.371780 273.393433 33.599998
      vertex 2.400001 275.098755 33.599998
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 2.068630 275.353027 33.599998
      vertex 1.600001 273.713104 33.599998
      vertex 2.400001 275.098755 33.599998
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 1.814360 275.684387 33.599998
      vertex 1.600001 273.713104 33.599998
      vertex 2.068630 275.353027 33.599998
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 0.937259 274.221649 33.599998
      vertex 1.600001 273.713104 33.599998
      vertex 1.814360 275.684387 33.599998
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 1.654520 276.070282 33.599998
      vertex 0.937259 274.221649 33.599998
      vertex 1.814360 275.684387 33.599998
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 0.428720 274.884399 33.599998
      vertex 0.937259 274.221649 33.599998
      vertex 1.654520 276.070282 33.599998
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 1.600001 276.484406 33.599998
      vertex 0.428720 274.884399 33.599998
      vertex 1.654520 276.070282 33.599998
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 1.100001 284.484406 33.599998
      vertex 1.600001 276.484406 33.599998
      vertex 1.600001 284.484406 33.599998
    endloop
  endfacet
  facet normal 0.991445 0.130525 0.000000
    outer loop
      vertex 41.090965 344.112610 33.599998
      vertex 41.200001 343.284393 33.599998
      vertex 41.200001 343.284393 7.000000
    endloop
  endfacet
  facet normal 0.991445 0.130525 -0.000000
    outer loop
      vertex 41.090965 344.112610 7.000000
      vertex 41.090965 344.112610 33.599998
      vertex 41.200001 343.284393 7.000000
    endloop
  endfacet
  facet normal 0.923881 0.382681 0.000000
    outer loop
      vertex 40.771282 344.884399 33.599998
      vertex 41.090965 344.112610 33.599998
      vertex 41.090965 344.112610 7.000000
    endloop
  endfacet
  facet normal 0.923881 0.382681 -0.000000
    outer loop
      vertex 40.771282 344.884399 7.000000
      vertex 40.771282 344.884399 33.599998
      vertex 41.090965 344.112610 7.000000
    endloop
  endfacet
  facet normal 0.793356 0.608758 0.000000
    outer loop
      vertex 40.262741 345.547150 33.599998
      vertex 40.771282 344.884399 33.599998
      vertex 40.771282 344.884399 7.000000
    endloop
  endfacet
  facet normal 0.793356 0.608758 -0.000000
    outer loop
      vertex 40.262741 345.547150 7.000000
      vertex 40.262741 345.547150 33.599998
      vertex 40.771282 344.884399 7.000000
    endloop
  endfacet
  facet normal 0.608744 0.793367 0.000000
    outer loop
      vertex 39.600002 346.055664 33.599998
      vertex 40.262741 345.547150 33.599998
      vertex 40.262741 345.547150 7.000000
    endloop
  endfacet
  facet normal 0.608744 0.793367 -0.000000
    outer loop
      vertex 39.600002 346.055664 7.000000
      vertex 39.600002 346.055664 33.599998
      vertex 40.262741 345.547150 7.000000
    endloop
  endfacet
  facet normal 0.382703 0.923871 0.000000
    outer loop
      vertex 38.828220 346.375366 33.599998
      vertex 39.600002 346.055664 33.599998
      vertex 39.600002 346.055664 7.000000
    endloop
  endfacet
  facet normal 0.382703 0.923871 -0.000000
    outer loop
      vertex 38.828220 346.375366 7.000000
      vertex 38.828220 346.375366 33.599998
      vertex 39.600002 346.055664 7.000000
    endloop
  endfacet
  facet normal 0.130529 0.991445 0.000000
    outer loop
      vertex 38.000000 346.484406 33.599998
      vertex 38.828220 346.375366 33.599998
      vertex 38.828220 346.375366 7.000000
    endloop
  endfacet
  facet normal 0.130529 0.991445 -0.000000
    outer loop
      vertex 38.000000 346.484406 7.000000
      vertex 38.000000 346.484406 33.599998
      vertex 38.828220 346.375366 7.000000
    endloop
  endfacet
  facet normal 0.991445 -0.130525 0.000000
    outer loop
      vertex 41.090965 275.656189 7.000000
      vertex 41.200001 276.484406 7.000000
      vertex 41.200001 276.484406 33.599998
    endloop
  endfacet
  facet normal 0.991445 -0.130525 0.000000
    outer loop
      vertex 41.090965 275.656189 33.599998
      vertex 41.090965 275.656189 7.000000
      vertex 41.200001 276.484406 33.599998
    endloop
  endfacet
  facet normal 0.923881 -0.382681 0.000000
    outer loop
      vertex 40.771282 274.884399 7.000000
      vertex 41.090965 275.656189 7.000000
      vertex 41.090965 275.656189 33.599998
    endloop
  endfacet
  facet normal 0.923881 -0.382681 0.000000
    outer loop
      vertex 40.771282 274.884399 33.599998
      vertex 40.771282 274.884399 7.000000
      vertex 41.090965 275.656189 33.599998
    endloop
  endfacet
  facet normal 0.793356 -0.608758 0.000000
    outer loop
      vertex 40.262741 274.221649 7.000000
      vertex 40.771282 274.884399 7.000000
      vertex 40.771282 274.884399 33.599998
    endloop
  endfacet
  facet normal 0.793356 -0.608758 0.000000
    outer loop
      vertex 40.262741 274.221649 33.599998
      vertex 40.262741 274.221649 7.000000
      vertex 40.771282 274.884399 33.599998
    endloop
  endfacet
  facet normal 0.608767 -0.793349 0.000000
    outer loop
      vertex 39.600002 273.713104 7.000000
      vertex 40.262741 274.221649 7.000000
      vertex 40.262741 274.221649 33.599998
    endloop
  endfacet
  facet normal 0.608767 -0.793349 0.000000
    outer loop
      vertex 39.600002 273.713104 33.599998
      vertex 39.600002 273.713104 7.000000
      vertex 40.262741 274.221649 33.599998
    endloop
  endfacet
  facet normal 0.382672 -0.923884 0.000000
    outer loop
      vertex 38.828220 273.393433 7.000000
      vertex 39.600002 273.713104 7.000000
      vertex 39.600002 273.713104 33.599998
    endloop
  endfacet
  facet normal 0.382672 -0.923884 0.000000
    outer loop
      vertex 38.828220 273.393433 33.599998
      vertex 38.828220 273.393433 7.000000
      vertex 39.600002 273.713104 33.599998
    endloop
  endfacet
  facet normal 0.130529 -0.991445 0.000000
    outer loop
      vertex 38.000000 273.284393 7.000000
      vertex 38.828220 273.393433 7.000000
      vertex 38.828220 273.393433 33.599998
    endloop
  endfacet
  facet normal 0.130529 -0.991445 0.000000
    outer loop
      vertex 38.000000 273.284393 33.599998
      vertex 38.000000 273.284393 7.000000
      vertex 38.828220 273.393433 33.599998
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 38.000000 273.284393 7.000000
      vertex 38.000000 273.284393 33.599998
      vertex 21.961481 273.284393 19.511734
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 22.200001 273.284393 17.700001
      vertex 38.000000 273.284393 7.000000
      vertex 21.961481 273.284393 19.511734
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 22.200001 273.284393 11.600000
      vertex 38.000000 273.284393 7.000000
      vertex 22.200001 273.284393 17.700001
    endloop
  endfacet
  facet normal -0.000000 -1.000000 0.000000
    outer loop
      vertex 38.000000 273.284393 33.599998
      vertex 3.200001 273.284393 33.599998
      vertex 17.011734 273.284393 24.461481
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 18.700001 273.284393 23.762178
      vertex 38.000000 273.284393 33.599998
      vertex 17.011734 273.284393 24.461481
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 20.149748 273.284393 22.649748
      vertex 38.000000 273.284393 33.599998
      vertex 18.700001 273.284393 23.762178
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 3.200001 273.284393 33.599998
      vertex 3.200001 273.284393 7.000000
      vertex 8.200001 273.284393 17.700001
    endloop
  endfacet
  facet normal -0.000000 -1.000000 0.000000
    outer loop
      vertex 8.438520 273.284393 19.511734
      vertex 3.200001 273.284393 33.599998
      vertex 8.200001 273.284393 17.700001
    endloop
  endfacet
  facet normal -0.000000 -1.000000 0.000000
    outer loop
      vertex 9.137823 273.284393 21.200001
      vertex 3.200001 273.284393 33.599998
      vertex 8.438520 273.284393 19.511734
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 3.200001 273.284393 7.000000
      vertex 38.000000 273.284393 7.000000
      vertex 22.200001 273.284393 11.600000
    endloop
  endfacet
  facet normal 0.000000 -1.000000 -0.000000
    outer loop
      vertex 8.200001 273.284393 11.600000
      vertex 3.200001 273.284393 7.000000
      vertex 22.200001 273.284393 11.600000
    endloop
  endfacet
  facet normal 0.000000 -1.000000 -0.000000
    outer loop
      vertex 8.200001 273.284393 17.700001
      vertex 3.200001 273.284393 7.000000
      vertex 8.200001 273.284393 11.600000
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 3.200001 273.284393 33.599998
      vertex 9.137823 273.284393 21.200001
      vertex 10.250254 273.284393 22.649748
    endloop
  endfacet
  facet normal -0.000000 -1.000000 0.000000
    outer loop
      vertex 11.700001 273.284393 23.762178
      vertex 3.200001 273.284393 33.599998
      vertex 10.250254 273.284393 22.649748
    endloop
  endfacet
  facet normal -0.000000 -1.000000 0.000000
    outer loop
      vertex 13.388268 273.284393 24.461481
      vertex 3.200001 273.284393 33.599998
      vertex 11.700001 273.284393 23.762178
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 3.200001 273.284393 33.599998
      vertex 13.388268 273.284393 24.461481
      vertex 15.200001 273.284393 24.700001
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 17.011734 273.284393 24.461481
      vertex 3.200001 273.284393 33.599998
      vertex 15.200001 273.284393 24.700001
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 38.000000 273.284393 33.599998
      vertex 20.149748 273.284393 22.649748
      vertex 21.262178 273.284393 21.200001
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 21.961481 273.284393 19.511734
      vertex 38.000000 273.284393 33.599998
      vertex 21.262178 273.284393 21.200001
    endloop
  endfacet
  facet normal -0.991445 -0.130527 0.000000
    outer loop
      vertex 0.109038 275.656189 33.599998
      vertex 0.000001 276.484406 33.599998
      vertex 0.000001 276.484406 7.000000
    endloop
  endfacet
  facet normal -0.991445 -0.130527 0.000000
    outer loop
      vertex 0.109038 275.656189 7.000000
      vertex 0.109038 275.656189 33.599998
      vertex 0.000001 276.484406 7.000000
    endloop
  endfacet
  facet normal -0.923881 -0.382679 0.000000
    outer loop
      vertex 0.428720 274.884399 33.599998
      vertex 0.109038 275.656189 33.599998
      vertex 0.109038 275.656189 7.000000
    endloop
  endfacet
  facet normal -0.923881 -0.382679 0.000000
    outer loop
      vertex 0.428720 274.884399 7.000000
      vertex 0.428720 274.884399 33.599998
      vertex 0.109038 275.656189 7.000000
    endloop
  endfacet
  facet normal -0.793357 -0.608756 0.000000
    outer loop
      vertex 0.937259 274.221649 33.599998
      vertex 0.428720 274.884399 33.599998
      vertex 0.428720 274.884399 7.000000
    endloop
  endfacet
  facet normal -0.793357 -0.608756 0.000000
    outer loop
      vertex 0.937259 274.221649 7.000000
      vertex 0.937259 274.221649 33.599998
      vertex 0.428720 274.884399 7.000000
    endloop
  endfacet
  facet normal -0.608765 -0.793350 0.000000
    outer loop
      vertex 1.600001 273.713104 33.599998
      vertex 0.937259 274.221649 33.599998
      vertex 0.937259 274.221649 7.000000
    endloop
  endfacet
  facet normal -0.608765 -0.793350 0.000000
    outer loop
      vertex 1.600001 273.713104 7.000000
      vertex 1.600001 273.713104 33.599998
      vertex 0.937259 274.221649 7.000000
    endloop
  endfacet
  facet normal -0.382673 -0.923884 0.000000
    outer loop
      vertex 2.371780 273.393433 33.599998
      vertex 1.600001 273.713104 33.599998
      vertex 1.600001 273.713104 7.000000
    endloop
  endfacet
  facet normal -0.382673 -0.923884 0.000000
    outer loop
      vertex 2.371780 273.393433 7.000000
      vertex 2.371780 273.393433 33.599998
      vertex 1.600001 273.713104 7.000000
    endloop
  endfacet
  facet normal -0.130528 -0.991445 0.000000
    outer loop
      vertex 3.200001 273.284393 33.599998
      vertex 2.371780 273.393433 33.599998
      vertex 2.371780 273.393433 7.000000
    endloop
  endfacet
  facet normal -0.130528 -0.991445 0.000000
    outer loop
      vertex 3.200001 273.284393 7.000000
      vertex 3.200001 273.284393 33.599998
      vertex 2.371780 273.393433 7.000000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 36.600002 327.884399 8.600000
      vertex 36.600002 292.884399 8.600000
      vertex 39.600002 284.484406 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 39.600002 336.284393 8.600000
      vertex 36.600002 327.884399 8.600000
      vertex 39.600002 284.484406 8.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 36.416000 329.282013 8.600000
      vertex 36.600002 327.884399 8.600000
      vertex 39.600002 336.284393 8.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 35.876537 330.584381 8.600000
      vertex 36.416000 329.282013 8.600000
      vertex 39.600002 336.284393 8.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 35.018379 331.702759 8.600000
      vertex 35.876537 330.584381 8.600000
      vertex 39.600002 336.284393 8.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 33.900002 332.560944 8.600000
      vertex 35.018379 331.702759 8.600000
      vertex 39.600002 336.284393 8.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 32.597626 333.100403 8.600000
      vertex 33.900002 332.560944 8.600000
      vertex 39.600002 336.284393 8.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 28.600000 336.284393 8.600000
      vertex 32.597626 333.100403 8.600000
      vertex 39.600002 336.284393 8.600000
    endloop
  endfacet
  facet normal -0.000000 -0.000000 1.000000
    outer loop
      vertex 31.200001 333.284393 8.600000
      vertex 32.597626 333.100403 8.600000
      vertex 28.600000 336.284393 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 27.797663 336.390015 8.600000
      vertex 31.200001 333.284393 8.600000
      vertex 28.600000 336.284393 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 27.050001 336.699707 8.600000
      vertex 31.200001 333.284393 8.600000
      vertex 27.797663 336.390015 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 39.600002 284.484406 8.600000
      vertex 36.600002 292.884399 8.600000
      vertex 36.416000 291.486786 8.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 35.876537 290.184387 8.600000
      vertex 39.600002 284.484406 8.600000
      vertex 36.416000 291.486786 8.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 35.018379 289.066010 8.600000
      vertex 39.600002 284.484406 8.600000
      vertex 35.876537 290.184387 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 39.600002 284.484406 8.600000
      vertex 35.018379 289.066010 8.600000
      vertex 33.900002 288.207855 8.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 32.597626 287.668396 8.600000
      vertex 39.600002 284.484406 8.600000
      vertex 33.900002 288.207855 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 28.600000 284.484406 8.600000
      vertex 39.600002 284.484406 8.600000
      vertex 32.597626 287.668396 8.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 31.200001 287.484406 8.600000
      vertex 28.600000 284.484406 8.600000
      vertex 32.597626 287.668396 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 27.797663 284.378754 8.600000
      vertex 28.600000 284.484406 8.600000
      vertex 31.200001 287.484406 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 27.050001 284.069061 8.600000
      vertex 27.797663 284.378754 8.600000
      vertex 31.200001 287.484406 8.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 10.000001 287.484406 8.600000
      vertex 27.050001 284.069061 8.600000
      vertex 31.200001 287.484406 8.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 26.407970 283.576416 8.600000
      vertex 27.050001 284.069061 8.600000
      vertex 10.000001 287.484406 8.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 25.915321 282.934387 8.600000
      vertex 26.407970 283.576416 8.600000
      vertex 10.000001 287.484406 8.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 25.605631 282.186737 8.600000
      vertex 25.915321 282.934387 8.600000
      vertex 10.000001 287.484406 8.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 25.500002 281.384399 8.600000
      vertex 25.605631 282.186737 8.600000
      vertex 10.000001 287.484406 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 8.700001 281.384399 8.600000
      vertex 25.500002 281.384399 8.600000
      vertex 10.000001 287.484406 8.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 25.500002 274.884399 8.600000
      vertex 25.500002 281.384399 8.600000
      vertex 8.700001 281.384399 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 8.700001 274.884399 8.600000
      vertex 25.500002 274.884399 8.600000
      vertex 8.700001 281.384399 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 10.000001 287.484406 8.600000
      vertex 8.602378 287.668396 8.600000
      vertex 8.284679 282.934387 8.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 8.594371 282.186737 8.600000
      vertex 10.000001 287.484406 8.600000
      vertex 8.284679 282.934387 8.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 8.700001 281.384399 8.600000
      vertex 10.000001 287.484406 8.600000
      vertex 8.594371 282.186737 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 8.602378 287.668396 8.600000
      vertex 7.300001 288.207855 8.600000
      vertex 7.150001 284.069061 8.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 7.792032 283.576416 8.600000
      vertex 8.602378 287.668396 8.600000
      vertex 7.150001 284.069061 8.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 8.284679 282.934387 8.600000
      vertex 8.602378 287.668396 8.600000
      vertex 7.792032 283.576416 8.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 6.402340 284.378754 8.600000
      vertex 7.150001 284.069061 8.600000
      vertex 7.300001 288.207855 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 6.181624 289.066010 8.600000
      vertex 6.402340 284.378754 8.600000
      vertex 7.300001 288.207855 8.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 5.600001 284.484406 8.600000
      vertex 6.402340 284.378754 8.600000
      vertex 6.181624 289.066010 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 5.323464 290.184387 8.600000
      vertex 5.600001 284.484406 8.600000
      vertex 6.181624 289.066010 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 1.100001 284.484406 8.600000
      vertex 5.600001 284.484406 8.600000
      vertex 5.323464 290.184387 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 4.784001 291.486786 8.600000
      vertex 1.100001 284.484406 8.600000
      vertex 5.323464 290.184387 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 4.600001 292.884399 8.600000
      vertex 1.100001 284.484406 8.600000
      vertex 4.784001 291.486786 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 1.100001 284.484406 8.600000
      vertex 4.600001 292.884399 8.600000
      vertex 4.600001 327.884399 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 1.100001 336.284393 8.600000
      vertex 1.100001 284.484406 8.600000
      vertex 4.600001 327.884399 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 4.784001 329.282013 8.600000
      vertex 1.100001 336.284393 8.600000
      vertex 4.600001 327.884399 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 5.323464 330.584381 8.600000
      vertex 1.100001 336.284393 8.600000
      vertex 4.784001 329.282013 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 5.600001 336.284393 8.600000
      vertex 1.100001 336.284393 8.600000
      vertex 5.323464 330.584381 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 6.181624 331.702759 8.600000
      vertex 5.600001 336.284393 8.600000
      vertex 5.323464 330.584381 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 6.402340 336.390015 8.600000
      vertex 5.600001 336.284393 8.600000
      vertex 6.181624 331.702759 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 7.300001 332.560944 8.600000
      vertex 6.402340 336.390015 8.600000
      vertex 6.181624 331.702759 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 7.150001 336.699707 8.600000
      vertex 6.402340 336.390015 8.600000
      vertex 7.300001 332.560944 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 8.602378 333.100403 8.600000
      vertex 7.150001 336.699707 8.600000
      vertex 7.300001 332.560944 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 7.792032 337.192352 8.600000
      vertex 7.150001 336.699707 8.600000
      vertex 8.602378 333.100403 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 8.284679 337.834381 8.600000
      vertex 7.792032 337.192352 8.600000
      vertex 8.602378 333.100403 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 10.000001 333.284393 8.600000
      vertex 8.284679 337.834381 8.600000
      vertex 8.602378 333.100403 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 8.594371 338.582062 8.600000
      vertex 8.284679 337.834381 8.600000
      vertex 10.000001 333.284393 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 8.700001 339.384399 8.600000
      vertex 8.594371 338.582062 8.600000
      vertex 10.000001 333.284393 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 25.500002 339.384399 8.600000
      vertex 8.700001 339.384399 8.600000
      vertex 10.000001 333.284393 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 8.700001 344.884399 8.600000
      vertex 8.700001 339.384399 8.600000
      vertex 25.500002 339.384399 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 25.500002 344.884399 8.600000
      vertex 8.700001 344.884399 8.600000
      vertex 25.500002 339.384399 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 10.000001 333.284393 8.600000
      vertex 31.200001 333.284393 8.600000
      vertex 27.050001 336.699707 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 26.407970 337.192352 8.600000
      vertex 10.000001 333.284393 8.600000
      vertex 27.050001 336.699707 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 25.915321 337.834381 8.600000
      vertex 10.000001 333.284393 8.600000
      vertex 26.407970 337.192352 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 10.000001 333.284393 8.600000
      vertex 25.915321 337.834381 8.600000
      vertex 25.605631 338.582062 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 25.500002 339.384399 8.600000
      vertex 10.000001 333.284393 8.600000
      vertex 25.605631 338.582062 8.600000
    endloop
  endfacet
  facet normal 0.130516 -0.991446 0.000000
    outer loop
      vertex 6.402340 336.390015 11.600000
      vertex 5.600001 336.284393 11.600000
      vertex 5.600001 336.284393 8.600000
    endloop
  endfacet
  facet normal 0.130516 -0.991446 0.000000
    outer loop
      vertex 6.402340 336.390015 8.600000
      vertex 6.402340 336.390015 11.600000
      vertex 5.600001 336.284393 8.600000
    endloop
  endfacet
  facet normal 0.382684 -0.923879 0.000000
    outer loop
      vertex 7.150001 336.699707 11.600000
      vertex 6.402340 336.390015 11.600000
      vertex 6.402340 336.390015 8.600000
    endloop
  endfacet
  facet normal 0.382684 -0.923879 0.000000
    outer loop
      vertex 7.150001 336.699707 8.600000
      vertex 7.150001 336.699707 11.600000
      vertex 6.402340 336.390015 8.600000
    endloop
  endfacet
  facet normal 0.608759 -0.793355 0.000000
    outer loop
      vertex 7.792032 337.192352 11.600000
      vertex 7.150001 336.699707 11.600000
      vertex 7.150001 336.699707 8.600000
    endloop
  endfacet
  facet normal 0.608759 -0.793355 0.000000
    outer loop
      vertex 7.792032 337.192352 8.600000
      vertex 7.792032 337.192352 11.600000
      vertex 7.150001 336.699707 8.600000
    endloop
  endfacet
  facet normal 0.793353 -0.608762 0.000000
    outer loop
      vertex 8.284679 337.834381 11.600000
      vertex 7.792032 337.192352 11.600000
      vertex 7.792032 337.192352 8.600000
    endloop
  endfacet
  facet normal 0.793353 -0.608762 0.000000
    outer loop
      vertex 8.284679 337.834381 8.600000
      vertex 8.284679 337.834381 11.600000
      vertex 7.792032 337.192352 8.600000
    endloop
  endfacet
  facet normal 0.923883 -0.382675 0.000000
    outer loop
      vertex 8.594371 338.582062 11.600000
      vertex 8.284679 337.834381 11.600000
      vertex 8.284679 337.834381 8.600000
    endloop
  endfacet
  facet normal 0.923883 -0.382675 0.000000
    outer loop
      vertex 8.594371 338.582062 8.600000
      vertex 8.594371 338.582062 11.600000
      vertex 8.284679 337.834381 8.600000
    endloop
  endfacet
  facet normal 0.991445 -0.130526 0.000000
    outer loop
      vertex 8.700001 339.384399 11.600000
      vertex 8.594371 338.582062 11.600000
      vertex 8.594371 338.582062 8.600000
    endloop
  endfacet
  facet normal 0.991445 -0.130526 0.000000
    outer loop
      vertex 8.700001 339.384399 8.600000
      vertex 8.700001 339.384399 11.600000
      vertex 8.594371 338.582062 8.600000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 8.700001 339.384399 8.600000
      vertex 8.700001 344.884399 8.600000
      vertex 8.700001 344.884399 11.600000
    endloop
  endfacet
  facet normal 1.000000 -0.000000 0.000000
    outer loop
      vertex 8.700001 339.384399 11.600000
      vertex 8.700001 339.384399 8.600000
      vertex 8.700001 344.884399 11.600000
    endloop
  endfacet
  facet normal 0.000000 -1.000000 -0.000000
    outer loop
      vertex 23.600000 344.884399 21.000000
      vertex 23.463705 344.884399 19.964724
      vertex 38.000000 344.884399 11.600000
    endloop
  endfacet
  facet normal 0.000000 -1.000000 -0.000000
    outer loop
      vertex 38.000000 344.884399 33.599998
      vertex 23.600000 344.884399 21.000000
      vertex 38.000000 344.884399 11.600000
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 23.463705 344.884399 22.035276
      vertex 23.600000 344.884399 21.000000
      vertex 38.000000 344.884399 33.599998
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 23.064102 344.884399 23.000000
      vertex 23.463705 344.884399 22.035276
      vertex 38.000000 344.884399 33.599998
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 22.428429 344.884399 23.828426
      vertex 23.064102 344.884399 23.000000
      vertex 38.000000 344.884399 33.599998
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 21.600000 344.884399 24.464102
      vertex 22.428429 344.884399 23.828426
      vertex 38.000000 344.884399 33.599998
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 20.635277 344.884399 24.863703
      vertex 21.600000 344.884399 24.464102
      vertex 38.000000 344.884399 33.599998
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 19.600000 344.884399 25.000000
      vertex 20.635277 344.884399 24.863703
      vertex 38.000000 344.884399 33.599998
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 3.200001 344.884399 33.599998
      vertex 19.600000 344.884399 25.000000
      vertex 38.000000 344.884399 33.599998
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 18.564724 344.884399 24.863703
      vertex 19.600000 344.884399 25.000000
      vertex 3.200001 344.884399 33.599998
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 17.600000 344.884399 24.464102
      vertex 18.564724 344.884399 24.863703
      vertex 3.200001 344.884399 33.599998
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 16.771574 344.884399 23.828426
      vertex 17.600000 344.884399 24.464102
      vertex 3.200001 344.884399 33.599998
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 16.135899 344.884399 23.000000
      vertex 16.771574 344.884399 23.828426
      vertex 3.200001 344.884399 33.599998
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 15.736298 344.884399 22.035276
      vertex 16.135899 344.884399 23.000000
      vertex 3.200001 344.884399 33.599998
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 15.600001 344.884399 21.000000
      vertex 15.736298 344.884399 22.035276
      vertex 3.200001 344.884399 33.599998
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 3.200001 344.884399 11.600000
      vertex 15.600001 344.884399 21.000000
      vertex 3.200001 344.884399 33.599998
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 8.700001 344.884399 11.600000
      vertex 15.600001 344.884399 21.000000
      vertex 3.200001 344.884399 11.600000
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 25.500002 344.884399 11.600000
      vertex 38.000000 344.884399 11.600000
      vertex 23.463705 344.884399 19.964724
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 23.064102 344.884399 19.000000
      vertex 25.500002 344.884399 11.600000
      vertex 23.463705 344.884399 19.964724
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 22.428429 344.884399 18.171574
      vertex 25.500002 344.884399 11.600000
      vertex 23.064102 344.884399 19.000000
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 25.500002 344.884399 11.600000
      vertex 22.428429 344.884399 18.171574
      vertex 21.600000 344.884399 17.535898
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 20.635277 344.884399 17.136297
      vertex 25.500002 344.884399 11.600000
      vertex 21.600000 344.884399 17.535898
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 19.600000 344.884399 17.000000
      vertex 25.500002 344.884399 11.600000
      vertex 20.635277 344.884399 17.136297
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 25.500002 344.884399 8.600000
      vertex 25.500002 344.884399 11.600000
      vertex 19.600000 344.884399 17.000000
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 18.564724 344.884399 17.136297
      vertex 25.500002 344.884399 8.600000
      vertex 19.600000 344.884399 17.000000
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 8.700001 344.884399 8.600000
      vertex 25.500002 344.884399 8.600000
      vertex 18.564724 344.884399 17.136297
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 8.700001 344.884399 11.600000
      vertex 8.700001 344.884399 8.600000
      vertex 18.564724 344.884399 17.136297
    endloop
  endfacet
  facet normal 0.000000 -1.000000 -0.000000
    outer loop
      vertex 17.600000 344.884399 17.535898
      vertex 8.700001 344.884399 11.600000
      vertex 18.564724 344.884399 17.136297
    endloop
  endfacet
  facet normal 0.000000 -1.000000 -0.000000
    outer loop
      vertex 16.771574 344.884399 18.171574
      vertex 8.700001 344.884399 11.600000
      vertex 17.600000 344.884399 17.535898
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 8.700001 344.884399 11.600000
      vertex 16.771574 344.884399 18.171574
      vertex 16.135899 344.884399 19.000000
    endloop
  endfacet
  facet normal 0.000000 -1.000000 -0.000000
    outer loop
      vertex 15.736298 344.884399 19.964724
      vertex 8.700001 344.884399 11.600000
      vertex 16.135899 344.884399 19.000000
    endloop
  endfacet
  facet normal 0.000000 -1.000000 -0.000000
    outer loop
      vertex 15.600001 344.884399 21.000000
      vertex 8.700001 344.884399 11.600000
      vertex 15.736298 344.884399 19.964724
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 25.500002 344.884399 8.600000
      vertex 25.500002 339.384399 8.600000
      vertex 25.500002 339.384399 11.600000
    endloop
  endfacet
  facet normal -1.000000 -0.000000 -0.000000
    outer loop
      vertex 25.500002 344.884399 11.600000
      vertex 25.500002 344.884399 8.600000
      vertex 25.500002 339.384399 11.600000
    endloop
  endfacet
  facet normal -0.991445 -0.130525 0.000000
    outer loop
      vertex 25.605631 338.582062 11.600000
      vertex 25.500002 339.384399 11.600000
      vertex 25.500002 339.384399 8.600000
    endloop
  endfacet
  facet normal -0.991445 -0.130525 0.000000
    outer loop
      vertex 25.605631 338.582062 8.600000
      vertex 25.605631 338.582062 11.600000
      vertex 25.500002 339.384399 8.600000
    endloop
  endfacet
  facet normal -0.923883 -0.382674 0.000000
    outer loop
      vertex 25.915321 337.834381 11.600000
      vertex 25.605631 338.582062 11.600000
      vertex 25.605631 338.582062 8.600000
    endloop
  endfacet
  facet normal -0.923883 -0.382674 0.000000
    outer loop
      vertex 25.915321 337.834381 8.600000
      vertex 25.915321 337.834381 11.600000
      vertex 25.605631 338.582062 8.600000
    endloop
  endfacet
  facet normal -0.793351 -0.608764 0.000000
    outer loop
      vertex 26.407970 337.192352 11.600000
      vertex 25.915321 337.834381 11.600000
      vertex 25.915321 337.834381 8.600000
    endloop
  endfacet
  facet normal -0.793351 -0.608764 0.000000
    outer loop
      vertex 26.407970 337.192352 8.600000
      vertex 26.407970 337.192352 11.600000
      vertex 25.915321 337.834381 8.600000
    endloop
  endfacet
  facet normal -0.608760 -0.793355 0.000000
    outer loop
      vertex 27.050001 336.699707 11.600000
      vertex 26.407970 337.192352 11.600000
      vertex 26.407970 337.192352 8.600000
    endloop
  endfacet
  facet normal -0.608760 -0.793355 0.000000
    outer loop
      vertex 27.050001 336.699707 8.600000
      vertex 27.050001 336.699707 11.600000
      vertex 26.407970 337.192352 8.600000
    endloop
  endfacet
  facet normal -0.382684 -0.923879 0.000000
    outer loop
      vertex 27.797663 336.390015 11.600000
      vertex 27.050001 336.699707 11.600000
      vertex 27.050001 336.699707 8.600000
    endloop
  endfacet
  facet normal -0.382684 -0.923879 0.000000
    outer loop
      vertex 27.797663 336.390015 8.600000
      vertex 27.797663 336.390015 11.600000
      vertex 27.050001 336.699707 8.600000
    endloop
  endfacet
  facet normal -0.130516 -0.991446 0.000000
    outer loop
      vertex 28.600000 336.284393 11.600000
      vertex 27.797663 336.390015 11.600000
      vertex 27.797663 336.390015 8.600000
    endloop
  endfacet
  facet normal -0.130516 -0.991446 0.000000
    outer loop
      vertex 28.600000 336.284393 8.600000
      vertex 28.600000 336.284393 11.600000
      vertex 27.797663 336.390015 8.600000
    endloop
  endfacet
  facet normal -0.000000 -1.000000 0.000000
    outer loop
      vertex 33.200001 336.284393 10.500000
      vertex 28.600000 336.284393 11.600000
      vertex 28.600000 336.284393 8.600000
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 39.600002 336.284393 8.600000
      vertex 33.200001 336.284393 10.500000
      vertex 28.600000 336.284393 8.600000
    endloop
  endfacet
  facet normal -0.000000 -1.000000 -0.000000
    outer loop
      vertex 39.600002 336.284393 10.500000
      vertex 33.200001 336.284393 10.500000
      vertex 39.600002 336.284393 8.600000
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 28.600000 336.284393 11.600000
      vertex 33.200001 336.284393 10.500000
      vertex 33.200001 336.284393 11.600000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 276.484406 11.600000
      vertex 39.600002 287.484406 25.200001
      vertex 39.600002 287.484406 17.000000
    endloop
  endfacet
  facet normal -1.000000 -0.000000 0.000000
    outer loop
      vertex 39.600002 287.668396 15.602377
      vertex 39.600002 276.484406 11.600000
      vertex 39.600002 287.484406 17.000000
    endloop
  endfacet
  facet normal -1.000000 -0.000000 0.000000
    outer loop
      vertex 39.600002 288.207855 14.300000
      vertex 39.600002 276.484406 11.600000
      vertex 39.600002 287.668396 15.602377
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 284.484406 11.600000
      vertex 39.600002 276.484406 11.600000
      vertex 39.600002 288.207855 14.300000
    endloop
  endfacet
  facet normal -1.000000 -0.000000 0.000000
    outer loop
      vertex 39.600002 289.066010 13.181623
      vertex 39.600002 284.484406 11.600000
      vertex 39.600002 288.207855 14.300000
    endloop
  endfacet
  facet normal -1.000000 -0.000000 0.000000
    outer loop
      vertex 39.600002 290.184387 12.323462
      vertex 39.600002 284.484406 11.600000
      vertex 39.600002 289.066010 13.181623
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 284.484406 11.600000
      vertex 39.600002 290.184387 12.323462
      vertex 39.600002 291.486786 11.784000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 284.484406 8.600000
      vertex 39.600002 284.484406 11.600000
      vertex 39.600002 291.486786 11.784000
    endloop
  endfacet
  facet normal -1.000000 -0.000000 0.000000
    outer loop
      vertex 39.600002 292.884399 11.600000
      vertex 39.600002 284.484406 8.600000
      vertex 39.600002 291.486786 11.784000
    endloop
  endfacet
  facet normal -1.000000 -0.000000 0.000000
    outer loop
      vertex 39.600002 304.984406 11.600000
      vertex 39.600002 284.484406 8.600000
      vertex 39.600002 292.884399 11.600000
    endloop
  endfacet
  facet normal -1.000000 -0.000000 0.000000
    outer loop
      vertex 39.600002 326.940277 10.525556
      vertex 39.600002 284.484406 8.600000
      vertex 39.600002 304.984406 11.600000
    endloop
  endfacet
  facet normal -1.000000 0.000000 -0.000000
    outer loop
      vertex 39.600002 306.382019 11.784000
      vertex 39.600002 326.940277 10.525556
      vertex 39.600002 304.984406 11.600000
    endloop
  endfacet
  facet normal -1.000000 -0.000000 -0.000000
    outer loop
      vertex 39.600002 326.759399 10.600481
      vertex 39.600002 326.940277 10.525556
      vertex 39.600002 306.382019 11.784000
    endloop
  endfacet
  facet normal -1.000000 -0.000000 -0.000000
    outer loop
      vertex 39.600002 326.604065 10.719670
      vertex 39.600002 326.759399 10.600481
      vertex 39.600002 306.382019 11.784000
    endloop
  endfacet
  facet normal -1.000000 0.000000 -0.000000
    outer loop
      vertex 39.600002 307.684387 12.323462
      vertex 39.600002 326.604065 10.719670
      vertex 39.600002 306.382019 11.784000
    endloop
  endfacet
  facet normal -1.000000 -0.000000 -0.000000
    outer loop
      vertex 39.600002 326.484863 10.875000
      vertex 39.600002 326.604065 10.719670
      vertex 39.600002 307.684387 12.323462
    endloop
  endfacet
  facet normal -1.000000 -0.000000 -0.000000
    outer loop
      vertex 39.600002 326.409943 11.055885
      vertex 39.600002 326.484863 10.875000
      vertex 39.600002 307.684387 12.323462
    endloop
  endfacet
  facet normal -1.000000 -0.000000 -0.000000
    outer loop
      vertex 39.600002 326.384399 11.250000
      vertex 39.600002 326.409943 11.055885
      vertex 39.600002 307.684387 12.323462
    endloop
  endfacet
  facet normal -1.000000 0.000000 -0.000000
    outer loop
      vertex 39.600002 308.802765 13.181623
      vertex 39.600002 326.384399 11.250000
      vertex 39.600002 307.684387 12.323462
    endloop
  endfacet
  facet normal -1.000000 0.000000 -0.000000
    outer loop
      vertex 39.600002 309.660919 14.300000
      vertex 39.600002 326.384399 11.250000
      vertex 39.600002 308.802765 13.181623
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 326.384399 11.250000
      vertex 39.600002 309.660919 14.300000
      vertex 39.600002 310.200409 15.602377
    endloop
  endfacet
  facet normal -1.000000 0.000000 -0.000000
    outer loop
      vertex 39.600002 326.384399 17.450001
      vertex 39.600002 326.384399 11.250000
      vertex 39.600002 310.200409 15.602377
    endloop
  endfacet
  facet normal -1.000000 0.000000 -0.000000
    outer loop
      vertex 39.600002 310.384399 17.000000
      vertex 39.600002 326.384399 17.450001
      vertex 39.600002 310.200409 15.602377
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 326.409943 17.644114
      vertex 39.600002 326.384399 17.450001
      vertex 39.600002 310.384399 17.000000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 326.484863 17.825001
      vertex 39.600002 326.409943 17.644114
      vertex 39.600002 310.384399 17.000000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 326.604065 17.980330
      vertex 39.600002 326.484863 17.825001
      vertex 39.600002 310.384399 17.000000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 326.759399 18.099520
      vertex 39.600002 326.604065 17.980330
      vertex 39.600002 310.384399 17.000000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 310.384399 25.200001
      vertex 39.600002 326.759399 18.099520
      vertex 39.600002 310.384399 17.000000
    endloop
  endfacet
  facet normal -1.000000 -0.000000 0.000000
    outer loop
      vertex 39.600002 326.940277 18.174444
      vertex 39.600002 326.759399 18.099520
      vertex 39.600002 310.384399 25.200001
    endloop
  endfacet
  facet normal -1.000000 -0.000000 0.000000
    outer loop
      vertex 39.600002 327.134399 18.200001
      vertex 39.600002 326.940277 18.174444
      vertex 39.600002 310.384399 25.200001
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 343.284393 33.599998
      vertex 39.600002 327.134399 18.200001
      vertex 39.600002 310.384399 25.200001
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 337.134399 18.200001
      vertex 39.600002 327.134399 18.200001
      vertex 39.600002 343.284393 33.599998
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 337.328522 18.174444
      vertex 39.600002 337.134399 18.200001
      vertex 39.600002 343.284393 33.599998
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 337.509399 18.099520
      vertex 39.600002 337.328522 18.174444
      vertex 39.600002 343.284393 33.599998
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 337.664734 17.980330
      vertex 39.600002 337.509399 18.099520
      vertex 39.600002 343.284393 33.599998
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 337.783905 17.825001
      vertex 39.600002 337.664734 17.980330
      vertex 39.600002 343.284393 33.599998
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 343.284393 11.600000
      vertex 39.600002 337.783905 17.825001
      vertex 39.600002 343.284393 33.599998
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 337.858826 17.644114
      vertex 39.600002 337.783905 17.825001
      vertex 39.600002 343.284393 11.600000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 337.884399 17.450001
      vertex 39.600002 337.858826 17.644114
      vertex 39.600002 343.284393 11.600000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 337.884399 11.600000
      vertex 39.600002 337.884399 17.450001
      vertex 39.600002 343.284393 11.600000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 343.284393 33.599998
      vertex 39.600002 310.384399 25.200001
      vertex 39.600002 310.200409 26.597622
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 309.660919 27.900000
      vertex 39.600002 343.284393 33.599998
      vertex 39.600002 310.200409 26.597622
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 308.802765 29.018377
      vertex 39.600002 343.284393 33.599998
      vertex 39.600002 309.660919 27.900000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 343.284393 33.599998
      vertex 39.600002 308.802765 29.018377
      vertex 39.600002 307.684387 29.876537
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 306.382019 30.416000
      vertex 39.600002 343.284393 33.599998
      vertex 39.600002 307.684387 29.876537
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 304.984406 30.600000
      vertex 39.600002 343.284393 33.599998
      vertex 39.600002 306.382019 30.416000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 276.484406 33.599998
      vertex 39.600002 343.284393 33.599998
      vertex 39.600002 304.984406 30.600000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 292.884399 30.600000
      vertex 39.600002 276.484406 33.599998
      vertex 39.600002 304.984406 30.600000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 291.486786 30.416000
      vertex 39.600002 276.484406 33.599998
      vertex 39.600002 292.884399 30.600000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 276.484406 33.599998
      vertex 39.600002 291.486786 30.416000
      vertex 39.600002 290.184387 29.876537
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 289.066010 29.018377
      vertex 39.600002 276.484406 33.599998
      vertex 39.600002 290.184387 29.876537
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 288.207855 27.900000
      vertex 39.600002 276.484406 33.599998
      vertex 39.600002 289.066010 29.018377
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 276.484406 33.599998
      vertex 39.600002 288.207855 27.900000
      vertex 39.600002 287.668396 26.597622
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 287.484406 25.200001
      vertex 39.600002 276.484406 33.599998
      vertex 39.600002 287.668396 26.597622
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 276.484406 11.600000
      vertex 39.600002 276.484406 33.599998
      vertex 39.600002 287.484406 25.200001
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 39.600002 336.284393 8.600000
      vertex 39.600002 284.484406 8.600000
      vertex 39.600002 326.940277 10.525556
    endloop
  endfacet
  facet normal -1.000000 -0.000000 -0.000000
    outer loop
      vertex 39.600002 327.134399 10.500000
      vertex 39.600002 336.284393 8.600000
      vertex 39.600002 326.940277 10.525556
    endloop
  endfacet
  facet normal -1.000000 -0.000000 -0.000000
    outer loop
      vertex 39.600002 336.284393 10.500000
      vertex 39.600002 336.284393 8.600000
      vertex 39.600002 327.134399 10.500000
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 39.600002 284.484406 8.600000
      vertex 28.600000 284.484406 8.600000
      vertex 28.600000 284.484406 11.600000
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 39.600002 284.484406 11.600000
      vertex 39.600002 284.484406 8.600000
      vertex 28.600000 284.484406 11.600000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 1.600001 343.284393 33.599998
      vertex 1.600001 336.284393 33.599998
      vertex 1.600001 336.284393 11.600000
    endloop
  endfacet
  facet normal 1.000000 0.000000 -0.000000
    outer loop
      vertex 1.600001 343.284393 11.600000
      vertex 1.600001 343.284393 33.599998
      vertex 1.600001 336.284393 11.600000
    endloop
  endfacet
  facet normal -0.000000 1.000000 0.000000
    outer loop
      vertex 22.200001 274.884399 11.600000
      vertex 25.500002 274.884399 11.600000
      vertex 25.500002 274.884399 8.600000
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 8.700001 274.884399 8.600000
      vertex 22.200001 274.884399 11.600000
      vertex 25.500002 274.884399 8.600000
    endloop
  endfacet
  facet normal -0.000000 1.000000 0.000000
    outer loop
      vertex 8.700001 274.884399 11.600000
      vertex 22.200001 274.884399 11.600000
      vertex 8.700001 274.884399 8.600000
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 25.500002 274.884399 11.600000
      vertex 22.200001 274.884399 11.600000
      vertex 22.200001 274.884399 17.700001
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 38.000000 274.884399 11.600000
      vertex 25.500002 274.884399 11.600000
      vertex 22.200001 274.884399 17.700001
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 21.961481 274.884399 19.511734
      vertex 38.000000 274.884399 11.600000
      vertex 22.200001 274.884399 17.700001
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 38.000000 274.884399 33.599998
      vertex 38.000000 274.884399 11.600000
      vertex 21.961481 274.884399 19.511734
    endloop
  endfacet
  facet normal -0.000000 1.000000 0.000000
    outer loop
      vertex 21.262178 274.884399 21.200001
      vertex 38.000000 274.884399 33.599998
      vertex 21.961481 274.884399 19.511734
    endloop
  endfacet
  facet normal -0.000000 1.000000 0.000000
    outer loop
      vertex 20.149748 274.884399 22.649748
      vertex 38.000000 274.884399 33.599998
      vertex 21.262178 274.884399 21.200001
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 38.000000 274.884399 33.599998
      vertex 20.149748 274.884399 22.649748
      vertex 18.700001 274.884399 23.762178
    endloop
  endfacet
  facet normal -0.000000 1.000000 0.000000
    outer loop
      vertex 17.011734 274.884399 24.461481
      vertex 38.000000 274.884399 33.599998
      vertex 18.700001 274.884399 23.762178
    endloop
  endfacet
  facet normal -0.000000 1.000000 0.000000
    outer loop
      vertex 3.200001 274.884399 33.599998
      vertex 38.000000 274.884399 33.599998
      vertex 17.011734 274.884399 24.461481
    endloop
  endfacet
  facet normal -0.000000 1.000000 -0.000000
    outer loop
      vertex 15.200001 274.884399 24.700001
      vertex 3.200001 274.884399 33.599998
      vertex 17.011734 274.884399 24.461481
    endloop
  endfacet
  facet normal 0.000000 1.000000 -0.000000
    outer loop
      vertex 13.388268 274.884399 24.461481
      vertex 3.200001 274.884399 33.599998
      vertex 15.200001 274.884399 24.700001
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 3.200001 274.884399 33.599998
      vertex 13.388268 274.884399 24.461481
      vertex 11.700001 274.884399 23.762178
    endloop
  endfacet
  facet normal 0.000000 1.000000 -0.000000
    outer loop
      vertex 10.250254 274.884399 22.649748
      vertex 3.200001 274.884399 33.599998
      vertex 11.700001 274.884399 23.762178
    endloop
  endfacet
  facet normal 0.000000 1.000000 -0.000000
    outer loop
      vertex 9.137823 274.884399 21.200001
      vertex 3.200001 274.884399 33.599998
      vertex 10.250254 274.884399 22.649748
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 3.200001 274.884399 33.599998
      vertex 9.137823 274.884399 21.200001
      vertex 8.438520 274.884399 19.511734
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 3.200001 274.884399 11.600000
      vertex 3.200001 274.884399 33.599998
      vertex 8.438520 274.884399 19.511734
    endloop
  endfacet
  facet normal 0.000000 1.000000 -0.000000
    outer loop
      vertex 8.200001 274.884399 17.700001
      vertex 3.200001 274.884399 11.600000
      vertex 8.438520 274.884399 19.511734
    endloop
  endfacet
  facet normal 0.000000 1.000000 -0.000000
    outer loop
      vertex 8.200001 274.884399 11.600000
      vertex 3.200001 274.884399 11.600000
      vertex 8.200001 274.884399 17.700001
    endloop
  endfacet
  facet normal 0.000000 -0.991433 -0.130618
    outer loop
      vertex 39.600002 337.858826 17.644114
      vertex 39.600002 337.884399 17.450001
      vertex 41.200001 337.884399 17.450001
    endloop
  endfacet
  facet normal -0.000000 -0.991433 -0.130618
    outer loop
      vertex 41.200001 337.858826 17.644114
      vertex 39.600002 337.858826 17.644114
      vertex 41.200001 337.884399 17.450001
    endloop
  endfacet
  facet normal 0.000000 -0.923889 -0.382660
    outer loop
      vertex 39.600002 337.783905 17.825001
      vertex 39.600002 337.858826 17.644114
      vertex 41.200001 337.858826 17.644114
    endloop
  endfacet
  facet normal -0.000000 -0.923889 -0.382660
    outer loop
      vertex 41.200001 337.783905 17.825001
      vertex 39.600002 337.783905 17.825001
      vertex 41.200001 337.858826 17.644114
    endloop
  endfacet
  facet normal 0.000000 -0.793395 -0.608707
    outer loop
      vertex 39.600002 337.664734 17.980330
      vertex 39.600002 337.783905 17.825001
      vertex 41.200001 337.783905 17.825001
    endloop
  endfacet
  facet normal -0.000000 -0.793395 -0.608707
    outer loop
      vertex 41.200001 337.664734 17.980330
      vertex 39.600002 337.664734 17.980330
      vertex 41.200001 337.783905 17.825001
    endloop
  endfacet
  facet normal 0.000000 -0.608755 -0.793359
    outer loop
      vertex 39.600002 337.509399 18.099520
      vertex 39.600002 337.664734 17.980330
      vertex 41.200001 337.664734 17.980330
    endloop
  endfacet
  facet normal -0.000000 -0.608755 -0.793359
    outer loop
      vertex 41.200001 337.509399 18.099520
      vertex 39.600002 337.509399 18.099520
      vertex 41.200001 337.664734 17.980330
    endloop
  endfacet
  facet normal 0.000000 -0.382694 -0.923875
    outer loop
      vertex 39.600002 337.328522 18.174444
      vertex 39.600002 337.509399 18.099520
      vertex 41.200001 337.509399 18.099520
    endloop
  endfacet
  facet normal -0.000000 -0.382694 -0.923875
    outer loop
      vertex 41.200001 337.328522 18.174444
      vertex 39.600002 337.328522 18.174444
      vertex 41.200001 337.509399 18.099520
    endloop
  endfacet
  facet normal 0.000000 -0.130526 -0.991445
    outer loop
      vertex 39.600002 337.134399 18.200001
      vertex 39.600002 337.328522 18.174444
      vertex 41.200001 337.328522 18.174444
    endloop
  endfacet
  facet normal -0.000000 -0.130526 -0.991445
    outer loop
      vertex 41.200001 337.134399 18.200001
      vertex 39.600002 337.134399 18.200001
      vertex 41.200001 337.328522 18.174444
    endloop
  endfacet
  facet normal -0.000000 -1.000000 0.000000
    outer loop
      vertex 41.200001 337.884399 17.450001
      vertex 39.600002 337.884399 17.450001
      vertex 39.600002 337.884399 11.600000
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 41.200001 337.884399 11.250000
      vertex 41.200001 337.884399 17.450001
      vertex 39.600002 337.884399 11.600000
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 33.200001 337.884399 11.250000
      vertex 41.200001 337.884399 11.250000
      vertex 39.600002 337.884399 11.600000
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 33.200001 337.884399 11.600000
      vertex 33.200001 337.884399 11.250000
      vertex 39.600002 337.884399 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.130521 0.991446
    outer loop
      vertex 33.200001 337.328522 10.525556
      vertex 33.200001 337.134399 10.500000
      vertex 41.200001 337.134399 10.500000
    endloop
  endfacet
  facet normal 0.000000 -0.130521 0.991446
    outer loop
      vertex 41.200001 337.328522 10.525556
      vertex 33.200001 337.328522 10.525556
      vertex 41.200001 337.134399 10.500000
    endloop
  endfacet
  facet normal 0.000000 -0.382698 0.923873
    outer loop
      vertex 33.200001 337.509399 10.600481
      vertex 33.200001 337.328522 10.525556
      vertex 41.200001 337.328522 10.525556
    endloop
  endfacet
  facet normal 0.000000 -0.382698 0.923873
    outer loop
      vertex 41.200001 337.509399 10.600481
      vertex 33.200001 337.509399 10.600481
      vertex 41.200001 337.328522 10.525556
    endloop
  endfacet
  facet normal 0.000000 -0.608752 0.793361
    outer loop
      vertex 33.200001 337.664734 10.719670
      vertex 33.200001 337.509399 10.600481
      vertex 41.200001 337.509399 10.600481
    endloop
  endfacet
  facet normal 0.000000 -0.608752 0.793361
    outer loop
      vertex 41.200001 337.664734 10.719670
      vertex 33.200001 337.664734 10.719670
      vertex 41.200001 337.509399 10.600481
    endloop
  endfacet
  facet normal 0.000000 -0.793397 0.608705
    outer loop
      vertex 33.200001 337.783905 10.875000
      vertex 33.200001 337.664734 10.719670
      vertex 41.200001 337.664734 10.719670
    endloop
  endfacet
  facet normal 0.000000 -0.793397 0.608705
    outer loop
      vertex 41.200001 337.783905 10.875000
      vertex 33.200001 337.783905 10.875000
      vertex 41.200001 337.664734 10.719670
    endloop
  endfacet
  facet normal 0.000000 -0.923888 0.382664
    outer loop
      vertex 33.200001 337.858826 11.055885
      vertex 33.200001 337.783905 10.875000
      vertex 41.200001 337.783905 10.875000
    endloop
  endfacet
  facet normal 0.000000 -0.923888 0.382664
    outer loop
      vertex 41.200001 337.858826 11.055885
      vertex 33.200001 337.858826 11.055885
      vertex 41.200001 337.783905 10.875000
    endloop
  endfacet
  facet normal 0.000000 -0.991433 0.130617
    outer loop
      vertex 33.200001 337.884399 11.250000
      vertex 33.200001 337.858826 11.055885
      vertex 41.200001 337.858826 11.055885
    endloop
  endfacet
  facet normal 0.000000 -0.991433 0.130617
    outer loop
      vertex 41.200001 337.884399 11.250000
      vertex 33.200001 337.884399 11.250000
      vertex 41.200001 337.858826 11.055885
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 39.600002 336.284393 10.500000
      vertex 41.200001 327.134399 10.500000
      vertex 41.200001 337.134399 10.500000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 33.200001 337.134399 10.500000
      vertex 39.600002 336.284393 10.500000
      vertex 41.200001 337.134399 10.500000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 33.200001 336.284393 10.500000
      vertex 39.600002 336.284393 10.500000
      vertex 33.200001 337.134399 10.500000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 41.200001 327.134399 10.500000
      vertex 39.600002 336.284393 10.500000
      vertex 39.600002 327.134399 10.500000
    endloop
  endfacet
  facet normal 0.000000 0.991453 0.130464
    outer loop
      vertex 39.600002 326.409943 11.055885
      vertex 39.600002 326.384399 11.250000
      vertex 41.200001 326.384399 11.250000
    endloop
  endfacet
  facet normal 0.000000 0.991453 0.130464
    outer loop
      vertex 41.200001 326.409943 11.055885
      vertex 39.600002 326.409943 11.055885
      vertex 41.200001 326.384399 11.250000
    endloop
  endfacet
  facet normal 0.000000 0.923888 0.382664
    outer loop
      vertex 39.600002 326.484863 10.875000
      vertex 39.600002 326.409943 11.055885
      vertex 41.200001 326.409943 11.055885
    endloop
  endfacet
  facet normal 0.000000 0.923888 0.382664
    outer loop
      vertex 41.200001 326.484863 10.875000
      vertex 39.600002 326.484863 10.875000
      vertex 41.200001 326.409943 11.055885
    endloop
  endfacet
  facet normal 0.000000 0.793321 0.608803
    outer loop
      vertex 39.600002 326.604065 10.719670
      vertex 39.600002 326.484863 10.875000
      vertex 41.200001 326.484863 10.875000
    endloop
  endfacet
  facet normal 0.000000 0.793321 0.608803
    outer loop
      vertex 41.200001 326.604065 10.719670
      vertex 39.600002 326.604065 10.719670
      vertex 41.200001 326.484863 10.875000
    endloop
  endfacet
  facet normal 0.000000 0.608752 0.793361
    outer loop
      vertex 39.600002 326.759399 10.600481
      vertex 39.600002 326.604065 10.719670
      vertex 41.200001 326.604065 10.719670
    endloop
  endfacet
  facet normal 0.000000 0.608752 0.793361
    outer loop
      vertex 41.200001 326.759399 10.600481
      vertex 39.600002 326.759399 10.600481
      vertex 41.200001 326.604065 10.719670
    endloop
  endfacet
  facet normal 0.000000 0.382698 0.923873
    outer loop
      vertex 39.600002 326.940277 10.525556
      vertex 39.600002 326.759399 10.600481
      vertex 41.200001 326.759399 10.600481
    endloop
  endfacet
  facet normal 0.000000 0.382698 0.923873
    outer loop
      vertex 41.200001 326.940277 10.525556
      vertex 39.600002 326.940277 10.525556
      vertex 41.200001 326.759399 10.600481
    endloop
  endfacet
  facet normal 0.000000 0.130521 0.991446
    outer loop
      vertex 39.600002 327.134399 10.500000
      vertex 39.600002 326.940277 10.525556
      vertex 41.200001 326.940277 10.525556
    endloop
  endfacet
  facet normal 0.000000 0.130521 0.991446
    outer loop
      vertex 41.200001 327.134399 10.500000
      vertex 39.600002 327.134399 10.500000
      vertex 41.200001 326.940277 10.525556
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 41.200001 326.384399 11.250000
      vertex 39.600002 326.384399 11.250000
      vertex 39.600002 326.384399 17.450001
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 41.200001 326.384399 17.450001
      vertex 41.200001 326.384399 11.250000
      vertex 39.600002 326.384399 17.450001
    endloop
  endfacet
  facet normal 0.000000 0.991453 -0.130465
    outer loop
      vertex 41.200001 326.409943 17.644114
      vertex 41.200001 326.384399 17.450001
      vertex 39.600002 326.384399 17.450001
    endloop
  endfacet
  facet normal 0.000000 0.991453 -0.130465
    outer loop
      vertex 39.600002 326.409943 17.644114
      vertex 41.200001 326.409943 17.644114
      vertex 39.600002 326.384399 17.450001
    endloop
  endfacet
  facet normal 0.000000 0.923889 -0.382660
    outer loop
      vertex 41.200001 326.484863 17.825001
      vertex 41.200001 326.409943 17.644114
      vertex 39.600002 326.409943 17.644114
    endloop
  endfacet
  facet normal 0.000000 0.923889 -0.382660
    outer loop
      vertex 39.600002 326.484863 17.825001
      vertex 41.200001 326.484863 17.825001
      vertex 39.600002 326.409943 17.644114
    endloop
  endfacet
  facet normal 0.000000 0.793319 -0.608805
    outer loop
      vertex 41.200001 326.604065 17.980330
      vertex 41.200001 326.484863 17.825001
      vertex 39.600002 326.484863 17.825001
    endloop
  endfacet
  facet normal 0.000000 0.793319 -0.608805
    outer loop
      vertex 39.600002 326.604065 17.980330
      vertex 41.200001 326.604065 17.980330
      vertex 39.600002 326.484863 17.825001
    endloop
  endfacet
  facet normal 0.000000 0.608755 -0.793359
    outer loop
      vertex 41.200001 326.759399 18.099520
      vertex 41.200001 326.604065 17.980330
      vertex 39.600002 326.604065 17.980330
    endloop
  endfacet
  facet normal 0.000000 0.608755 -0.793359
    outer loop
      vertex 39.600002 326.759399 18.099520
      vertex 41.200001 326.759399 18.099520
      vertex 39.600002 326.604065 17.980330
    endloop
  endfacet
  facet normal 0.000000 0.382694 -0.923875
    outer loop
      vertex 41.200001 326.940277 18.174444
      vertex 41.200001 326.759399 18.099520
      vertex 39.600002 326.759399 18.099520
    endloop
  endfacet
  facet normal 0.000000 0.382694 -0.923875
    outer loop
      vertex 39.600002 326.940277 18.174444
      vertex 41.200001 326.940277 18.174444
      vertex 39.600002 326.759399 18.099520
    endloop
  endfacet
  facet normal 0.000000 0.130526 -0.991445
    outer loop
      vertex 41.200001 327.134399 18.200001
      vertex 41.200001 326.940277 18.174444
      vertex 39.600002 326.940277 18.174444
    endloop
  endfacet
  facet normal 0.000000 0.130526 -0.991445
    outer loop
      vertex 39.600002 327.134399 18.200001
      vertex 41.200001 327.134399 18.200001
      vertex 39.600002 326.940277 18.174444
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 39.600002 327.134399 18.200001
      vertex 39.600002 337.134399 18.200001
      vertex 41.200001 337.134399 18.200001
    endloop
  endfacet
  facet normal 0.000000 0.000000 -1.000000
    outer loop
      vertex 41.200001 327.134399 18.200001
      vertex 39.600002 327.134399 18.200001
      vertex 41.200001 337.134399 18.200001
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 33.200001 336.284393 11.600000
      vertex 33.200001 336.284393 10.500000
      vertex 33.200001 337.134399 10.500000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 33.200001 337.328522 10.525556
      vertex 33.200001 336.284393 11.600000
      vertex 33.200001 337.134399 10.500000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 33.200001 337.509399 10.600481
      vertex 33.200001 336.284393 11.600000
      vertex 33.200001 337.328522 10.525556
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 33.200001 336.284393 11.600000
      vertex 33.200001 337.509399 10.600481
      vertex 33.200001 337.664734 10.719670
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 33.200001 337.783905 10.875000
      vertex 33.200001 336.284393 11.600000
      vertex 33.200001 337.664734 10.719670
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 33.200001 337.858826 11.055885
      vertex 33.200001 336.284393 11.600000
      vertex 33.200001 337.783905 10.875000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 33.200001 336.284393 11.600000
      vertex 33.200001 337.858826 11.055885
      vertex 33.200001 337.884399 11.250000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 33.200001 337.884399 11.600000
      vertex 33.200001 336.284393 11.600000
      vertex 33.200001 337.884399 11.250000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 8.200001 274.884399 17.700001
      vertex 8.200001 273.284393 17.700001
      vertex 8.200001 273.284393 11.600000
    endloop
  endfacet
  facet normal 1.000000 0.000000 -0.000000
    outer loop
      vertex 8.200001 274.884399 11.600000
      vertex 8.200001 274.884399 17.700001
      vertex 8.200001 273.284393 11.600000
    endloop
  endfacet
  facet normal 0.991445 0.000000 -0.130526
    outer loop
      vertex 8.438520 273.284393 19.511734
      vertex 8.200001 273.284393 17.700001
      vertex 8.200001 274.884399 17.700001
    endloop
  endfacet
  facet normal 0.991445 0.000000 -0.130526
    outer loop
      vertex 8.438520 274.884399 19.511734
      vertex 8.438520 273.284393 19.511734
      vertex 8.200001 274.884399 17.700001
    endloop
  endfacet
  facet normal 0.923880 0.000000 -0.382683
    outer loop
      vertex 9.137823 273.284393 21.200001
      vertex 8.438520 273.284393 19.511734
      vertex 8.438520 274.884399 19.511734
    endloop
  endfacet
  facet normal 0.923880 0.000000 -0.382683
    outer loop
      vertex 9.137823 274.884399 21.200001
      vertex 9.137823 273.284393 21.200001
      vertex 8.438520 274.884399 19.511734
    endloop
  endfacet
  facet normal 0.793353 0.000000 -0.608762
    outer loop
      vertex 10.250254 273.284393 22.649748
      vertex 9.137823 273.284393 21.200001
      vertex 9.137823 274.884399 21.200001
    endloop
  endfacet
  facet normal 0.793353 0.000000 -0.608762
    outer loop
      vertex 10.250254 274.884399 22.649748
      vertex 10.250254 273.284393 22.649748
      vertex 9.137823 274.884399 21.200001
    endloop
  endfacet
  facet normal 0.608762 0.000000 -0.793353
    outer loop
      vertex 11.700001 273.284393 23.762178
      vertex 10.250254 273.284393 22.649748
      vertex 10.250254 274.884399 22.649748
    endloop
  endfacet
  facet normal 0.608762 0.000000 -0.793353
    outer loop
      vertex 11.700001 274.884399 23.762178
      vertex 11.700001 273.284393 23.762178
      vertex 10.250254 274.884399 22.649748
    endloop
  endfacet
  facet normal 0.382683 0.000000 -0.923880
    outer loop
      vertex 13.388268 273.284393 24.461481
      vertex 11.700001 273.284393 23.762178
      vertex 11.700001 274.884399 23.762178
    endloop
  endfacet
  facet normal 0.382683 0.000000 -0.923880
    outer loop
      vertex 13.388268 274.884399 24.461481
      vertex 13.388268 273.284393 24.461481
      vertex 11.700001 274.884399 23.762178
    endloop
  endfacet
  facet normal 0.130526 0.000000 -0.991445
    outer loop
      vertex 15.200001 273.284393 24.700001
      vertex 13.388268 273.284393 24.461481
      vertex 13.388268 274.884399 24.461481
    endloop
  endfacet
  facet normal 0.130526 0.000000 -0.991445
    outer loop
      vertex 15.200001 274.884399 24.700001
      vertex 15.200001 273.284393 24.700001
      vertex 13.388268 274.884399 24.461481
    endloop
  endfacet
  facet normal -0.130526 0.000000 -0.991445
    outer loop
      vertex 17.011734 273.284393 24.461481
      vertex 15.200001 273.284393 24.700001
      vertex 15.200001 274.884399 24.700001
    endloop
  endfacet
  facet normal -0.130526 -0.000000 -0.991445
    outer loop
      vertex 17.011734 274.884399 24.461481
      vertex 17.011734 273.284393 24.461481
      vertex 15.200001 274.884399 24.700001
    endloop
  endfacet
  facet normal -0.382683 0.000000 -0.923880
    outer loop
      vertex 18.700001 273.284393 23.762178
      vertex 17.011734 273.284393 24.461481
      vertex 17.011734 274.884399 24.461481
    endloop
  endfacet
  facet normal -0.382683 -0.000000 -0.923880
    outer loop
      vertex 18.700001 274.884399 23.762178
      vertex 18.700001 273.284393 23.762178
      vertex 17.011734 274.884399 24.461481
    endloop
  endfacet
  facet normal -0.608762 0.000000 -0.793353
    outer loop
      vertex 20.149748 273.284393 22.649748
      vertex 18.700001 273.284393 23.762178
      vertex 18.700001 274.884399 23.762178
    endloop
  endfacet
  facet normal -0.608762 -0.000000 -0.793353
    outer loop
      vertex 20.149748 274.884399 22.649748
      vertex 20.149748 273.284393 22.649748
      vertex 18.700001 274.884399 23.762178
    endloop
  endfacet
  facet normal -0.793353 0.000000 -0.608762
    outer loop
      vertex 21.262178 273.284393 21.200001
      vertex 20.149748 273.284393 22.649748
      vertex 20.149748 274.884399 22.649748
    endloop
  endfacet
  facet normal -0.793353 -0.000000 -0.608762
    outer loop
      vertex 21.262178 274.884399 21.200001
      vertex 21.262178 273.284393 21.200001
      vertex 20.149748 274.884399 22.649748
    endloop
  endfacet
  facet normal -0.923880 0.000000 -0.382683
    outer loop
      vertex 21.961481 273.284393 19.511734
      vertex 21.262178 273.284393 21.200001
      vertex 21.262178 274.884399 21.200001
    endloop
  endfacet
  facet normal -0.923880 -0.000000 -0.382683
    outer loop
      vertex 21.961481 274.884399 19.511734
      vertex 21.961481 273.284393 19.511734
      vertex 21.262178 274.884399 21.200001
    endloop
  endfacet
  facet normal -0.991445 0.000000 -0.130526
    outer loop
      vertex 22.200001 273.284393 17.700001
      vertex 21.961481 273.284393 19.511734
      vertex 21.961481 274.884399 19.511734
    endloop
  endfacet
  facet normal -0.991445 -0.000000 -0.130526
    outer loop
      vertex 22.200001 274.884399 17.700001
      vertex 22.200001 273.284393 17.700001
      vertex 21.961481 274.884399 19.511734
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 22.200001 273.284393 17.700001
      vertex 22.200001 274.884399 17.700001
      vertex 22.200001 274.884399 11.600000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 22.200001 273.284393 11.600000
      vertex 22.200001 273.284393 17.700001
      vertex 22.200001 274.884399 11.600000
    endloop
  endfacet
  facet normal 0.130564 -0.991440 0.000000
    outer loop
      vertex 2.785891 344.829865 11.600000
      vertex 3.200001 344.884399 11.600000
      vertex 3.200001 344.884399 33.599998
    endloop
  endfacet
  facet normal 0.130564 -0.991440 0.000000
    outer loop
      vertex 2.785891 344.829865 33.599998
      vertex 2.785891 344.829865 11.600000
      vertex 3.200001 344.884399 33.599998
    endloop
  endfacet
  facet normal 0.382642 -0.923897 0.000000
    outer loop
      vertex 2.400001 344.670044 11.600000
      vertex 2.785891 344.829865 11.600000
      vertex 2.785891 344.829865 33.599998
    endloop
  endfacet
  facet normal 0.382642 -0.923897 0.000000
    outer loop
      vertex 2.400001 344.670044 33.599998
      vertex 2.400001 344.670044 11.600000
      vertex 2.785891 344.829865 33.599998
    endloop
  endfacet
  facet normal 0.608765 -0.793350 0.000000
    outer loop
      vertex 2.068630 344.415771 11.600000
      vertex 2.400001 344.670044 11.600000
      vertex 2.400001 344.670044 33.599998
    endloop
  endfacet
  facet normal 0.608765 -0.793350 0.000000
    outer loop
      vertex 2.068630 344.415771 33.599998
      vertex 2.068630 344.415771 11.600000
      vertex 2.400001 344.670044 33.599998
    endloop
  endfacet
  facet normal 0.793371 -0.608739 0.000000
    outer loop
      vertex 1.814360 344.084381 11.600000
      vertex 2.068630 344.415771 11.600000
      vertex 2.068630 344.415771 33.599998
    endloop
  endfacet
  facet normal 0.793371 -0.608739 0.000000
    outer loop
      vertex 1.814360 344.084381 33.599998
      vertex 1.814360 344.084381 11.600000
      vertex 2.068630 344.415771 33.599998
    endloop
  endfacet
  facet normal 0.923871 -0.382705 0.000000
    outer loop
      vertex 1.654520 343.698517 11.600000
      vertex 1.814360 344.084381 11.600000
      vertex 1.814360 344.084381 33.599998
    endloop
  endfacet
  facet normal 0.923871 -0.382705 0.000000
    outer loop
      vertex 1.654520 343.698517 33.599998
      vertex 1.654520 343.698517 11.600000
      vertex 1.814360 344.084381 33.599998
    endloop
  endfacet
  facet normal 0.991445 -0.130522 0.000000
    outer loop
      vertex 1.600001 343.284393 11.600000
      vertex 1.654520 343.698517 11.600000
      vertex 1.654520 343.698517 33.599998
    endloop
  endfacet
  facet normal 0.991445 -0.130522 0.000000
    outer loop
      vertex 1.600001 343.284393 33.599998
      vertex 1.600001 343.284393 11.600000
      vertex 1.654520 343.698517 33.599998
    endloop
  endfacet
  facet normal 0.991445 0.130522 0.000000
    outer loop
      vertex 1.654520 276.070282 11.600000
      vertex 1.600001 276.484406 11.600000
      vertex 1.600001 276.484406 33.599998
    endloop
  endfacet
  facet normal 0.991445 0.130522 0.000000
    outer loop
      vertex 1.654520 276.070282 33.599998
      vertex 1.654520 276.070282 11.600000
      vertex 1.600001 276.484406 33.599998
    endloop
  endfacet
  facet normal 0.923881 0.382679 0.000000
    outer loop
      vertex 1.814360 275.684387 11.600000
      vertex 1.654520 276.070282 11.600000
      vertex 1.654520 276.070282 33.599998
    endloop
  endfacet
  facet normal 0.923881 0.382679 0.000000
    outer loop
      vertex 1.814360 275.684387 33.599998
      vertex 1.814360 275.684387 11.600000
      vertex 1.654520 276.070282 33.599998
    endloop
  endfacet
  facet normal 0.793344 0.608774 0.000000
    outer loop
      vertex 2.068630 275.353027 11.600000
      vertex 1.814360 275.684387 11.600000
      vertex 1.814360 275.684387 33.599998
    endloop
  endfacet
  facet normal 0.793344 0.608774 0.000000
    outer loop
      vertex 2.068630 275.353027 33.599998
      vertex 2.068630 275.353027 11.600000
      vertex 1.814360 275.684387 33.599998
    endloop
  endfacet
  facet normal 0.608765 0.793350 0.000000
    outer loop
      vertex 2.400001 275.098755 11.600000
      vertex 2.068630 275.353027 11.600000
      vertex 2.068630 275.353027 33.599998
    endloop
  endfacet
  facet normal 0.608765 0.793350 0.000000
    outer loop
      vertex 2.400001 275.098755 33.599998
      vertex 2.400001 275.098755 11.600000
      vertex 2.068630 275.353027 33.599998
    endloop
  endfacet
  facet normal 0.382705 0.923871 0.000000
    outer loop
      vertex 2.785891 274.938904 11.600000
      vertex 2.400001 275.098755 11.600000
      vertex 2.400001 275.098755 33.599998
    endloop
  endfacet
  facet normal 0.382705 0.923871 0.000000
    outer loop
      vertex 2.785891 274.938904 33.599998
      vertex 2.785891 274.938904 11.600000
      vertex 2.400001 275.098755 33.599998
    endloop
  endfacet
  facet normal 0.130493 0.991449 0.000000
    outer loop
      vertex 3.200001 274.884399 11.600000
      vertex 2.785891 274.938904 11.600000
      vertex 2.785891 274.938904 33.599998
    endloop
  endfacet
  facet normal 0.130493 0.991449 0.000000
    outer loop
      vertex 3.200001 274.884399 33.599998
      vertex 3.200001 274.884399 11.600000
      vertex 2.785891 274.938904 33.599998
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 33.200001 337.884399 11.600000
      vertex 30.773335 339.966736 11.600000
      vertex 30.850000 339.384399 11.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 30.773335 338.802063 11.600000
      vertex 33.200001 337.884399 11.600000
      vertex 30.850000 339.384399 11.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 30.548557 338.259399 11.600000
      vertex 33.200001 337.884399 11.600000
      vertex 30.773335 338.802063 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 33.200001 337.884399 11.600000
      vertex 30.548557 338.259399 11.600000
      vertex 30.190990 337.793396 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 33.200001 336.284393 11.600000
      vertex 33.200001 337.884399 11.600000
      vertex 30.190990 337.793396 11.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 29.725000 337.435852 11.600000
      vertex 33.200001 336.284393 11.600000
      vertex 30.190990 337.793396 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 28.600000 336.284393 11.600000
      vertex 33.200001 336.284393 11.600000
      vertex 29.725000 337.435852 11.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 29.182344 337.211060 11.600000
      vertex 28.600000 336.284393 11.600000
      vertex 29.725000 337.435852 11.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 28.600000 337.134399 11.600000
      vertex 28.600000 336.284393 11.600000
      vertex 29.182344 337.211060 11.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 27.797663 336.390015 11.600000
      vertex 28.600000 336.284393 11.600000
      vertex 28.600000 337.134399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 28.017658 337.211060 11.600000
      vertex 27.797663 336.390015 11.600000
      vertex 28.600000 337.134399 11.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 27.050001 336.699707 11.600000
      vertex 27.797663 336.390015 11.600000
      vertex 28.017658 337.211060 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 27.475000 337.435852 11.600000
      vertex 27.050001 336.699707 11.600000
      vertex 28.017658 337.211060 11.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 26.407970 337.192352 11.600000
      vertex 27.050001 336.699707 11.600000
      vertex 27.475000 337.435852 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 27.009010 337.793396 11.600000
      vertex 26.407970 337.192352 11.600000
      vertex 27.475000 337.435852 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 25.915321 337.834381 11.600000
      vertex 26.407970 337.192352 11.600000
      vertex 27.009010 337.793396 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 26.651443 338.259399 11.600000
      vertex 25.915321 337.834381 11.600000
      vertex 27.009010 337.793396 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 25.605631 338.582062 11.600000
      vertex 25.915321 337.834381 11.600000
      vertex 26.651443 338.259399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 26.426668 338.802063 11.600000
      vertex 25.605631 338.582062 11.600000
      vertex 26.651443 338.259399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 25.500002 339.384399 11.600000
      vertex 25.605631 338.582062 11.600000
      vertex 26.426668 338.802063 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 26.350000 339.384399 11.600000
      vertex 25.500002 339.384399 11.600000
      vertex 26.426668 338.802063 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 26.426668 339.966736 11.600000
      vertex 25.500002 339.384399 11.600000
      vertex 26.350000 339.384399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 25.500002 339.384399 11.600000
      vertex 26.426668 339.966736 11.600000
      vertex 26.651443 340.509399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 25.500002 344.884399 11.600000
      vertex 25.500002 339.384399 11.600000
      vertex 26.651443 340.509399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 27.009010 340.975372 11.600000
      vertex 25.500002 344.884399 11.600000
      vertex 26.651443 340.509399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 27.475000 341.332947 11.600000
      vertex 25.500002 344.884399 11.600000
      vertex 27.009010 340.975372 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 25.500002 344.884399 11.600000
      vertex 27.475000 341.332947 11.600000
      vertex 28.017658 341.557739 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 28.600000 341.634399 11.600000
      vertex 25.500002 344.884399 11.600000
      vertex 28.017658 341.557739 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 29.182344 341.557739 11.600000
      vertex 25.500002 344.884399 11.600000
      vertex 28.600000 341.634399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 38.000000 344.884399 11.600000
      vertex 25.500002 344.884399 11.600000
      vertex 29.182344 341.557739 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 29.725000 341.332947 11.600000
      vertex 38.000000 344.884399 11.600000
      vertex 29.182344 341.557739 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 30.190990 340.975372 11.600000
      vertex 38.000000 344.884399 11.600000
      vertex 29.725000 341.332947 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 39.600002 343.284393 11.600000
      vertex 38.000000 344.884399 11.600000
      vertex 30.190990 340.975372 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 30.548557 340.509399 11.600000
      vertex 39.600002 343.284393 11.600000
      vertex 30.190990 340.975372 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 30.773335 339.966736 11.600000
      vertex 39.600002 343.284393 11.600000
      vertex 30.548557 340.509399 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 33.200001 337.884399 11.600000
      vertex 39.600002 343.284393 11.600000
      vertex 30.773335 339.966736 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 39.600002 343.284393 11.600000
      vertex 33.200001 337.884399 11.600000
      vertex 39.600002 337.884399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 38.000000 344.884399 11.600000
      vertex 39.600002 343.284393 11.600000
      vertex 39.545483 343.698517 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 39.385643 344.084381 11.600000
      vertex 38.000000 344.884399 11.600000
      vertex 39.545483 343.698517 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 39.131371 344.415771 11.600000
      vertex 38.000000 344.884399 11.600000
      vertex 39.385643 344.084381 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 38.000000 344.884399 11.600000
      vertex 39.131371 344.415771 11.600000
      vertex 38.799999 344.670044 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 38.414112 344.829865 11.600000
      vertex 38.000000 344.884399 11.600000
      vertex 38.799999 344.670044 11.600000
    endloop
  endfacet
  facet normal -0.130553 0.991441 0.000000
    outer loop
      vertex 27.797663 284.378754 11.600000
      vertex 28.600000 284.484406 11.600000
      vertex 28.600000 284.484406 8.600000
    endloop
  endfacet
  facet normal -0.130553 0.991441 0.000000
    outer loop
      vertex 27.797663 284.378754 8.600000
      vertex 27.797663 284.378754 11.600000
      vertex 28.600000 284.484406 8.600000
    endloop
  endfacet
  facet normal -0.382684 0.923879 0.000000
    outer loop
      vertex 27.050001 284.069061 11.600000
      vertex 27.797663 284.378754 11.600000
      vertex 27.797663 284.378754 8.600000
    endloop
  endfacet
  facet normal -0.382684 0.923879 0.000000
    outer loop
      vertex 27.050001 284.069061 8.600000
      vertex 27.050001 284.069061 11.600000
      vertex 27.797663 284.378754 8.600000
    endloop
  endfacet
  facet normal -0.608760 0.793355 0.000000
    outer loop
      vertex 26.407970 283.576416 11.600000
      vertex 27.050001 284.069061 11.600000
      vertex 27.050001 284.069061 8.600000
    endloop
  endfacet
  facet normal -0.608760 0.793355 0.000000
    outer loop
      vertex 26.407970 283.576416 8.600000
      vertex 26.407970 283.576416 11.600000
      vertex 27.050001 284.069061 8.600000
    endloop
  endfacet
  facet normal -0.793351 0.608764 0.000000
    outer loop
      vertex 25.915321 282.934387 11.600000
      vertex 26.407970 283.576416 11.600000
      vertex 26.407970 283.576416 8.600000
    endloop
  endfacet
  facet normal -0.793351 0.608764 0.000000
    outer loop
      vertex 25.915321 282.934387 8.600000
      vertex 25.915321 282.934387 11.600000
      vertex 26.407970 283.576416 8.600000
    endloop
  endfacet
  facet normal -0.923878 0.382687 0.000000
    outer loop
      vertex 25.605631 282.186737 11.600000
      vertex 25.915321 282.934387 11.600000
      vertex 25.915321 282.934387 8.600000
    endloop
  endfacet
  facet normal -0.923878 0.382687 0.000000
    outer loop
      vertex 25.605631 282.186737 8.600000
      vertex 25.605631 282.186737 11.600000
      vertex 25.915321 282.934387 8.600000
    endloop
  endfacet
  facet normal -0.991445 0.130525 0.000000
    outer loop
      vertex 25.500002 281.384399 11.600000
      vertex 25.605631 282.186737 11.600000
      vertex 25.605631 282.186737 8.600000
    endloop
  endfacet
  facet normal -0.991445 0.130525 0.000000
    outer loop
      vertex 25.500002 281.384399 8.600000
      vertex 25.500002 281.384399 11.600000
      vertex 25.605631 282.186737 8.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 39.600002 284.484406 11.600000
      vertex 30.773335 281.966736 11.600000
      vertex 30.850000 281.384399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 30.773335 280.802063 11.600000
      vertex 39.600002 284.484406 11.600000
      vertex 30.850000 281.384399 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 39.600002 276.484406 11.600000
      vertex 39.600002 284.484406 11.600000
      vertex 30.773335 280.802063 11.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 30.548557 280.259399 11.600000
      vertex 39.600002 276.484406 11.600000
      vertex 30.773335 280.802063 11.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 30.190990 279.793396 11.600000
      vertex 39.600002 276.484406 11.600000
      vertex 30.548557 280.259399 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 38.000000 274.884399 11.600000
      vertex 39.600002 276.484406 11.600000
      vertex 30.190990 279.793396 11.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 29.725000 279.435852 11.600000
      vertex 38.000000 274.884399 11.600000
      vertex 30.190990 279.793396 11.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 29.182344 279.211060 11.600000
      vertex 38.000000 274.884399 11.600000
      vertex 29.725000 279.435852 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 25.500002 274.884399 11.600000
      vertex 38.000000 274.884399 11.600000
      vertex 29.182344 279.211060 11.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 28.600000 279.134399 11.600000
      vertex 25.500002 274.884399 11.600000
      vertex 29.182344 279.211060 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 28.017658 279.211060 11.600000
      vertex 25.500002 274.884399 11.600000
      vertex 28.600000 279.134399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 25.500002 274.884399 11.600000
      vertex 28.017658 279.211060 11.600000
      vertex 27.475000 279.435852 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 27.009010 279.793396 11.600000
      vertex 25.500002 274.884399 11.600000
      vertex 27.475000 279.435852 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 26.651443 280.259399 11.600000
      vertex 25.500002 274.884399 11.600000
      vertex 27.009010 279.793396 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 25.500002 281.384399 11.600000
      vertex 25.500002 274.884399 11.600000
      vertex 26.651443 280.259399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 26.426668 280.802063 11.600000
      vertex 25.500002 281.384399 11.600000
      vertex 26.651443 280.259399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 26.350000 281.384399 11.600000
      vertex 25.500002 281.384399 11.600000
      vertex 26.426668 280.802063 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 25.500002 281.384399 11.600000
      vertex 26.350000 281.384399 11.600000
      vertex 26.426668 281.966736 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 25.605631 282.186737 11.600000
      vertex 25.500002 281.384399 11.600000
      vertex 26.426668 281.966736 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 26.651443 282.509399 11.600000
      vertex 25.605631 282.186737 11.600000
      vertex 26.426668 281.966736 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 25.915321 282.934387 11.600000
      vertex 25.605631 282.186737 11.600000
      vertex 26.651443 282.509399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 27.009010 282.975372 11.600000
      vertex 25.915321 282.934387 11.600000
      vertex 26.651443 282.509399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 26.407970 283.576416 11.600000
      vertex 25.915321 282.934387 11.600000
      vertex 27.009010 282.975372 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 27.475000 283.332947 11.600000
      vertex 26.407970 283.576416 11.600000
      vertex 27.009010 282.975372 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 27.050001 284.069061 11.600000
      vertex 26.407970 283.576416 11.600000
      vertex 27.475000 283.332947 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 28.017658 283.557739 11.600000
      vertex 27.050001 284.069061 11.600000
      vertex 27.475000 283.332947 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 27.797663 284.378754 11.600000
      vertex 27.050001 284.069061 11.600000
      vertex 28.017658 283.557739 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 28.600000 283.634399 11.600000
      vertex 27.797663 284.378754 11.600000
      vertex 28.017658 283.557739 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 28.600000 284.484406 11.600000
      vertex 27.797663 284.378754 11.600000
      vertex 28.600000 283.634399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 29.182344 283.557739 11.600000
      vertex 28.600000 284.484406 11.600000
      vertex 28.600000 283.634399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 29.725000 283.332947 11.600000
      vertex 28.600000 284.484406 11.600000
      vertex 29.182344 283.557739 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 39.600002 284.484406 11.600000
      vertex 28.600000 284.484406 11.600000
      vertex 29.725000 283.332947 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 30.190990 282.975372 11.600000
      vertex 39.600002 284.484406 11.600000
      vertex 29.725000 283.332947 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 30.548557 282.509399 11.600000
      vertex 39.600002 284.484406 11.600000
      vertex 30.190990 282.975372 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 39.600002 284.484406 11.600000
      vertex 30.548557 282.509399 11.600000
      vertex 30.773335 281.966736 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 38.000000 274.884399 11.600000
      vertex 38.414112 274.938904 11.600000
      vertex 38.799999 275.098755 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 39.131371 275.353027 11.600000
      vertex 38.000000 274.884399 11.600000
      vertex 38.799999 275.098755 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 39.385643 275.684387 11.600000
      vertex 38.000000 274.884399 11.600000
      vertex 39.131371 275.353027 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 38.000000 274.884399 11.600000
      vertex 39.385643 275.684387 11.600000
      vertex 39.545483 276.070282 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 39.600002 276.484406 11.600000
      vertex 38.000000 274.884399 11.600000
      vertex 39.545483 276.070282 11.600000
    endloop
  endfacet
  facet normal -1.000000 0.000000 0.000000
    outer loop
      vertex 25.500002 281.384399 8.600000
      vertex 25.500002 274.884399 8.600000
      vertex 25.500002 274.884399 11.600000
    endloop
  endfacet
  facet normal -1.000000 -0.000000 -0.000000
    outer loop
      vertex 25.500002 281.384399 11.600000
      vertex 25.500002 281.384399 8.600000
      vertex 25.500002 274.884399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 8.700001 281.384399 11.600000
      vertex 7.773334 281.966736 11.600000
      vertex 7.850001 281.384399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 7.773334 280.802063 11.600000
      vertex 8.700001 281.384399 11.600000
      vertex 7.850001 281.384399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 7.548558 280.259399 11.600000
      vertex 8.700001 281.384399 11.600000
      vertex 7.773334 280.802063 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 8.700001 274.884399 11.600000
      vertex 8.700001 281.384399 11.600000
      vertex 7.548558 280.259399 11.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 7.190991 279.793396 11.600000
      vertex 8.700001 274.884399 11.600000
      vertex 7.548558 280.259399 11.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 6.725001 279.435852 11.600000
      vertex 8.700001 274.884399 11.600000
      vertex 7.190991 279.793396 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 8.700001 274.884399 11.600000
      vertex 6.725001 279.435852 11.600000
      vertex 6.182344 279.211060 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 8.200001 274.884399 11.600000
      vertex 8.700001 274.884399 11.600000
      vertex 6.182344 279.211060 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 8.200001 273.284393 11.600000
      vertex 8.700001 274.884399 11.600000
      vertex 8.200001 274.884399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 8.200001 274.884399 11.600000
      vertex 6.182344 279.211060 11.600000
      vertex 5.600001 279.134399 11.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 1.600001 276.484406 11.600000
      vertex 8.200001 274.884399 11.600000
      vertex 5.600001 279.134399 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 3.200001 274.884399 11.600000
      vertex 8.200001 274.884399 11.600000
      vertex 1.600001 276.484406 11.600000
    endloop
  endfacet
  facet normal -0.000000 -0.000000 1.000000
    outer loop
      vertex 1.654520 276.070282 11.600000
      vertex 3.200001 274.884399 11.600000
      vertex 1.600001 276.484406 11.600000
    endloop
  endfacet
  facet normal -0.000000 -0.000000 1.000000
    outer loop
      vertex 1.814360 275.684387 11.600000
      vertex 3.200001 274.884399 11.600000
      vertex 1.654520 276.070282 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 1.600001 276.484406 11.600000
      vertex 5.600001 279.134399 11.600000
      vertex 5.017658 279.211060 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 4.475001 279.435852 11.600000
      vertex 1.600001 276.484406 11.600000
      vertex 5.017658 279.211060 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 4.009011 279.793396 11.600000
      vertex 1.600001 276.484406 11.600000
      vertex 4.475001 279.435852 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 1.600001 276.484406 11.600000
      vertex 4.009011 279.793396 11.600000
      vertex 3.651444 280.259399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 3.426668 280.802063 11.600000
      vertex 1.600001 276.484406 11.600000
      vertex 3.651444 280.259399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 3.350001 281.384399 11.600000
      vertex 1.600001 276.484406 11.600000
      vertex 3.426668 280.802063 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 1.600001 284.484406 11.600000
      vertex 1.600001 276.484406 11.600000
      vertex 3.350001 281.384399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 3.426668 281.966736 11.600000
      vertex 1.600001 284.484406 11.600000
      vertex 3.350001 281.384399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 3.651444 282.509399 11.600000
      vertex 1.600001 284.484406 11.600000
      vertex 3.426668 281.966736 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 1.600001 284.484406 11.600000
      vertex 3.651444 282.509399 11.600000
      vertex 4.009011 282.975372 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 4.475001 283.332947 11.600000
      vertex 1.600001 284.484406 11.600000
      vertex 4.009011 282.975372 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 5.017658 283.557739 11.600000
      vertex 1.600001 284.484406 11.600000
      vertex 4.475001 283.332947 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 5.600001 284.484406 11.600000
      vertex 1.600001 284.484406 11.600000
      vertex 5.017658 283.557739 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 5.600001 283.634399 11.600000
      vertex 5.600001 284.484406 11.600000
      vertex 5.017658 283.557739 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 6.402340 284.378754 11.600000
      vertex 5.600001 284.484406 11.600000
      vertex 5.600001 283.634399 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 6.182344 283.557739 11.600000
      vertex 6.402340 284.378754 11.600000
      vertex 5.600001 283.634399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 7.150001 284.069061 11.600000
      vertex 6.402340 284.378754 11.600000
      vertex 6.182344 283.557739 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 6.725001 283.332947 11.600000
      vertex 7.150001 284.069061 11.600000
      vertex 6.182344 283.557739 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 7.792032 283.576416 11.600000
      vertex 7.150001 284.069061 11.600000
      vertex 6.725001 283.332947 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 7.190991 282.975372 11.600000
      vertex 7.792032 283.576416 11.600000
      vertex 6.725001 283.332947 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 8.284679 282.934387 11.600000
      vertex 7.792032 283.576416 11.600000
      vertex 7.190991 282.975372 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 7.548558 282.509399 11.600000
      vertex 8.284679 282.934387 11.600000
      vertex 7.190991 282.975372 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 8.594371 282.186737 11.600000
      vertex 8.284679 282.934387 11.600000
      vertex 7.548558 282.509399 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 7.773334 281.966736 11.600000
      vertex 8.594371 282.186737 11.600000
      vertex 7.548558 282.509399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 8.700001 281.384399 11.600000
      vertex 8.594371 282.186737 11.600000
      vertex 7.773334 281.966736 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 22.200001 273.284393 11.600000
      vertex 22.200001 274.884399 11.600000
      vertex 8.700001 274.884399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 8.200001 273.284393 11.600000
      vertex 22.200001 273.284393 11.600000
      vertex 8.700001 274.884399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 3.200001 274.884399 11.600000
      vertex 1.814360 275.684387 11.600000
      vertex 2.068630 275.353027 11.600000
    endloop
  endfacet
  facet normal -0.000000 -0.000000 1.000000
    outer loop
      vertex 2.400001 275.098755 11.600000
      vertex 3.200001 274.884399 11.600000
      vertex 2.068630 275.353027 11.600000
    endloop
  endfacet
  facet normal -0.000000 -0.000000 1.000000
    outer loop
      vertex 2.785891 274.938904 11.600000
      vertex 3.200001 274.884399 11.600000
      vertex 2.400001 275.098755 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 7.850001 339.384399 11.600000
      vertex 7.773334 338.802063 11.600000
      vertex 8.594371 338.582062 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 8.700001 339.384399 11.600000
      vertex 7.850001 339.384399 11.600000
      vertex 8.594371 338.582062 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 7.773334 339.966736 11.600000
      vertex 7.850001 339.384399 11.600000
      vertex 8.700001 339.384399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 7.548558 340.509399 11.600000
      vertex 7.773334 339.966736 11.600000
      vertex 8.700001 339.384399 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 8.700001 344.884399 11.600000
      vertex 7.548558 340.509399 11.600000
      vertex 8.700001 339.384399 11.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 7.190991 340.975372 11.600000
      vertex 7.548558 340.509399 11.600000
      vertex 8.700001 344.884399 11.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 6.725001 341.332947 11.600000
      vertex 7.190991 340.975372 11.600000
      vertex 8.700001 344.884399 11.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 6.182344 341.557739 11.600000
      vertex 6.725001 341.332947 11.600000
      vertex 8.700001 344.884399 11.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 5.600001 341.634399 11.600000
      vertex 6.182344 341.557739 11.600000
      vertex 8.700001 344.884399 11.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 3.200001 344.884399 11.600000
      vertex 5.600001 341.634399 11.600000
      vertex 8.700001 344.884399 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 5.017658 341.557739 11.600000
      vertex 5.600001 341.634399 11.600000
      vertex 3.200001 344.884399 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 4.475001 341.332947 11.600000
      vertex 5.017658 341.557739 11.600000
      vertex 3.200001 344.884399 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 4.009011 340.975372 11.600000
      vertex 4.475001 341.332947 11.600000
      vertex 3.200001 344.884399 11.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 1.600001 343.284393 11.600000
      vertex 4.009011 340.975372 11.600000
      vertex 3.200001 344.884399 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 3.651444 340.509399 11.600000
      vertex 4.009011 340.975372 11.600000
      vertex 1.600001 343.284393 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 3.426668 339.966736 11.600000
      vertex 3.651444 340.509399 11.600000
      vertex 1.600001 343.284393 11.600000
    endloop
  endfacet
  facet normal 0.000000 -0.000000 1.000000
    outer loop
      vertex 3.350001 339.384399 11.600000
      vertex 3.426668 339.966736 11.600000
      vertex 1.600001 343.284393 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 1.600001 336.284393 11.600000
      vertex 3.350001 339.384399 11.600000
      vertex 1.600001 343.284393 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 3.426668 338.802063 11.600000
      vertex 3.350001 339.384399 11.600000
      vertex 1.600001 336.284393 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 3.651444 338.259399 11.600000
      vertex 3.426668 338.802063 11.600000
      vertex 1.600001 336.284393 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 4.009011 337.793396 11.600000
      vertex 3.651444 338.259399 11.600000
      vertex 1.600001 336.284393 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 4.475001 337.435852 11.600000
      vertex 4.009011 337.793396 11.600000
      vertex 1.600001 336.284393 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 5.600001 336.284393 11.600000
      vertex 4.475001 337.435852 11.600000
      vertex 1.600001 336.284393 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 5.017658 337.211060 11.600000
      vertex 4.475001 337.435852 11.600000
      vertex 5.600001 336.284393 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 5.600001 337.134399 11.600000
      vertex 5.017658 337.211060 11.600000
      vertex 5.600001 336.284393 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 6.182344 337.211060 11.600000
      vertex 5.600001 337.134399 11.600000
      vertex 5.600001 336.284393 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 6.402340 336.390015 11.600000
      vertex 6.182344 337.211060 11.600000
      vertex 5.600001 336.284393 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 6.725001 337.435852 11.600000
      vertex 6.182344 337.211060 11.600000
      vertex 6.402340 336.390015 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 7.150001 336.699707 11.600000
      vertex 6.725001 337.435852 11.600000
      vertex 6.402340 336.390015 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 7.190991 337.793396 11.600000
      vertex 6.725001 337.435852 11.600000
      vertex 7.150001 336.699707 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 7.792032 337.192352 11.600000
      vertex 7.190991 337.793396 11.600000
      vertex 7.150001 336.699707 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 7.548558 338.259399 11.600000
      vertex 7.190991 337.793396 11.600000
      vertex 7.792032 337.192352 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 8.284679 337.834381 11.600000
      vertex 7.548558 338.259399 11.600000
      vertex 7.792032 337.192352 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 7.773334 338.802063 11.600000
      vertex 7.548558 338.259399 11.600000
      vertex 8.284679 337.834381 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 8.594371 338.582062 11.600000
      vertex 7.773334 338.802063 11.600000
      vertex 8.284679 337.834381 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 1.600001 343.284393 11.600000
      vertex 3.200001 344.884399 11.600000
      vertex 2.785891 344.829865 11.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 2.400001 344.670044 11.600000
      vertex 1.600001 343.284393 11.600000
      vertex 2.785891 344.829865 11.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 2.068630 344.415771 11.600000
      vertex 1.600001 343.284393 11.600000
      vertex 2.400001 344.670044 11.600000
    endloop
  endfacet
  facet normal 0.000000 0.000000 1.000000
    outer loop
      vertex 1.600001 343.284393 11.600000
      vertex 2.068630 344.415771 11.600000
      vertex 1.814360 344.084381 11.600000
    endloop
  endfacet
  facet normal -0.000000 0.000000 1.000000
    outer loop
      vertex 1.654520 343.698517 11.600000
      vertex 1.600001 343.284393 11.600000
      vertex 1.814360 344.084381 11.600000
    endloop
  endfacet
  facet normal -0.000000 -1.000000 0.000000
    outer loop
      vertex 1.600001 336.284393 11.600000
      vertex 1.100001 336.284393 33.599998
      vertex 1.100001 336.284393 8.600000
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 5.600001 336.284393 8.600000
      vertex 1.600001 336.284393 11.600000
      vertex 1.100001 336.284393 8.600000
    endloop
  endfacet
  facet normal -0.000000 -1.000000 -0.000000
    outer loop
      vertex 5.600001 336.284393 11.600000
      vertex 1.600001 336.284393 11.600000
      vertex 5.600001 336.284393 8.600000
    endloop
  endfacet
  facet normal 0.000000 -1.000000 0.000000
    outer loop
      vertex 1.100001 336.284393 33.599998
      vertex 1.600001 336.284393 11.600000
      vertex 1.600001 336.284393 33.599998
    endloop
  endfacet
  facet normal 0.000000 1.000000 -0.000000
    outer loop
      vertex 23.600000 346.484406 21.000000
      vertex 23.463705 346.484406 22.035276
      vertex 38.000000 346.484406 33.599998
    endloop
  endfacet
  facet normal 0.000000 1.000000 -0.000000
    outer loop
      vertex 38.000000 346.484406 7.000000
      vertex 23.600000 346.484406 21.000000
      vertex 38.000000 346.484406 33.599998
    endloop
  endfacet
  facet normal -0.000000 1.000000 0.000000
    outer loop
      vertex 23.463705 346.484406 19.964724
      vertex 23.600000 346.484406 21.000000
      vertex 38.000000 346.484406 7.000000
    endloop
  endfacet
  facet normal -0.000000 1.000000 0.000000
    outer loop
      vertex 23.064102 346.484406 19.000000
      vertex 23.463705 346.484406 19.964724
      vertex 38.000000 346.484406 7.000000
    endloop
  endfacet
  facet normal -0.000000 1.000000 0.000000
    outer loop
      vertex 22.428429 346.484406 18.171574
      vertex 23.064102 346.484406 19.000000
      vertex 38.000000 346.484406 7.000000
    endloop
  endfacet
  facet normal -0.000000 1.000000 0.000000
    outer loop
      vertex 21.600000 346.484406 17.535898
      vertex 22.428429 346.484406 18.171574
      vertex 38.000000 346.484406 7.000000
    endloop
  endfacet
  facet normal -0.000000 1.000000 0.000000
    outer loop
      vertex 20.635277 346.484406 17.136297
      vertex 21.600000 346.484406 17.535898
      vertex 38.000000 346.484406 7.000000
    endloop
  endfacet
  facet normal -0.000000 1.000000 0.000000
    outer loop
      vertex 19.600000 346.484406 17.000000
      vertex 20.635277 346.484406 17.136297
      vertex 38.000000 346.484406 7.000000
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 3.200001 346.484406 7.000000
      vertex 19.600000 346.484406 17.000000
      vertex 38.000000 346.484406 7.000000
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 18.564724 346.484406 17.136297
      vertex 19.600000 346.484406 17.000000
      vertex 3.200001 346.484406 7.000000
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 17.600000 346.484406 17.535898
      vertex 18.564724 346.484406 17.136297
      vertex 3.200001 346.484406 7.000000
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 16.771574 346.484406 18.171574
      vertex 17.600000 346.484406 17.535898
      vertex 3.200001 346.484406 7.000000
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 16.135899 346.484406 19.000000
      vertex 16.771574 346.484406 18.171574
      vertex 3.200001 346.484406 7.000000
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 15.736298 346.484406 19.964724
      vertex 16.135899 346.484406 19.000000
      vertex 3.200001 346.484406 7.000000
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 15.600001 346.484406 21.000000
      vertex 15.736298 346.484406 19.964724
      vertex 3.200001 346.484406 7.000000
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 3.200001 346.484406 33.599998
      vertex 15.600001 346.484406 21.000000
      vertex 3.200001 346.484406 7.000000
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 15.736298 346.484406 22.035276
      vertex 15.600001 346.484406 21.000000
      vertex 3.200001 346.484406 33.599998
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 16.135899 346.484406 23.000000
      vertex 15.736298 346.484406 22.035276
      vertex 3.200001 346.484406 33.599998
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 16.771574 346.484406 23.828426
      vertex 16.135899 346.484406 23.000000
      vertex 3.200001 346.484406 33.599998
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 17.600000 346.484406 24.464102
      vertex 16.771574 346.484406 23.828426
      vertex 3.200001 346.484406 33.599998
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 18.564724 346.484406 24.863703
      vertex 17.600000 346.484406 24.464102
      vertex 3.200001 346.484406 33.599998
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 19.600000 346.484406 25.000000
      vertex 18.564724 346.484406 24.863703
      vertex 3.200001 346.484406 33.599998
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 38.000000 346.484406 33.599998
      vertex 19.600000 346.484406 25.000000
      vertex 3.200001 346.484406 33.599998
    endloop
  endfacet
  facet normal 0.000000 1.000000 -0.000000
    outer loop
      vertex 20.635277 346.484406 24.863703
      vertex 19.600000 346.484406 25.000000
      vertex 38.000000 346.484406 33.599998
    endloop
  endfacet
  facet normal 0.000000 1.000000 -0.000000
    outer loop
      vertex 21.600000 346.484406 24.464102
      vertex 20.635277 346.484406 24.863703
      vertex 38.000000 346.484406 33.599998
    endloop
  endfacet
  facet normal 0.000000 1.000000 -0.000000
    outer loop
      vertex 22.428429 346.484406 23.828426
      vertex 21.600000 346.484406 24.464102
      vertex 38.000000 346.484406 33.599998
    endloop
  endfacet
  facet normal 0.000000 1.000000 -0.000000
    outer loop
      vertex 23.064102 346.484406 23.000000
      vertex 22.428429 346.484406 23.828426
      vertex 38.000000 346.484406 33.599998
    endloop
  endfacet
  facet normal 0.000000 1.000000 -0.000000
    outer loop
      vertex 23.463705 346.484406 22.035276
      vertex 23.064102 346.484406 23.000000
      vertex 38.000000 346.484406 33.599998
    endloop
  endfacet
  facet normal -0.991445 -0.130524 0.000000
    outer loop
      vertex 39.545483 343.698517 11.600000
      vertex 39.600002 343.284393 11.600000
      vertex 39.600002 343.284393 33.599998
    endloop
  endfacet
  facet normal -0.991445 -0.130524 -0.000000
    outer loop
      vertex 39.545483 343.698517 33.599998
      vertex 39.545483 343.698517 11.600000
      vertex 39.600002 343.284393 33.599998
    endloop
  endfacet
  facet normal -0.923872 -0.382703 0.000000
    outer loop
      vertex 39.385643 344.084381 11.600000
      vertex 39.545483 343.698517 11.600000
      vertex 39.545483 343.698517 33.599998
    endloop
  endfacet
  facet normal -0.923872 -0.382703 -0.000000
    outer loop
      vertex 39.385643 344.084381 33.599998
      vertex 39.385643 344.084381 11.600000
      vertex 39.545483 343.698517 33.599998
    endloop
  endfacet
  facet normal -0.793368 -0.608743 0.000000
    outer loop
      vertex 39.131371 344.415771 11.600000
      vertex 39.385643 344.084381 11.600000
      vertex 39.385643 344.084381 33.599998
    endloop
  endfacet
  facet normal -0.793368 -0.608743 -0.000000
    outer loop
      vertex 39.131371 344.415771 33.599998
      vertex 39.131371 344.415771 11.600000
      vertex 39.385643 344.084381 33.599998
    endloop
  endfacet
  facet normal -0.608765 -0.793351 0.000000
    outer loop
      vertex 38.799999 344.670044 11.600000
      vertex 39.131371 344.415771 11.600000
      vertex 39.131371 344.415771 33.599998
    endloop
  endfacet
  facet normal -0.608765 -0.793351 -0.000000
    outer loop
      vertex 38.799999 344.670044 33.599998
      vertex 38.799999 344.670044 11.600000
      vertex 39.131371 344.415771 33.599998
    endloop
  endfacet
  facet normal -0.382644 -0.923896 0.000000
    outer loop
      vertex 38.414112 344.829865 11.600000
      vertex 38.799999 344.670044 11.600000
      vertex 38.799999 344.670044 33.599998
    endloop
  endfacet
  facet normal -0.382644 -0.923896 -0.000000
    outer loop
      vertex 38.414112 344.829865 33.599998
      vertex 38.414112 344.829865 11.600000
      vertex 38.799999 344.670044 33.599998
    endloop
  endfacet
  facet normal -0.130564 -0.991440 0.000000
    outer loop
      vertex 38.000000 344.884399 11.600000
      vertex 38.414112 344.829865 11.600000
      vertex 38.414112 344.829865 33.599998
    endloop
  endfacet
  facet normal -0.130564 -0.991440 -0.000000
    outer loop
      vertex 38.000000 344.884399 33.599998
      vertex 38.000000 344.884399 11.600000
      vertex 38.414112 344.829865 33.599998
    endloop
  endfacet
  facet normal -0.130492 0.991449 0.000000
    outer loop
      vertex 38.414112 274.938904 11.600000
      vertex 38.000000 274.884399 11.600000
      vertex 38.000000 274.884399 33.599998
    endloop
  endfacet
  facet normal -0.130492 0.991449 0.000000
    outer loop
      vertex 38.414112 274.938904 33.599998
      vertex 38.414112 274.938904 11.600000
      vertex 38.000000 274.884399 33.599998
    endloop
  endfacet
  facet normal -0.382707 0.923870 0.000000
    outer loop
      vertex 38.799999 275.098755 11.600000
      vertex 38.414112 274.938904 11.600000
      vertex 38.414112 274.938904 33.599998
    endloop
  endfacet
  facet normal -0.382707 0.923870 0.000000
    outer loop
      vertex 38.799999 275.098755 33.599998
      vertex 38.799999 275.098755 11.600000
      vertex 38.414112 274.938904 33.599998
    endloop
  endfacet
  facet normal -0.608765 0.793351 0.000000
    outer loop
      vertex 39.131371 275.353027 11.600000
      vertex 38.799999 275.098755 11.600000
      vertex 38.799999 275.098755 33.599998
    endloop
  endfacet
  facet normal -0.608765 0.793351 0.000000
    outer loop
      vertex 39.131371 275.353027 33.599998
      vertex 39.131371 275.353027 11.600000
      vertex 38.799999 275.098755 33.599998
    endloop
  endfacet
  facet normal -0.793341 0.608778 0.000000
    outer loop
      vertex 39.385643 275.684387 11.600000
      vertex 39.131371 275.353027 11.600000
      vertex 39.131371 275.353027 33.599998
    endloop
  endfacet
  facet normal -0.793341 0.608778 0.000000
    outer loop
      vertex 39.385643 275.684387 33.599998
      vertex 39.385643 275.684387 11.600000
      vertex 39.131371 275.353027 33.599998
    endloop
  endfacet
  facet normal -0.923882 0.382677 0.000000
    outer loop
      vertex 39.545483 276.070282 11.600000
      vertex 39.385643 275.684387 11.600000
      vertex 39.385643 275.684387 33.599998
    endloop
  endfacet
  facet normal -0.923882 0.382677 0.000000
    outer loop
      vertex 39.545483 276.070282 33.599998
      vertex 39.545483 276.070282 11.600000
      vertex 39.385643 275.684387 33.599998
    endloop
  endfacet
  facet normal -0.991445 0.130524 0.000000
    outer loop
      vertex 39.600002 276.484406 11.600000
      vertex 39.545483 276.070282 11.600000
      vertex 39.545483 276.070282 33.599998
    endloop
  endfacet
  facet normal -0.991445 0.130524 0.000000
    outer loop
      vertex 39.600002 276.484406 33.599998
      vertex 39.600002 276.484406 11.600000
      vertex 39.545483 276.070282 33.599998
    endloop
  endfacet
  facet normal -0.000000 1.000000 0.000000
    outer loop
      vertex 1.600001 284.484406 11.600000
      vertex 5.600001 284.484406 11.600000
      vertex 5.600001 284.484406 8.600000
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 1.100001 284.484406 8.600000
      vertex 1.600001 284.484406 11.600000
      vertex 5.600001 284.484406 8.600000
    endloop
  endfacet
  facet normal 0.000000 1.000000 0.000000
    outer loop
      vertex 1.100001 284.484406 33.599998
      vertex 1.600001 284.484406 11.600000
      vertex 1.100001 284.484406 8.600000
    endloop
  endfacet
  facet normal 0.000000 1.000000 -0.000000
    outer loop
      vertex 1.600001 284.484406 11.600000
      vertex 1.100001 284.484406 33.599998
      vertex 1.600001 284.484406 33.599998
    endloop
  endfacet
  facet normal 0.991445 0.130526 0.000000
    outer loop
      vertex 8.594371 282.186737 11.600000
      vertex 8.700001 281.384399 11.600000
      vertex 8.700001 281.384399 8.600000
    endloop
  endfacet
  facet normal 0.991445 0.130526 -0.000000
    outer loop
      vertex 8.594371 282.186737 8.600000
      vertex 8.594371 282.186737 11.600000
      vertex 8.700001 281.384399 8.600000
    endloop
  endfacet
  facet normal 0.923878 0.382688 0.000000
    outer loop
      vertex 8.284679 282.934387 11.600000
      vertex 8.594371 282.186737 11.600000
      vertex 8.594371 282.186737 8.600000
    endloop
  endfacet
  facet normal 0.923878 0.382688 -0.000000
    outer loop
      vertex 8.284679 282.934387 8.600000
      vertex 8.284679 282.934387 11.600000
      vertex 8.594371 282.186737 8.600000
    endloop
  endfacet
  facet normal 0.793353 0.608762 0.000000
    outer loop
      vertex 7.792032 283.576416 11.600000
      vertex 8.284679 282.934387 11.600000
      vertex 8.284679 282.934387 8.600000
    endloop
  endfacet
  facet normal 0.793353 0.608762 -0.000000
    outer loop
      vertex 7.792032 283.576416 8.600000
      vertex 7.792032 283.576416 11.600000
      vertex 8.284679 282.934387 8.600000
    endloop
  endfacet
  facet normal 0.608759 0.793355 0.000000
    outer loop
      vertex 7.150001 284.069061 11.600000
      vertex 7.792032 283.576416 11.600000
      vertex 7.792032 283.576416 8.600000
    endloop
  endfacet
  facet normal 0.608759 0.793355 -0.000000
    outer loop
      vertex 7.150001 284.069061 8.600000
      vertex 7.150001 284.069061 11.600000
      vertex 7.792032 283.576416 8.600000
    endloop
  endfacet
  facet normal 0.382684 0.923879 0.000000
    outer loop
      vertex 6.402340 284.378754 11.600000
      vertex 7.150001 284.069061 11.600000
      vertex 7.150001 284.069061 8.600000
    endloop
  endfacet
  facet normal 0.382684 0.923879 -0.000000
    outer loop
      vertex 6.402340 284.378754 8.600000
      vertex 6.402340 284.378754 11.600000
      vertex 7.150001 284.069061 8.600000
    endloop
  endfacet
  facet normal 0.130553 0.991441 0.000000
    outer loop
      vertex 5.600001 284.484406 11.600000
      vertex 6.402340 284.378754 11.600000
      vertex 6.402340 284.378754 8.600000
    endloop
  endfacet
  facet normal 0.130553 0.991441 -0.000000
    outer loop
      vertex 5.600001 284.484406 8.600000
      vertex 5.600001 284.484406 11.600000
      vertex 6.402340 284.378754 8.600000
    endloop
  endfacet
  facet normal 1.000000 0.000000 0.000000
    outer loop
      vertex 8.700001 274.884399 8.600000
      vertex 8.700001 281.384399 8.600000
      vertex 8.700001 281.384399 11.600000
    endloop
  endfacet
  facet normal 1.000000 -0.000000 0.000000
    outer loop
      vertex 8.700001 274.884399 11.600000
      vertex 8.700001 274.884399 8.600000
      vertex 8.700001 281.384399 11.600000
    endloop
  endfacet
endsolid Mesh

```

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
