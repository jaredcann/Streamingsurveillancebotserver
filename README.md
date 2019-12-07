# Streamingsurveillancebotserver





_
Web Page Instruction from Dr. Hamblen

The web page should explain the project idea, provide instructions, code, and hardware setups so that anyone could recreate your project along with photos and videos along with team member names. It might make sense to have a longer video on the web page (since presentation time is so short). Documentation somewhat like a notebook page can be added in Github. Be sure to setup Github so that a password logon is not needed to view the site.
_
When creating the shell script file make sure that the first line (the Hash-Bang Hack) is not begin with a space. If the shell script is generated properly, when reopening it after saving, the auto-coloring will be applied.
_______________________________________
Other than configuring the path in lighttpd.conf to find the index.html, the cgi enable need to be configure too using 

<b>sudo nano /etc/lighttpd/conf-enabled/10-cgi.conf</b> 

In the $http ["url"] section make sure the alias.url is directed to the right file path. In our case it should be /var/www/cgi-bin
Some people also have success configuring it in the lighttpd.conf file and follow the same step, but we have not try it. 
_______________________________________
camera stream window added to Web page and start up stream added to rc.local
_______________________________________
LD_LIBRARY_PATH=/opt/mjpg-streamer/ /opt/mjpg-streamer/mjpg_streamer -i "input_raspicam.so -fps 15 -q 50 -x 640 -y 480" -o "output_http.so -p 9000 -w /opt/mjpg-streamer/www" &
_______________________________________
 
<b>sudo chmod 777 /dev/vchiq</b>
https://stackoverflow.com/questions/42583835/failed-to-open-vchiq-instance/42584382



Adding the microhone through bash commands

____________________________________________
https://www.seeedstudio.com/blog/2019/08/08/how-to-use-usb-mini-microphone-on-raspberry-pi-4/
_____________________________________________________________

The pwm messed up the sound from aux cord, must define explicit pwm signal in a precompiled .cpp program that way it doesnt leak and ruin the audio quality

Wiring -pi does not allow for graceful using of the aux port for audio

_____________________________________________________________
audio live streaming/broadcasting with darkice and icecast2
https://technicalustad.com/live-streaming-of-mp3-using-darkice-and-icecast2-on-raspberry-pi/
