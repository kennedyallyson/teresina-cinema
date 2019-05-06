import re

from bs4 import BeautifulSoup as Soup
from bottle import route, run, template
import requests


def search_movies():
    full_url = []
    new_url = []

    with requests.get('http://www.cinemasteresina.com.br/') as response:
        html = response.text
        page = Soup(html, 'html.parser')
        movies = page.find_all("img", src = re.compile("/uploads/movie/poster/"))

        for i in range(len(movies)):
            full_url = "http://www.cinemasteresina.com.br{}".format(movies[i]["src"])
            full_url = re.sub(r"midi_", "", full_url)

            if full_url in new_url:
                continue
            else:
                new_url.append(full_url)
    return new_url


@route('/')
def index():
    new_url = search_movies()
    return template("views/index.html", src = new_url)


def main():
    run(host='localhost', port=8000)


if __name__=='__main__':
    main()
