# things.py

# Let's get this party started!
import falcon
import json
from bson import json_util
from pymongo import MongoClient

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class ThingsResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status

        client = MongoClient("localhost:27017")
        db = client.test_database
        test_column = db.test_column

        test = {"squid": "mollusc"}
        test_column.insert(test)

        #index_file = open('index.html', 'r')
        results = []
        for doc in test_column.find():
            json_doc = json.dumps(doc, default=json_util.default)
            results.append(json_doc)

        resp.body = json.dumps(results)
        resp.content_type = "text/json"

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
things = ThingsResource()

# things will handle all requests to the '/things' URL path
app.add_route('/things', things)