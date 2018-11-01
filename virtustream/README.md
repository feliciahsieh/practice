# Virtustream Fibonacci app

<p align="center"><img src="fibonacci.jpg" style="height:100px" /></p>

## Welcome
REST app that sends the requested elements of the Fibonacci sequence.

First series of Fibonacci starts with 0, 1, 1, 2, 3, ...

Test files are in the ```tests``` directory.

This app uses python, flask. Curl is used for testing.


## Table of Contents
* [Environment](#environment)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)


## Environment
* Vagrant 2.0.2
* SSH

Python is installed in /usr/bin/python3. You may have to adjust the directory path to your python source files accordingly in each of the *.py files.

## Requirements
* Ubuntu 14.04 LTS
* Python 3.4.2
* Flask 0.12.2
* setuptools

## Installation
In your terminal window, git clone the directory with the following command:

```
git clone https://github.com/feliciahsieh/practice/virtustream/fibonacci.git
```

To install setuptools for python 3.x:
```
sudo apt-get install python3-setuptools
```


## Usage
In one vagrant window, run (and leave it running):
```
./app.py
```

In second vagrant window, run
```
curl 127.0.0.1 ....[to be updated]
```
