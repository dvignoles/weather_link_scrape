#!/bin/sh
#Run every 10 minutes

WS_USER_ID=#WeatherLink User Id here
WS_PASS=#WeatherLink Password here
WS_TOKEN=#Weatherlink api token here
ALERT_SENDER=#Email here
ALERT_PASS=#Email pass here
ALERT_RECEIVER=#Email here

python run.py $WS_USER_ID $WS_PASS $WS_TOKEN $ALERT_SENDER $ALERT_PASS $ALERT_RECEIVER
