import database
import transform

class Load:

    def __init__(self, file_location = ""):
            self._file_location = file_location

    def first_database_check(self):
        obj = database.Database()
        tf = transform.Transform(self._file_location)
        columns = tf.get_all_columns()
        if obj._dbExists == False:
            obj.create_database()
            obj.create_competitors_table(columns)
            obj.insert_row(columns)

    def insert_competitor_data(self):
        obj = database.Database()
        tf = transform.Transform(self._file_location)
        columns = tf.get_all_columns()
        if obj._dbExists == True:            
            obj.insert_row(columns)