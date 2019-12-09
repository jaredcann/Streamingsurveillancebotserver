# Streaming Surveillance Bot Server

   The goal of this project is to create a room surveillance droid or robot that could be controlled remotely through a web page. The droid will be operated using a Pi 4B board and will comes with multitude of different features:
   
   1. Web page GUI<br>
      Allowing the user to control the droid using a control GUI hosted on the pi web server. User will be able to log into the web page with any device that support web browser capability and are connected onto the same network as the droids.
   2. Video live steam with IR night vision pi camera<br>
   A combination of noIR pi camera and 2 IR LED light connected with light sensor for automatic switch, that will stream the visual input of the room (dark or bright) onto the web page 
   3. Speaker warning signals<br>
   Ouputing warning singals available on the GUI to the target room
   4. Live Broadcast target room audio<br>
   Allowing user to get live audio feedback of the room while surveilling
   5. Pan and tilt camera<br>
   Giving the user freedom to adjust camera viewing angle

_____________________________________
# Hardware setup
* Raspberry pi-4
* [4WD DC-motor and chassis](https://www.amazon.com/Robot-Chassis-Motor-Arduino-Raspberry/dp/B07F759T89/ref=asc_df_B07F759T89/?tag=hyprod-20&linkCode=df0&hvadid=312123579962&hvpos=1o2&hvnetw=g&hvrand=4023891843030921682&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1015254&hvtargid=pla-572041604638&psc=1&tag=&ref=&adgrpid=65834404201&hvpone=&hvptwo=&hvadid=312123579962&hvpos=1o2&hvnetw=g&hvrand=4023891843030921682&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1015254&hvtargid=pla-572041604638)
* sparkfun h-bridge motor driver  
* [Mini Portable Speaker, 3W Mobile Phone Speaker Line-in Speaker 3.5mm AUX Audio Interface ](https://www.amazon.com/gp/product/B07RJR1XPH/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1) 
* 2 servos
* [no Infared filter pi camera and Infared LED lights](https://www.amazon.com/Raspberry-Haiworld-Version-Megapixel-Infrared/dp/B01MYUOQ0A/ref=sr_1_5?keywords=pi+module+ir+camera&qid=1573746119&sr=8-5)
* Portable cellular battery charger
* 4 AA batteries and holder
* [Top plate of red robot chassis](https://www.sumozade.com/magician-robot-chassis-kit---red-455)


_____________________________________
# Hook up Guide

## H-bridge Pin Connections

| Raspberry pi pin  | H-bridge pin |
| ------------- | ------------- |
| 3.3V  |  logic for motor driver for speed information  |
| GPIO 6  | connect to H-bridge- Motor left -  |
| GPIO 5  | connect to H-bridge- Motor left +  |
| GPIO 19  | Connect to H-bridge- Motor Right -  |
| GPIO 13  | Connect to H-bridge- Motor right -  |
| AA batery rail  | H-bridge power input  |

## Servos Wiring & Pin Connection

Red and black power wires connects to 4AA batteries power rail

| Raspberry pi pin  | Servo|
| ------------- | ------------- |
| GPIO 17  |  connects to control tilt servo |
| GPIO 23  |  connects to control pan servo |

## Misc. Parts Connection

* connect 3.5 aux jack to portable mini speaker

* Usb microphone to pi-4 usb input

* Pi-camera to pi-4 camera ribbin cable connector

* Connect Pi-4 Usb-C pwr port to portable cell phone power pack


![Pi 4 Pinout](/Assets/pi4PinOut.png)

![Top view](/Assets/IMG_1382.jpg)

![Back view](/Assets/IMG_1389.jpg)

<br>

Link to video Demo:  https://youtu.be/eEnGLcFCr18

_____
# Software setup

## Setting up and install wiringPi
```
$ git clone git://git.drogon.net/wiringPi

$ cd wiringPi

$ ./build
```
<br><br>
## Setting up and install lighttpd 
```
$ sudo apt-get -y install lighttpd

$ sudo lighttpd-enable-mod cgi

$ sudo lighttpd-enable-mod fastcgi
```
Changing the lighttpd config file 

Changing where the config file is looking for index.html file to "/var/www" instead of its default of "/var/www/html"

Config file location `$ sudo nano /etc/lighttpd/lighttpd.conf`

Other than configuring the path in lighttpd.conf to find the index.html, the cgi enable need to be configure too using

`sudo nano /etc/lighttpd/conf-enabled/10-cgi.conf`

In the $http ["url"] section make sure the alias.url is directed to the right file path. In our case it should be /var/www/cgi-bin. Some people also have success configuring it in the lighttpd.conf file and follow the same step, but we have not try it.

Start and stop lighttpd service
```
$ sudo /etc/init.d/lighttpd stop

$ sudo /etc/init.d/lighttpd start
```
<br><br>
## Install and setup mjpg-streamer for video streaming over web
```
$ sudo apt-get update

$ sudo apt-get upgrade

$ sudo apt-get install libjpeg62-turbo-dev

$ sudo apt-get install cmake

$ git clone https://github.com/jacksonliam/mjpg-streamer.git ~/mjpg-streamer

$ cd ~/mjpg-streamer/mjpg-streamer-experimental

$ make clean all

$ sudo rm -rf /opt/mjpg-streamer

$ sudo mv ~/mjpg-streamer/mjpg-streamer-experimental /opt/mjpg-streamer

$ sudo rm -rf ~/mjpg-streamer
```
- Test stream<br>
`LD_LIBRARY_PATH=/opt/mjpg-streamer/ /opt/mjpg-streamer/mjpg_streamer -i "input_raspicam.so -fps 15 -q 50 -x 640 -y 480" -o "output_http.so -p 9000 -w /opt/mjpg-streamer/www"`

<br><br>
## Servo Blaster library setup

Servo blaster allows you to control servos with GPIO pins instead of pwm pins

you must also change the libary default timing method from "PWM" to using the "PCM" so it doesnt interfere with 3.5mm aux jack

Copy and setup Servo blaster library
```
$ cd

$ sudo git clone https://github.com/richardghirst/PiBits

$ cd PiBits/ServoBlaster/user

$ sudo make servod

$ sudo make install

$ sudo chmod 755 servod

$ sudo ./servod
```
Define pins

`$ sudo ./servod --p1pins=11,16`


### Aditional config change

`$ sudo nano /etc/init.d/servoblaster`
```
...

case "$1" in
start)

/usr/local/sbin/servod $OPTS >/dev/null
```
change to:

`/usr/local/sbin/servod --p1pins=11,16 $OPTS >/dev/null`

To run this on startup use the follow in the rc.local file
```
cd /home/pi/PiBits/ServoBlaster/user

sudo ./servod --p1pins=11,16

cd
```
<br><br>
## Darkice and Icecast2 setup for audio broadcast

To install Darkice into raspbian, first in terminal run:

`$ sudo apt-get update`

Then add a deb-src repository to your sources list at /home/pi:
```
$ cd

$ wget https://github.com/x20mar/darkice-with-mp3-for-raspberry-pi/blob/master/darkice_1.0.1-999~mp3+1_armhf.deb?raw=true

$ mv darkice_1.0.1-999~mp3+1_armhf.deb?raw=true darkice_1.0.1-999~mp3+1_armhf.deb
```
Install Darkice using the newly added repository
```
$ sudo apt-get install libmp3lame0 libtwolame0

$ sudo dpkg -i darkice_1.0.1-999~mp3+1_armhf.deb
```
Once it is installed, from the Github, download and move the config file for Darkice , darckice.cfg, and the shell script darkice.sh to /home/pi. Make darkice.sh into executable 

`$ sudo chmod 777 /home/pi/darkice.sh`

Then go to rc.local to execute this shell script on boot up

`$ sudo nano /etc/rc.local`

At the bottom of the page before exit 0 add

`sudo /home/pi/darkice.sh`

Once darkice is installed and configure, follow these steps to activate the Icecast2 server.

`$ sudo apt-get install icecast2`

Follow through the configuration window, I suggest keep the default setting and press yes and ok for all setting. Next, start the Icecast2 server service by typing this command 

`$ sudo service icecast2 start`

<br><br>
## Omxplayer setup for audio warning signal output

since omxplayer is build-in not much setup to be done other than some permission setting

To allow the actual audio to be streamed from web page the following command needed to be used to give execution access to "vchiq"

`$ sudo chmod 777 /dev/vchiq`

<br></br>
## CGI file location and creation

Once the library is intalled and setup, from the Github, download and move the cgi-bin folder into /var/www/

To make sure all the file are executable, run:
```
$ cd /var/www/cgi-bin

$ sudo chmod 755 [filename]
```
For each of the cgi file using their corresponding filename such as,

`$ sudo chmod 755 forward.cgi`

Other than the given shell script, when creating new shell script file make sure that the first line (the Hash-Bang Hack, `#!/bin/bash`) is not begin with a space. If the shell script is generated properly, when reopening it after saving, the auto-coloring will be applied.

<br><br>
## Web page location

With all the shell scripts and library in place, the web page content can be obtain by downloading and moving the index.html, indexMobile.html, sounds, and image file and folder to /var/www/ for the lighttpd web server to read. 
