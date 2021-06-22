class Country:
    def __init__(self, countryID, db_obj):
        self.id = countryID
        self.name = db_obj.get_country_name(self.id)