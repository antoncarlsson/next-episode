import requests
from bs4 import BeautifulSoup

class EpisodeInfoNotAvailableError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return "Error: " + self.message

class Search(object):
    def __init__(self, series_name):
        string = series_name.replace(" ", "-")
        url    = "http://next-episode.net/" + string
        page   = requests.get(url, headers = { "User-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36" })
        soup   = BeautifulSoup(page.content, "lxml")
        result = soup.find("div", id = "next_episode")
             
        try:
            attr_list = list(result.stripped_strings)[1:-2]
            if attr_list[0].startswith("Sorry"):
                raise EpisodeInfoNotAvailableError(attr_list[0])
        except AttributeError as e:
            e.args += ("Error: Could not find '{}' on {}".format(series_name, url),)
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
             

class NextEpisode(object):
    def __init__(self):
        pass 
    
    def search(self, series_name):
        return Search(series_name)

