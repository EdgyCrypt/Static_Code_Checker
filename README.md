# Static_Code_Checker

## Requirement

- [Python 3.7](https://www.python.org/downloads/release/python-375/)
    - As of Jan 22 2020 we are still treating Python 3.8 as "unsafe"
- Pip ("Pip installs Packages / Python")

- For Mac Users only
    - [Active State TCL](https://www.activestate.com/products/tcl/downloads/) 

- For Linux Users (NonUbuntu based distro's) Only
    - [Active State TCL](https://www.activestate.com/products/tcl/downloads/) 
        - To run without making configs changes you will also have to run the install script as root
            - you may also have to update the $PATH in your .bashrc file
    - You could also get the package from your disto's repos 
        - [AUR](https://www.archlinux.org/packages/extra/x86_64/tk/)

## Getting Pip

### Windows and MacOS

Downloading Python 3.7 and allowing it extend the $PATH during installation will force give you access to Pip

### Linux

using your distro's package manager call something like this

``` bash 
sudo <package manager command> <install command> python3-pip
```

or

``` bash
sudo <package manager command> <install command> python-pip
```

based on what your defaulted python version is

#### Debian / Ubuntu Based

``` bash
sudo apt install python3-pip
```

#### Arch Based

``` bash
sudo pacman -Syu python3-pip
```

#### Red Hat Based

``` bash
sudo dnf / yum install python3-pip
```

## Installing with Pip
``` bash
cd <path>/Static_Code_Checker
pip install -r requirements.txt
```

## Running The Application
``` bash
cd <path>/Static_Code_Checker
<python command> TBD
```

Then go to this [site](http://localhost:8080/) (http://localhost:8080/)
