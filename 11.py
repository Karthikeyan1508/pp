import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

movies = soup.select(".ipc-title a")

for movie in movies[:10]:
    link = "https://www.imdb.com" + movie.get("href")
    movie_response = requests.get(link, headers=headers)

    if movie_response.ok:
        movie_soup = BeautifulSoup(movie_response.content, "html.parser")

        # Extract movie details
        try:
            movie_name = movie_soup.select_one("h1").get_text(strip=True)
        except AttributeError:
            movie_name = "N/A"

        try:
            movie_year = movie_soup.select_one(".sc-8c396aa2-2").get_text(strip=True)
        except AttributeError:
            movie_year = "N/A"

        try:
            movie_summary = movie_soup.select_one(".sc-16ede01-2").get_text(strip=True)
        except AttributeError:
            movie_summary = "N/A"

        # Print movie details
        print(f"Name: {movie_name}")
        print(f"Year: {movie_year}")
        print(f"Summary: {movie_summary}")
        print("--------------------")
