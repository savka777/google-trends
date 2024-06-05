# Get the top trending results in the last 24 hours

from pytrends.request import TrendReq
OKGREEN = '\033[92m'
CEND = '\033[0m'

def get_top_trending_keywords():
    pytrends = TrendReq(hl='en-US', tz=360)
    
    trending_searches = pytrends.trending_searches(pn='united_kingdom')
    
    top_trending_keywords = trending_searches.head(10).values.flatten().tolist()
    
    return top_trending_keywords

top_trending_keywords = get_top_trending_keywords()
print("Top 10 trending keywords in your region in the last 24 hours:")
for i, keyword in enumerate(top_trending_keywords, 1):
    print(OKGREEN + f"{i}. {keyword}" + CEND)
