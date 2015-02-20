__author__ = 'Diego'
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
class WebDriverWrapper:


    def __init__(self):
        self.webDriver = None

    def start(self, url):
        self.webDriver = webdriver.Firefox()
        self.webDriver.implicitly_wait(10)
        self.webDriver.get(url)


    def setCookies(self, cookies):
        self.webDriver.delete_all_cookies()
        print("Setting cookies...")
        for cookie in cookies:
            self.webDriver.add_cookie({'name':cookie.name, 'value':cookie.value, 'domain' : cookie.domain, 'path':cookie.path, 'secure':True})
        print("Cookies Set")

    def sendCredentials(self, credentials):
        elem = self.webDriver.find_element_by_id("email")
        elem.send_keys(credentials[0])
        elem = self.webDriver.find_element_by_id("pass")
        elem.send_keys(credentials[1])
        elem.send_keys(Keys.RETURN)

    def stop(self):
        self.webDriver.quit()