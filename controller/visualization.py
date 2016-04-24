# test page for data visualizations

import os
import uuid
import mimetypes

import falcon

class VisualizationPage(object):
    # def __init__(self, storage_path):
    #     self.storage_path = storage_path

    def on_get(self,req,resp):
        # outfile = open('user_uploads/user_file' + str(self.file_count) + '.csv', 'w')
        # outfile.write(req.stream.read())
        outfile = open('/tmp/test.txt','w')
        outfile.write('hello world!\n')
        outfile.close()
        infile = open('/tmp/test.txt','r')
        content = infile.read()
        infile.close()
        resp.status = falcon.HTTP_200
        resp.body = content#('\nHey you! You have landed on the viz page!\n')


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