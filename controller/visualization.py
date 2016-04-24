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


        # plotnum = req.get_param('plotnum')
        plotnum = 3

        # SPORT FISHING BY FISH TYPE
        if plotnum == 1:
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
            chum = df_sport['CHUM'].tolist()
            pink = df_sport['PINK'].tolist()
            sockeye = df_sport['SOCKEYE'].tolist()
            steelhead = df_sport['STEELHEAD'].tolist()


            bar_chart_sport = pygal.StackedBar(x_label_rotation=270)
            bar_chart_sport.title = "Sport Fishing Since 1974 by Fish Type"
            bar_chart_sport.add('Chinook',chinook)
            bar_chart_sport.add('Coho', coho)
            bar_chart_sport.add('Chum', chum)
            bar_chart_sport.add('Pink', pink)
            bar_chart_sport.add('Sockeye', sockeye)
            bar_chart_sport.add('Steelhead', steelhead)
            bar_chart_sport.x_labels = map(str,map(int,years))

            bar_chart_sport.render_data_uri()
            bar_chart_sport.render_to_file('bar_chart.svg')

            resp.status = falcon.HTTP_200
            resp.body = str(bar_chart_sport.render_data_uri())
            return bar_chart_sport.render_data_uri()
        elif plotnum == 2:
             home_dataset = HomeDataset()

             data = home_dataset.get_data()

             df = pd.DataFrame(
                 columns=('Year', 'Fisher Type', 'CHINOOK', 'COHO', 'CHUM', 'PINK', 'SOCKEYE', 'STEELHEAD'))

             for row in data:
                 j = json.loads(row)
                 vals = [to_int(j['Year']), j['Fisher Type'], to_int(j['CHINOOK']), to_int(j['COHO']),
                         to_int(j['CHUM']), to_int(j['PINK']), to_int(j['SOCKEYE']), to_int(j['STEELHEAD'])]
                 df.loc[len(df)] = vals

             # sport catches
             df_nontreaty = df[df['Fisher Type'] == 'Non-Treaty']

             years = df_nontreaty['Year'].tolist()
             chinook = df_nontreaty['CHINOOK'].tolist()
             coho = df_nontreaty['COHO'].tolist()
             chum = df_nontreaty['CHUM'].tolist()
             pink = df_nontreaty['PINK'].tolist()
             sockeye = df_nontreaty['SOCKEYE'].tolist()
             steelhead = df_nontreaty['STEELHEAD'].tolist()

             bar_chart_nontreaty = pygal.StackedBar(x_label_rotation=270)
             bar_chart_nontreaty.title = "Non Treaty Fishing Since 1974 by Fish Type"
             bar_chart_nontreaty.add('Chinook', chinook)
             bar_chart_nontreaty.add('Coho', coho)
             bar_chart_nontreaty.add('Chum', chum)
             bar_chart_nontreaty.add('Pink', pink)
             bar_chart_nontreaty.add('Sockeye', sockeye)
             bar_chart_nontreaty.add('Steelhead', steelhead)
             bar_chart_nontreaty.x_labels = map(str, map(int, years))

             bar_chart_nontreaty.render_data_uri()
             bar_chart_nontreaty.render_to_file('bar_chart.svg')

             resp.status = falcon.HTTP_200
             resp.body = str(df_nontreaty.to_string())
             return bar_chart_nontreaty.render_data_uri()
        elif plotnum == 3:
            home_dataset = HomeDataset()

            data = home_dataset.get_data()

            df = pd.DataFrame(
                columns=('Year', 'Fisher Type', 'CHINOOK', 'COHO', 'CHUM', 'PINK', 'SOCKEYE', 'STEELHEAD'))

            for row in data:
                j = json.loads(row)
                vals = [to_int(j['Year']), j['Fisher Type'], to_int(j['CHINOOK']), to_int(j['COHO']),
                        to_int(j['CHUM']), to_int(j['PINK']), to_int(j['SOCKEYE']), to_int(j['STEELHEAD'])]
                df.loc[len(df)] = vals

            # sport catches
            df_treaty = df[df['Fisher Type'] == 'Treaty']

            years = df_treaty['Year'].tolist()
            chinook = df_treaty['CHINOOK'].tolist()
            coho = df_treaty['COHO'].tolist()
            chum = df_treaty['CHUM'].tolist()
            pink = df_treaty['PINK'].tolist()
            sockeye = df_treaty['SOCKEYE'].tolist()
            steelhead = df_treaty['STEELHEAD'].tolist()

            bar_chart_treaty = pygal.StackedBar(x_label_rotation=270)
            bar_chart_treaty.title = "Treaty Fishing Since 1974 by Fish Type"
            bar_chart_treaty.add('Chinook', chinook)
            bar_chart_treaty.add('Coho', coho)
            bar_chart_treaty.add('Chum', chum)
            bar_chart_treaty.add('Pink', pink)
            bar_chart_treaty.add('Sockeye', sockeye)
            bar_chart_treaty.add('Steelhead', steelhead)
            bar_chart_treaty.x_labels = map(str, map(int, years))

            bar_chart_treaty.render_data_uri()
            bar_chart_treaty.render_to_file('bar_chart.svg')

            resp.status = falcon.HTTP_200
            resp.body = str(df_treaty.to_string())
            return bar_chart_treaty.render_data_uri()

        

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