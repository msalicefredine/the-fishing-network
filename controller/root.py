# Home Page/Startup App Page

import falcon

class HomePage(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        page = open('index.html', 'r')
        resp.stream = page
        resp.content_type = "text/html"