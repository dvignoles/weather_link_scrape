"""
    run.py
    Author: Daniel Vignoles

    Purpose: Scrape the contents of an api.weather.com xml page to data directory
"""

from WeatherLinkScrape import write_xml
import sys

username = sys.argv[1]
password = sys.argv[2]
token = sys.argv[3]

XML_URL = 'https://api.weatherlink.com/v1/NoaaExt.xml?user='+ username +'&pass=' + password +'&apiToken=' + token

write_xml(XML_URL)