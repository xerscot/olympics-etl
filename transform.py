import extract

class Transform:

    extract_object = None

    def __init__(self, file_location = ""):
        global extract_object
        self._file_location = file_location
        self._main_content = ""
        extract_object = extract.Extract(self._file_location)
        self.get_transform_content()

    def get_transform_content(self):
        global extract_object
        self._main_content = extract_object.get_usable_content()

    def get_columns(self):
            bio_information = self._main_content.find_all("label")

            column_data = {}

            for b in bio_information:
                column = b.get_text()    
                cell = b.parent.text
                cell = cell.replace(column, "")
                column = column.replace(":", "")
                column = column.strip()
                cell = cell.replace("\n", "").strip()
                cell = cell.replace("'", "''").strip()                                
                cell = cell.replace(":", "").strip()
                column = column.title()
                column = column.replace(" ", "")
                column = column.replace("'", "''")
                column_data[column] = cell 
            
            return column_data

    def get_all_columns(self):
        global extract_object
        ds = {}

        if self._main_content == "":
            return ds

        ds["FullName"] = extract_object.get_athlete_name().replace("'", "''")
        ds["CountryOfRepresentation"] = extract_object.get_athlete_representation_country().replace("'", "''")
        ds["Discipline"] = extract_object.get_discipline().replace("'", "''")

        ds_continued = self.get_columns()

        row = ds | ds_continued

        return row