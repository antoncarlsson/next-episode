import requests
import sys
from bs4 import BeautifulSoup

NEXT_EPISODE_URL = "http://next-episode.net/{}"

class EpisodeInfoNotAvailableError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return "Error: " + self.message

class NextEpisode(object):
    def __init__(self, series_name):
        self._search(series_name)
        
        try:
            attr_list = list(self.__result.stripped_strings)[1:-2]
            if attr_list[0].startswith("Sorry"):
                raise EpisodeInfoNotAvailableError(attr_list[0])
        except AttributeError as e:
            e.args += ("Error: Could not find '{}' on {}".format(series_name,
                                                                  self.__url),)
            raise
        else:
            self.series_name  = series_name
            self.episode_name = attr_list[1]
            self.countdown    = attr_list[3]
            self.date         = attr_list[5]
            self.season       = attr_list[7]
            self.episode      = attr_list[9]
            
    def __str__(self):
        return "{}: {}\nIn {}. {}\nSeason {} Episode {}".format(self.series_name,
                                                                self.episode_name,
                                                                self.countdown,
                                                                self.date,
                                                                self.season,
                                                                self.episode)
    
    def _search(self, series_name):
        string        = series_name.replace(" ", "-")
        self.__url    = NEXT_EPISODE_URL.format(string)
        page          = requests.get(self.__url)
        soup          = BeautifulSoup(page.content, "lxml")
        self.__result = soup.find("div", id = "next_episode")
        
    
ne = NextEpisode(sys.argv[1])
print(ne)

