# test page for data visualizations

import os
import uuid
import mimetypes

import numpy as np
import pandas as pd
import pygal
import json

from homeDataset import HomeDataset

import falcon

class VisualizationPage(object):
    # def __init__(self, storage_path):
    #     self.storage_path = storage_path

    def on_get(self,req,resp):

        # import matplotlib as mpl

        # import matplotlib.pyplot as plt
        # import seaborn as sns

        # outfile = open('user_uploads/user_file' + str(self.file_count) + '.csv', 'w')
        # outfile.write(req.stream.read())

        home_dataset = HomeDataset()

        data = home_dataset.get_data()
        resp.status = falcon.HTTP_200

        years = []
        chinook = []
        coho = []
        chum = []
        pink = []
        sockeye = []
        steelhead = []
        for row in data:
            # not the greatest practices but yolo
            # j is the dictionary of the json row
            j = json.loads(row)

            # Year
            ye = j["Year"]
            years.append(int(ye))

            # chinook
            ch = j["CHINOOK"]
            ch = 0 if ch == '' else ch
            chinook.append(int(ch))



            # pass


        j = json.loads(data[4])
        # resp.body = str(j["STEELHEAD"] == '')

        catch_bar_chart = pygal.Bar()
        catch_bar_chart.add('Chinook',chinook)
        catch_bar_chart.x_labels = map(str,years)
        catch_bar_chart.render_to_file('bar_chart.svg')
        resp.body = catch_bar_chart.render_data_uri()

        return catch_bar_chart.render_data_uri()


        # resp.body = str(chinook)



        # bar_chart = pygal.Bar()  # Then create a bar graph object
        # bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])  # Add some values
        # bar_chart.render_to_file('/tmp/bar_chart.svg')
        # bar_chart.render_to_png('/tmp/bar_chart.png')
        #
        # outfile = open('/tmp/test.txt','w')
        # outfile.write('\nHey! You have landed on the viz page!\n')
        # outfile.close()
        # infile = open('/tmp/test.txt','r')
        # content = infile.read()
        # infile.close()
        # resp.status = falcon.HTTP_200
        # resp.body = bar_chart.render_data_uri()
        # resp.body = content#('\nHey you! You have landed on the viz page!\n')


    def on_post(self, req, resp):
        pass
        # with('/test.txt', 'w') as outfile:
        #     outfile.write('hello world!\n')
        # ext = mimetypes.guess_extension(req.content_type)
        # filename = 'mats_test.jpg'
        # # filename = '{uuid}{ext}'.format(uuid=uuid.uuid4(), ext=ext)
        # # filename = '{uuid}{ext}'.format(uuid='mats_test', ext=ext)
        # image_path = os.path.join(self.storage_path, filename)
        #
        # with open(image_path, 'wb') as image_file:
        #     while True:
        #         chunk = req.stream.read(4096)
        #         if not chunk:
        #             break
        #
        #         image_file.write(chunk)
        #
        # resp.status = falcon.HTTP_201
        # resp.location = '/images/' + filename
        # # resp.location = '/images/' + 'mats_test.jpg'