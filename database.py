import sqlite3
from sqlite3 import Error
from os.path import exists

class Database:

    def __init__(self):
        self._db_file_location = "data/olympics.db"
        self._dbExists = exists(self._db_file_location)

    def create_database(self):    
        try:
            connection = sqlite3.connect(self._db_file_location)
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            if connection:
                connection.close()

    def create_competitors_table(self, structure):
        # iterate through the structure and build up the command line
        try:
            connection = sqlite3.connect(self._db_file_location)
            cursor = connection.cursor()
            # Encountered some rogue field names
            command = "CREATE TABLE competitors (competitor_id INTEGER PRIMARY KEY, Hand TEXT, Training TEXT, NationalTeam TEXT, PreviousNames TEXT, Music TEXT, Choreographer TEXT, "
            fields = ""
            for key in structure:
                temp_key = key
                if "height" in temp_key.strip().lower():
                    temp_key = "Height"
                fields = fields + temp_key + " TEXT, "
            command = command + fields[:-2] + ")"
            cursor.execute(command)
        except Error as e:
            print(e)
        finally:
            if connection:
                connection.close()

    def insert_row(self, row):
        #extract data from the dictionary and insert below
        if len(row) == 0:
            return
        fields = ""
        values = ""
        try:
            connection = sqlite3.connect(self._db_file_location)
            cursor = connection.cursor()
            command = "INSERT INTO competitors "            
            for k, v in row.items():
                temp_key = k
                if "height" in temp_key.strip().lower():
                    temp_key = "Height"
                fields = fields + temp_key + ", "
                values = values + "'" + v + "', "
            command = command + "(" + fields[:-2] + ") VALUES (" + values[:-2] + ")"
            cursor.execute(command)
            connection.commit()
        except Error as e:
            print(e)
        finally:
            if connection:
                connection.close()