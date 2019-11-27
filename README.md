# Streamingsurveillancebotserver


camera stream window added to Web page and start up stream added to rc.local
_______________________
LD_LIBRARY_PATH=/opt/mjpg-streamer/ /opt/mjpg-streamer/mjpg_streamer -i "input_raspicam.so -fps 15 -q 50 -x 640 -y 480" -o "output_http.so -p 9000 -w /opt/mjpg-streamer/www" &
 _________________________
 
 
