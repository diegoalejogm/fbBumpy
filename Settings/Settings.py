__author__ = 'Diego'

import os

class Settings:


    MAIN_PATH = os.path.dirname(os.path.dirname(__file__))
    POSTS_PATH = os.path.join(MAIN_PATH, 'Data/posts')
    COOKIES_PATH = os.path.join(MAIN_PATH, 'Data/cookies')
    LOG_PATH = os.path.join(MAIN_PATH, 'logs/default.log')