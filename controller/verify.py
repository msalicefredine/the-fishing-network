import falcon
import json
from field_dictionary import FieldDictionary
from upload import UploadPage

class VerifyPage(object):
    delegate = None

    def __init__(self, delegate):
        self.delegate = delegate

    def on_get(self, req, resp, filename):
        resp.status = falcon.HTTP_200  # This is the default status
        info = self.delegate.info_for_filename.get(filename, None)
        field_dict = self.delegate.info_for_filename[filename]

        if req.params.get("load_data", None) is None:
            resp.status = falcon.HTTP_200  # This is the default status

            page = open('views/verify.html', 'r')
            resp.stream = page
            resp.content_type = "text/html"
        else:
            resp.status = resp.status = falcon.HTTP_200
            resp.body = json.dumps({'accepted': field_dict.accepted,
                                    'invalid': field_dict.invalid,
                                    'unmatched': field_dict.unmatched_fields})