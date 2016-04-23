# Home Page/Startup App Page

import falcon

class HomePage(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('\nHello, world! You found a page.\n')