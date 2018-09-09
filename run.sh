#!/bin/bash

# ./cpp/main.out
python ./__main__.py

# HOW TO ADD TO AUTO STARTUP: 
# 	$ sudo nano /etc/init.d/my-webserver
# 		#!/bin/bash
#		/home/pi/Desktop/my-git/RPiPythonWebServer/run.sh
# 	$ sudo chmod 755 /etc/init.d/my-webserver 
# 	$ sudo update-rc.d my-webserver defaults