#!/bin/sh
#Run every 5 minutes

while :; do clear; date | echo; bash wl_scrape.sh; sleep 300; done
