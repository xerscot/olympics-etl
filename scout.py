from bs4 import BeautifulSoup
import extract

class Scout:

    def __init__(self, file_location = ""):
            self._file_location = file_location
            self._column_number = 0 

    def get_number_of_columns(self):
        file_name = self._file_location

        f = open(file_name, "r")

        html = f.read()
        soup = BeautifulSoup(html, "html.parser")

        try:
            content = soup.find_all("main", class_="wrs-content")[0]
        except IndexError:
            self._column_number = 0 
            return

        bio_information = content.find_all("label")
        self._column_number = len(bio_information)