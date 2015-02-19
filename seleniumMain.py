#!/usr/bin/env python

__author__ = 'Diego'


try:
    import sys
    import time
    from selenium import webdriver
    from Post import Post
#    from pyvirtualdisplay import Display

    print("Starting Display...")
#    display = Display(visible=0, size=(800, 600))
#    display.start()
    print("Display started")


    groupID = '428018200570439'
    #rams = Post('800493409989581',groupID)
    cases = Post('806265299412392', groupID)
    amazon = Post('818658298173092', groupID)
    posts = [cases, amazon]

    #firefox start
    print("Starting Firefox...")
    driver= webdriver.Firefox()
    driver.implicitly_wait(10)
    print("Firefox Started")

    #facebook setup
    driver.get("https://www.facebook.com")

    #add facebook cookies
    print("Setting cookies...")
    driver.add_cookie({'name':'c_user', 'value':'520939739', 'path':'/', 'domain' : '.facebook.com'})
    driver.add_cookie({'domain' : '.facebook.com', 'name':'csm', 'value':'2', 'path':'/'})
    driver.add_cookie({'domain' : '.facebook.com', 'name':'datr', 'value':'ztyAVGFUEUL8wgJQG3yEOSPR', 'path':'/'})
    driver.add_cookie({'domain' : '.facebook.com', 'name':'fr', 'value':'0UvacA4Ydvcql5Fa6.AWXcxi6vn06jMGL9IMuv9WqJ-Hs.BUgNz6.mq.AAA.0.AWXDmO5q', 'path':'/'})
    driver.add_cookie({'domain' : '.facebook.com', 'name':'lu', 'value':'RwJINI6fCcIQdOH0JJKxpRig', 'path':'/'})
    driver.add_cookie({'domain' : '.facebook.com', 'name':'p', 'value':'-2', 'path':'/'})
    driver.add_cookie({'domain' : '.facebook.com', 'name':'presence', 'value':'EM417731331EuserFA2520939739A2EstateFDutF1417731331993Et2F_5b_5dElm2FnullEuct2F1417730722BEtrFnullEtwF761593334EatF1417731326694Esb2F0CEchFDp_5f520939739F0CC', 'path':'/'})
    driver.add_cookie({'domain' : '.facebook.com', 'name':'s', 'value':'Aa7aJEThV0bzCDqG.BUgNz6', 'path':'/'})
    driver.add_cookie({'domain' : '.facebook.com', 'name':'xs', 'value':'225%3A0oAAGGzoN0lsgQ%3A2%3A1417731322%3A18422', 'path':'/'})
    print("Cookies Set")
    #for cookie in driver.get_cookies():
    #    print "%s -> %s" % (cookie['name'], cookie['value'])
    #driver.get(defaultURL + '/' + groupID + '/' + str(postID))

    i = 0

    for post in posts:

    # CREATE POST
        created = False
        while (not(created)):
            try:
                print("Creating Post "+ str(i) + "...")
                urlPost = 'https://developers.facebook.com/tools/explorer/145634995501895/?method=POST&path='+post.groupID+'_'+post.id+'%2Fcomments&message=.'
                driver.get(urlPost)
                time.sleep(2)
                submitButton = driver.find_element_by_id('graph_submit')
                submitButton.click()
                time.sleep(2)
                print("Post Created")
                created = True
            except:
                pass
    #CAMBIAR DE URL


    # DELETE POST
        deleted = False
        while (not(deleted)):
            try:

                anchor = driver.find_element_by_css_selector('.json_string').find_element_by_tag_name('a')
                anchor.click()
                time.sleep(2)
                print("Deleting Post "+ str(i) + "...")

                driver.get(str(driver.current_url).replace('GET','DELETE'))

                submitButton = driver.find_element_by_id('graph_submit')
                submitButton.click()
                time.sleep(2)
                print("Post Deleted")
                deleted = True
            except:
                pass

        i=i+1

except:
    print "Unexpected error:", sys.exc_info()[0]
#    driver.close()
#    display.stop()
    raise
driver.close()
#display.stop()
print("Script End")
