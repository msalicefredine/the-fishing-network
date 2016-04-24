import falcon
import csv
import json
from field_dictionary import FieldDictionary

class UploadPage(object):
    file_count = 0
    info_for_filename = {}

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # This is the default status

        page = open('views/upload.html', 'r')
        resp.stream = page
        resp.content_type = "text/html"

    def on_post(self, req, resp):
        file_name = 'user_file' + str(self.file_count) + '.csv'
        outfile = open(file_name, 'w')
        outfile.write(req.stream.read())
        outfile.close()
        self.file_count += 1
        fd = FieldDictionary()
        fd = self.parse_file(file_name, fd)
        self.info_for_filename[file_name] = fd
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({'filename': file_name})


    def clean_file(self, file_name):
        print "cleaning file\n"
        f = open(file_name, 'r+')
        lines = f.readlines()
        del lines[0]
        del lines[0]
        del lines[0]
        del lines[0]
        del lines[len(lines) - 1]
        print("cleaned file contents: \n")
        print (lines)
        f.seek(0)
        f.truncate()
        f.writelines(lines)
        f.close()

    def parse_file(self, file_name, fd):
        self.clean_file(file_name)
        f = open(file_name, 'r+')
        csv_f = csv.reader(f)
        file_lines = []
        for row in csv_f:
            file_lines.append(row)
        file_fields = file_lines[0]
        field_index = 0
        # duplicate_dict = {}
        for field in file_fields:
            ++field_index
            # valid name, not yet filled
            if field in fd.field_names_dictionary and not fd.field_names_dictionary[field]:
                fd.field_names_dictionary[field] = field_index
                fd.accepted.append(field)
                fd.unmatched_fields.remove(field)
            elif field in fd.field_names_dictionary:
                # duplicate field
                # delete for now.
                for line in file_lines:
                    del line[field]
                --field_index
                # duplicate_dict[field] = field_index
            else:
                fd.invalid.append(field)
        f.close()
        return fd
        # f.readlines()
        # f.write("\nAccepted: ")
        # f.writelines(fd.accepted)
        # f.write("\nInvalid: ")
        # f.writelines(fd.invalid, )
        # f.write("\nUnmatched Fields: ")
        # f.writelines(fd.unmatched_fields)
        # properly handle duplicates:
        # - figure out how to send back to the


