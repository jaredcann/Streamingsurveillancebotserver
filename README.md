# Streamingsurveillancebotserver

<b>Outline (Delete once web page finished):</b>
1. Explain project idea
2. Provide instructions, code, and hardware setups
   - <i>add photo or graph that might help instructing</i>
   - lighttpd setup
   - wiringpi setup
   - mjpeg (video streaming) setup
   - servoblaster setup
   - darkice and icecast2 setup
   - speaker setup
   - cgi file location and creation
   - web page location and creation (index.html)
   - hardware wiring 
3. Photo and video of the final result


_____




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
   

______

# Web Page Instruction from Dr. Hamblen

The web page should explain the project idea, provide instructions, code, and hardware setups so that anyone could recreate your project along with photos and videos along with team member names. It might make sense to have a longer video on the web page (since presentation time is so short). Documentation somewhat like a notebook page can be added in Github. Be sure to setup Github so that a password logon is not needed to view the site.
_________________


# Hardware setup
___________________________
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


<b> H-bridge Pin Connections</b>

GPIO 18- pwm for motor driver for speed information
GPIO 6 - connect to H-bridge- Motor left -
GPIO 5 - connect to H-bridge- Motor left +
GPIO 19 -connect to H-bridge- Motor left -
GPIO 13 -connect to H-bridge- Motor left +
AA battery power rails- to H-Bridge power input

<b>Connecting Servos</b>

Red and black power connects to 4AA batteries power rail
GPIO 17- connects to control tilt servo
GPIO 23- connects to control pan servo

connect 3.5 aux jack to portable mini speaker

Usb microphone to pi-4 usb input

Pi-camera to pi-4 camera ribbin cable connector











______

When creating the shell script file make sure that the first line (the Hash-Bang Hack) is not begin with a space. If the shell script is generated properly, when reopening it after saving, the auto-coloring will be applied.

_______________________________________

Other than configuring the path in lighttpd.conf to find the index.html, the cgi enable need to be configure too using<br><br>

<b>sudo nano /etc/lighttpd/conf-enabled/10-cgi.conf</b><br><br> 

In the $http ["url"] section make sure the alias.url is directed to the right file path. In our case it should be /var/www/cgi-bin. Some people also have success configuring it in the lighttpd.conf file and follow the same step, but we have not try it.
      
_______________________________________
camera stream window added to Web page and start up stream added to rc.local


LD_LIBRARY_PATH=/opt/mjpg-streamer/ /opt/mjpg-streamer/mjpg_streamer -i "input_raspicam.so -fps 15 -q 50 -x 640 -y 480" -o "output_http.so -p 9000 -w /opt/mjpg-streamer/www" &
_______________________________________
 
<b>sudo chmod 777 /dev/vchiq</b>
https://stackoverflow.com/questions/42583835/failed-to-open-vchiq-instance/42584382



Adding the microphone through bash commands

____________________________________________
https://www.seeedstudio.com/blog/2019/08/08/how-to-use-usb-mini-microphone-on-raspberry-pi-4/
_____________________________________________________________

The pwm messed up the sound from aux cord, must define explicit pwm signal in a precompiled .cpp program that way it doesnt leak and ruin the audio quality

Wiring -pi does not allow for graceful using of the aux port for audio

_____________________________________________________________
audio live streaming/broadcasting with darkice and icecast2
https://technicalustad.com/live-streaming-of-mp3-using-darkice-and-icecast2-on-raspberry-pi/
