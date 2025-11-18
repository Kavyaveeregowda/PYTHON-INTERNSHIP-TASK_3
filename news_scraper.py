import requests
from bs4 import BeautifulSoup

url = "https://timesofindia.indiatimes.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
headlines = soup.find_all("h2")

with open("headlines.txt", "w", encoding="utf-8") as f:
    for h in headlines:
        title = h.get_text(strip=True)
        if title:
            f.write(title + "\n")

print("Headlines saved successfully!")