import falcon
import csv
import json

class UploadPage(object):
    file_count = 0

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # This is the default status

        page = open('views/upload.html', 'r')
        resp.stream = page
        resp.content_type = "text/html"

    def on_post(self, req, resp):
        file_name = 'user_uploads/user_file' + str(self.file_count) + '.csv'
        outfile = open(file_name, 'w')
        outfile.write(req.stream.read())
        outfile.close()
        self.file_count += 1
        self.parse_file(file_name)
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({})


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

    def parse_file(self, file_name):
        self.clean_file(file_name)
        fd = FieldDictionary()
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
        f.readlines()
        f.write("\nAccepted: ")
        f.writelines(fd.accepted)
        f.write("\nInvalid: ")
        f.writelines(fd.invalid, )
        f.write("\nUnmatched Fields: ")
        f.writelines(fd.unmatched_fields)
        # properly handle duplicates:
        # - figure out how to send back to the


class FieldDictionary(object):
    field_names = [
        "user_name",
        "user_address",
        "user_phone",
        "user_email",
        "user_type",
        "dealer_id",
        "dealer_name",
        "dealer_address",
        "is_sold",
        "trip_start",
        "trip_end",
        "trip_time",
        "trip_locales",
        "published_date",
        "licence_prefix",
        "licence_root",
        "licence_suffix",
        "licence_tab",
        "licence_status",
        "liel_seq",
        "licence_issue_date",
        "licence_expiry_date",
        "fishery_group",
        "area",
        "licence_type",
        "licence_holder_type",
        "licence_holder_first_name",
        "licence_holder_middle_name",
        "licence_holder_last_name",
        "licence_holder_vrn",
        "licence_holder_vessel",
        "licence_operator_first_name",
        "licence_operator_middle_name",
        "licence_operator_last_name",
        "licence_operator_vpn",
        "licence_operator_vessel",
        "vessel_owner_first_name",
        "vessel_owner_middle_name",
        "vessel_owner_last_name",
        "vessel_dot_id",
        "foreign_vessel",
        "vess_latest_lic_issue_dt",
        "vessel_length_mr"
    ]

    def __init__(self):
        self.field_names_dictionary = dict.fromkeys(FieldDictionary.field_names, False)
        self.accepted = [] # the list we will pass to the client of found field names
        self.invalid = [] # the list of field names that did not map to anything.
        self.unmatched_fields = FieldDictionary.field_names #remaining fields that haven't been mapped to.

