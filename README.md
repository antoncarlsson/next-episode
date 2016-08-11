Unofficial Python API for [Next-Episode](http://next-episode.net/).

Usage
==========

```python
from nextepisode import NextEpisode

# create a NextEpisode object
ne = NextEpisode()

# search for the next episode of "Mr. Robot"
s1 = ne.search("Mr. Robot")

# print all available info
print(s1)

# print just the episode's name
print(s1.episode_name)
```

Episode details available
==================

Attributes
----------

* **series_name** # the name of the series
* **episode_name** # the name of the episode
* **countdown** # how much time is left until the episode airs
* **date** # the date the episode airs
* **season** # which season the next episode belongs to
* **episode** # which episode number the next episode has