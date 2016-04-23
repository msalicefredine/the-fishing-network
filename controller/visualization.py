# test page for data visualizations

import falcon

class VisualizationPage(object):
    def on_get(self,req,resp):
        resp.status = falcon.HTTP_200
        resp.body = ('\nYou have landed on the viz page!\n')