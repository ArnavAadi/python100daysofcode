import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
page = response.text

# Write your code below this line 👇

soup = BeautifulSoup(page, "html.parser")
title_tags = soup.find_all("h3", class_="title")
titles = [title.text for title in title_tags]

with open("data.txt", "a") as file:
    for num in range(99, -1, -1):
        file.write(f"{titles[num]}\n")
