# test page for data visualizations

import os
import uuid
import mimetypes

import numpy as np
import pandas as pd
import json
import pygal

from homeDataset import HomeDataset

import falcon

class VisualizationPage(object):
    # def __init__(self, storage_path):
    #     self.storage_path = storage_path

    def on_get(self,req,resp):

        def to_int(integer_string):
            if integer_string == '':
                return 0
            else:
                return int(integer_string)


        home_dataset = HomeDataset()

        data = home_dataset.get_data()

        df = pd.DataFrame(columns=('Year', 'Fisher Type', 'CHINOOK', 'COHO',  'CHUM',  'PINK', 'SOCKEYE', 'STEELHEAD'))

        for row in data:
            j = json.loads(row)
            vals = [to_int(j['Year']), j['Fisher Type'], to_int(j['CHINOOK']), to_int(j['COHO']),  to_int(j['CHUM']),  to_int(j['PINK']), to_int(j['SOCKEYE']), to_int(j['STEELHEAD'])]
            df.loc[len(df)] = vals

        # sport catches
        df_sport = df[df['Fisher Type']=='Sport']

        years = df_sport['Year'].tolist()
        chinook = df_sport['CHINOOK'].tolist()
        coho = df_sport['COHO'].tolist()

        bar_chart_sport = pygal.StackedBar(x_label_rotation=270)
        bar_chart_sport.add('Chinook',chinook)
        bar_chart_sport.add('Coho', coho)
        bar_chart_sport.x_labels = map(str,map(int,years))

        bar_chart_sport.render_data_uri()
        bar_chart_sport.render_to_file('bar_chart.svg')

        resp.status = falcon.HTTP_200
        resp.body = str(bar_chart_sport.render_data_uri())

        return bar_chart_sport.render_data_uri()

        # import matplotlib as mpl

        # import matplotlib.pyplot as plt
        # import seaborn as sns

        # outfile = open('user_uploads/user_file' + str(self.file_count) + '.csv', 'w')
        # outfile.write(req.stream.read())

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