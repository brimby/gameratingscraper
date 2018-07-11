# Game Rating Scraper

When the script gameratingscraper.py is run it crawls http://gamefaqs.com and retrieves
quality ratings, difficulty ratings, and game length estimations for every game
on the website. It then records the values to a local MySQL database.

## Roadmap

The plan is to crawl other sites besides gamefaqs and combine the ratings together,
but first I'm going to start another project which will be the API for retrieving
this data from a database. After that API is complete I'll come back to this
project and expand its scraping targets.

The eventual goal for the combination of these two projects is to have a better
source of game ratings info for Retropie or any other games library applications
that want rating info with a larger sample size than what is currently available
from open database APIs.
