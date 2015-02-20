#!/usr/bin/env python

__author__ = 'Diego'

import socket
import sys
import datetime

from Classes.WebDriverWrapper import WebDriverWrapper as WebDriver
from Classes import DisplayWrapper as Display
from Classes.DataExtractor import DataExtractor
from Classes.FBPoster import FBPoster




# Variables

logMessage = ''

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

    # WEBDRIVER INITIALIZATION
    webDriver = WebDriver()
    webDriver.start(FACEBOOK_URL)

    webDriver.setCookies(cookies)


    # FBPOSTER INITIALIZATION AND EXECUTION
    fbPoster = FBPoster(driver=webDriver.webDriver)

    for post in posts:
        fbPoster.createAndDeletePost(post, error)
    message = DEFAULT_MESSAGE

    logMessage = 'SUCCESS'
except:

    logMessage = 'ERROR: '+ str(sys.exc_info()[0]) + ' (' + str(sys.exc_info()[1]) + ')'

finally:
    # STOP DRIVER AND DISPLAY
    print(logMessage)
    webDriver.stop()

    if(DEPLOYMENT):
        display.stop()

    # SAVE LOG
    time = str(datetime.datetime.now())
    logMessage = time + ' --> ' + logMessage
    with open('logs/default.log', 'a+') as f:
        f.write(logMessage + '\n')
    # END