import requests
from bs4 import BeautifulSoup

def fetch_amazon_deals():
    url = "https://www.amazon.in/deals"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    deals = []
    for item in soup.select(".DealGridItem-module__dealItem"):
        title = item.get_text(strip=True)
        deals.append({
            "title": title,
            "source": "Amazon"
        })
    return deals
