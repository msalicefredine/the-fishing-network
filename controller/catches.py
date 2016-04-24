import falcon
from pymongo import MongoClient
import json
from bson import json_util
import csv

class Catches():
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # This is the default status

        client = MongoClient("localhost:27017")
        db = client.fishing_network
        table = db.catch

        results = []
        for doc in table.find():
            json_doc = json.dumps(doc, default=json_util.default)
            results.append(json_doc)

        resp.body = json.dumps(results)
        resp.content_type = "text/json"

    def on_post(self, req, resp):
        filename = req.get_param('catches', True)
        with open(filename, 'rb') as f:
            reader = csv.reader(f)
            fields = next(reader)
            client = MongoClient("localhost:27017")
            db = client.fishing_network
            table = db.catch
            for row in reader:
                input = {}
                for i in range(len(row)):
                    key = fields[i]
                    input[key] = row[i]
                table.insert(input)

        resp.status = falcon.HTTP_201
        resp.location = '/catches'