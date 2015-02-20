#!/usr/bin/env python

__author__ = 'Diego'

import socket
import sys
import datetime

from Classes.WebDriverWrapper import WebDriverWrapper as WebDriver
from Classes import DisplayWrapper as Display
from Classes.DataExtractor import DataExtractor
from Classes.FBPoster import FBPoster
import traceback



# Variables

logMessage = ''
displayStarts = False
webDriverStarts = False

try:

    # SET DEPLOYMENT VARIABLES
    DEPLOYMENT = True
    if(socket.gethostname() == 'macdiego' or 'Apple' in sys.version):
        DEPLOYMENT = False


    # CONSTANTS
    FACEBOOK_URL = 'https://www.facebook.com'
    DEFAULT_MESSAGE = 'Inbox'


    # DATA EXTRACTION
    posts = DataExtractor().extractPosts()
    cookies = DataExtractor().extractCookies()

    # DISPLAY INITIALIZATION
    if(DEPLOYMENT):
        display = Display()
        display.start()
        displayStarts = True


    # WEBDRIVER INITIALIZATION
    webDriver = WebDriver()
    webDriver.start(FACEBOOK_URL)
    webDriverStarts = True
    webDriver.setCookies(cookies)


    # FBPOSTER INITIALIZATION AND EXECUTION
    fbPoster = FBPoster(driver=webDriver.webDriver)

    for post in posts:
        fbPoster.createAndDeletePost(post, DEFAULT_MESSAGE)
    message = DEFAULT_MESSAGE

    logMessage = 'SUCCESS'
except:

    logMessage = 'ERROR: '+ str(sys.exc_info()[0]) + ' (' + str(sys.exc_info()[1]) + ')'
    traceback.print_exc()


finally:

    # SAVE LOG
    time = str(datetime.datetime.now())
    logMessage = time + ' --> ' + logMessage
    with open('logs/default.log', 'a+') as f:
        f.write(logMessage + '\n')
    # END


# STOP RUNNING PROCESESS
if(webDriverStarts):
    print(logMessage)
    webDriver.stop()

if(displayStarts):
    if(DEPLOYMENT):
        display.stop()