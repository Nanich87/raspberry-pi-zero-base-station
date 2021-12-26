# Raspberry Pi Zero Base Station

## Requerements

### RTKLIB

> git clone https://github.com/rtklibexplorer/RTKLIB.git

### Libs

> sudo apt-get install build-essential
> sudo apt-get install automake
> sudo apt-get install checkinstall
> sudo apt-get install liblapack3
> sudo apt-get install libblas3
> sudo apt-get install gfortran

## Build

> cd RTKLIB
> cd app
> cd consapp
> sudo make
> sudo make install