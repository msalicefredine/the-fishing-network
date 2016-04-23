import falcon

class UploadPage(object):
    file_count = 0

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # This is the default status

        page = open('views/upload.html', 'r')
        resp.stream = page
        resp.content_type = "text/html"

    def on_post(self, req, resp):
        outfile = open('user_uploads/user_file' + str(self.file_count) + '.csv', 'w')
        outfile.write(req.stream.read())

        self.file_count += 1

        resp.status = falcon.HTTP_200
