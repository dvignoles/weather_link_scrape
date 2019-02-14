#!/bin/sh
#Run every 10 minutes

WS_USER_ID=#WeatherLink User Id here
WS_PASS=#WeatherLink Password here
WS_TOKEN=#Weatherlink api token here

while :; do python run.py $WS_USER_ID $WS_PASS $WS_TOKEN; sleep 600; done
