from fetch_ratings import fetch_gamefaqs
from commit_scrapings import commit

gamefaqs_ratings = fetch_gamefaqs()
commit(gamefaqs_ratings)
