"""
    run.py
    Author: Daniel Vignoles

    Purpose: Scrape the contents of an api.weather.com xml page to data directory
"""

from WeatherLinkScrape import write_xml
from wl_sqlalch import db_insert
import os

username = os.environ['WS_USER_ID']
password = os.environ['WS_PASS']
token = os.environ['WS_TOKEN']

#alerts
#TODO: provide option to not use alerts
email = {}
email['sender'] = os.environ.get('ALERT_SENDER')
email['sender_pass'] = os.environ.get('ALERT_PASS')
email['receiver'] = os.environ.get('ALERT_RECEIVER')

XML_URL = 'https://api.weatherlink.com/v1/NoaaExt.xml?user='+ username +'&pass=' + password +'&apiToken=' + token

db_insert(XML_URL,alert=email)