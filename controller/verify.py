import falcon
from upload import UploadPage

class VerifyPage(object):
    delegate = None

    def __init__(self, delegate):
        self.delegate = delegate

    def on_get(self, req, resp, filename):
        resp.status = falcon.HTTP_200  # This is the default status
        info = self.delegate.info_for_filename.get(filename, None)
