# Windows-GUI-network-flow-monitoring-program
This simple Windows desktop widget will show your network's up and down data flow, it is written in Python 3, using **Tkinter** comes with Python as its GUI library and **psutil** a useful system monitoring and analyzing package. It is good for us learning GUI and network programming in Python.
## psutil
In order to get the network information from your machine, we use psutil, a cross-platform package that will easily help you acquire the system's current running processes and the system's usage rate including CPU, RAM, drives, network etc. information. It supports 32bit and 64bit Linux, Windows, MacOS, FreeBSD etc. operating systems.

**To get basic network information**
1. obtain the total network throughput

   psutil.net_io_counters()
3. obtain a specific network adapter's throughput, add pernic=True parameter

   psutil.net_io_counters(pernic=True)['ETHERNET']
## How to install psutil
Open your command line prompt on Windows, input
### >pip install psutil
A screenshot of this program

![screenshot](images/screenshot1.png#pic_center)
