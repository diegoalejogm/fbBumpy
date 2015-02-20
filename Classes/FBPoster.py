__author__ = 'Diego'
import time

class FBPoster:

    # CONSTRUCTOR
    def __init__(self, driver):

        self.driver = driver


    def createAndDeletePost(self, post, message):

        # POST CREATION
        created = False
        while (not(created)):
            print("Creating Post " + "...")
            urlPost = 'https://developers.facebook.com/tools/explorer/145634995501895/?method=POST&path='+post.groupID+'_'+post.id+'%2Fcomments&message='+message
            print(urlPost)
            self.driver.get(urlPost)
            time.sleep(2)
            submitButton = self.driver.find_element_by_id('graph_submit')
            submitButton.click()
        #   time.sleep(2)
            print("Post Created")
            created = True


        # POST DELETION
        deleted = False
        while (not(deleted)):
            anchor = self.driver.find_element_by_css_selector('.json_string').find_element_by_tag_name('a')
            anchor.click()
    #       time.sleep(2)
            print("Deleting Post "+ "...")

            self.driver.get(str(self.driver.current_url).replace('GET','DELETE'))

            submitButton = self.driver.find_element_by_id('graph_submit')
            submitButton.click()
    #       time.sleep(2)
            print("Post Deleted")
            deleted = True