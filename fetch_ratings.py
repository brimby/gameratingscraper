import requests
import time

from bs4 import BeautifulSoup

def fetch_gamefaqs():
    # col_titles is the column titles in the db. Will have to put more safeguards
    # in place so that if gamefaqs rearranged the HTML the columns won't get
    # mixed up.
    col_titles = ['rank', 'platform', 'name', 'rating', 'difficulty', 'length']
    # ratings will be populated after the scraping takes place. The "end product"
    # to be written to db
    ratings = []
    page_failures = 0
    current_page = 0
    base_url = "https://gamefaqs.gamespot.com/games/rankings?min_votes=2&page="
    # Headers are required not to get 403 Forbidden HTTP response
    headers = {'user-agent': 'my-app/0.0.1'}

    while page_failures < 10:
        page_fetched = False
        page_tries = 0
        while page_fetched is False and page_tries < 3:
            page = requests.get(base_url + str(current_page), headers=headers)
            if page.status_code != requests.codes.ok:
                # The script tried to get the page and failed. Retries 2 more times.
                page_tries += 1
                time.sleep(5)
                print "Try failed = " + str(current_page)
                continue
            else:
                page_fetched = True

        if page_fetched is False:
            # The script tried 3 times to fetch the page and failed. Next page.
            page_failures += 1
            current_page += 1
            print "page failed = " + str(current_page)
            continue

        source = page.text
        soup = BeautifulSoup(source, 'lxml')

        rows = soup.select('tbody tr')
        if not rows:
            break
        for row in rows:
            ratings.append(dict(zip(col_titles, row.stripped_strings)))
            try:
                float(ratings[-1]['rating'])
            except ValueError:
                ratings[-1]['rating'] = None
            try:
                float(ratings[-1]['difficulty'])
            except ValueError:
                ratings[-1]['difficulty'] = None
            try:
                ratings[-1]['length'] = ratings[-1]['length'].replace('+', '')
                float(ratings[-1]['length'])
            except ValueError:
                ratings[-1]['length'] = None

        current_page +=1

    return ratings
