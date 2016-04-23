# Operations Controller for get and post requests

import falcon
from pymongo import MongoClient
import datetime
import json
from bson import json_util
import csv


class Operations(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # This is the default status

        client = MongoClient("localhost:27017")
        db = client.fishing_network
        table = db.operation

        results = []
        for doc in table.find():
            json_doc = json.dumps(doc, default=json_util.default)
            results.append(json_doc)

        resp.body = json.dumps(results)
        resp.content_type = "text/json"


    def on_post(self, req, resp):
        filename = req.get_param('operations', True)
        with open(filename, 'rb') as f:
            reader = csv.reader(f)
            fields = next(reader)
            client = MongoClient("localhost:27017")
            db = client.fishing_network
            table = db.operation
            for row in reader:
                locales = row[12].split("|")
                input = {
                    fields[0]: row[0],
                    fields[1]: row[1],
                    fields[2]: row[2],
                    fields[3]: row[3],
                    fields[4]: row[4],
                    fields[5]: row[5],
                    fields[6]: row[6],
                    fields[7]: row[7],
                    fields[8]: row[8],
                    fields[9]: row[9],
                    fields[10]: row[10],
                    fields[11]: row[11],
                    fields[12]: locales
                }
                table.insert(input)

        resp.status = falcon.HTTP_201
        resp.location = '/operations'