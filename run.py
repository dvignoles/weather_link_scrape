"""
    run.py
    Author: Daniel Vignoles

    Purpose: Scrape the contents of an api.weather.com xml page to data directory
"""

from WeatherLinkScrape import write_xml
from wl_sqlalch import db_insert
import sys

username = sys.argv[1]
password = sys.argv[2]
token = sys.argv[3]

#alerts
#TODO: provide option to not use alerts
email = {}
email['sender'] = sys.argv[4]
email['sender_pass'] = sys.argv[5]
email['receiver'] = sys.argv[6]

XML_URL = 'https://api.weatherlink.com/v1/NoaaExt.xml?user='+ username +'&pass=' + password +'&apiToken=' + token

db_insert(XML_URL,alert=email)