import falcon
from pymongo import MongoClient
import json

class ViewDatasetsPage(object):
    file_count = 0

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # This is the default status

        if req.params.get("get_tables", None) is not None:
            resp.data = self.get_tables()
            resp.content_type = "text/json"
        else:
            page = open('views/view_datasets.html', 'r')
            resp.stream = page
            resp.content_type = "text/html"

    def get_tables(self):
        client = MongoClient("localhost:27017")
        db = client.fishing_network
        names = db.collection_names(include_system_collections = False)
        names.remove('home_page')
        return json.dumps(names)