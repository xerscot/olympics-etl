from bs4 import BeautifulSoup

class Extract:

    def __init__(self, file_location = ""):
            self._file_location = file_location
            self._main_content = ""
            self.set_usable_content()

    def set_usable_content(self):
        f = open(self._file_location, "r")

        html = f.read()
        soup = BeautifulSoup(html, "html.parser")
        
        try:
            content = soup.find_all("main", class_="wrs-content")[0]
        except IndexError:
            f.close()
            content = ""
            return
        
        f.close()
        self._main_content = content

    def get_usable_content(self):
        return self._main_content

    def get_athlete_name(self):
        return self._main_content.find("h1").get_text().strip()

    def get_athlete_representation_country(self):
        return self._main_content.find("a", class_ = "country").get_text().strip()

    def get_discipline(self):
        discipline = ""
        for t in self._main_content.find_all("a"):
            disc = t.get("title", "")
            if "Olympic Schedule" in disc:
                d = disc[disc.find(" - "):]
                discipline = d[3:]
        return discipline

    