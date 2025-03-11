import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Sachin_Tendulkar"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

images = soup.select("img")

for image in images:
    src = image.get("src")

    if not src:
        continue  # Skip if no src attribute

    if src.startswith("//"):
        src = "https:" + src  # Add protocol
    elif src.startswith("/"):
        src = "https://en.wikipedia.org" + src  # Add domain

    print(src)
