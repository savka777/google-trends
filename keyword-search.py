# Trending words based on keyword search

from pytrends.request import TrendReq # type: ignore
OKGREEN = '\033[92m'
CEND = '\033[0m'

def get_trending_keywords(keyword, geo='GB'):
    pytrends = TrendReq(hl='en-GB', tz=0)
    pytrends.build_payload([keyword], cat=0, timeframe='now 1-d', geo=geo, gprop='')
    trending_data = pytrends.related_queries()[keyword]['top']
    
    if trending_data is not None:
        return trending_data['query'].tolist()
    else:
        return []

# Example usage
keyword = input("Keyword to search: ")
trending_keywords = get_trending_keywords(keyword)
for i, keyword in enumerate(trending_keywords, 1):
    print(OKGREEN + f"{i}. {keyword}" + CEND)
