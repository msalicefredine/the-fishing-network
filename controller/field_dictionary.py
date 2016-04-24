
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
        "vessel_length_mr",
        "Do Not Use"
    ]

    def __init__(self):
        self.field_names_dictionary = dict.fromkeys(FieldDictionary.field_names, False)
        self.accepted = [] # the list we will pass to the client of found field names
        self.invalid = [] # the list of field names that did not map to anything.
        self.unmatched_fields = FieldDictionary.field_names #remaining fields that haven't been mapped to.
        self.db_ready = False
