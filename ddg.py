import requests

query = "?q=presidents+of+the+united+states&"
url_ddg = f"https://api.duckduckgo.com/{query}"

response = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")

json_data = response.json()['RelatedTopics']




