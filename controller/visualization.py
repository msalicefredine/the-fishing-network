# test page for data visualizations

import falcon

class VisualizationPage(object):
    def on_get(self,req,resp):
        resp.status = falcon.HTTP_200
        resp.body = 'You have landed on the viz page!'