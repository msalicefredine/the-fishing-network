import falcon

class ViewDatasetsPage(object):
    file_count = 0

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # This is the default status

        page = open('views/view_datasets.html', 'r')
        resp.stream = page
        resp.content_type = "text/html"