__author__ = 'Diego'

from Post import Post
from Cookie import Cookie
from Settings.Settings import Settings


class DataExtractor:



    @staticmethod
    def extractPosts():
        posts = []
        with open(Settings.POSTS_PATH) as f:
            for line in f:
                if(not line.startswith('#')):
                    postData = line.split('==')
                    postName = postData[0]
                    postID = postData[1]
                    postGroupID = postData[2]
                    newPost = Post(name=postName, id=postID, groupId=postGroupID)
                    posts.append(newPost)
        return posts

    @staticmethod
    def extractCookies():
        cookies = []
        with open(Settings().COOKIES_PATH) as f:
            for line in f:
                if(not line.startswith('#')):
                    cookieData = line.split('==')
                    cookieName = cookieData[0]
                    cookieValue = cookieData[1].strip()
                    cookieDomain = '.facebook.com'
                    cookiePath = '/'
                    newCookie = Cookie(name=cookieName, value=cookieValue, domain=cookieDomain, path=cookiePath)
                    print(str(cookieValue))
                    cookies.append(newCookie)
        return cookies
