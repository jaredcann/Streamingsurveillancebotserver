#!/bin/bash
sudo arecord --device=hw:1,0 --format S16_LE --rate 44100 -V mono -c 1 -d 10 /var/www/sounds/voice.wav
