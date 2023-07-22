"""
requests를 사용해 검색하기
"""

import requests

params = dict(q="Sausages", format="json")
parsed = requests.get("http://api.duckduckgo.com", params=params).json()

results = parsed["RelatedTopics"]
for r in results:
    if "Text" in r:
        print(r["FirstURL"] + " - " + r["Text"])
