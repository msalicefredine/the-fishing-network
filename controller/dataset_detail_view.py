import falcon

class DatasetDetailView(object):

    def on_get(self, req, resp, name):
        resp.status = falcon.HTTP_200  # This is the default status
        page = open('views/dataset_detail_view.html', 'r')
        resp.stream = page
        resp.content_type = "text/html"
