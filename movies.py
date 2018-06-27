import re
import urllib.request
from bs4 import BeautifulSoup as Soup
from bottle import route, run, template


url = 'http://www.cinemasteresina.com.br/'
new_url = []
full_url = []

with urllib.request.urlopen(url) as response:
    html = response.read()
    page = Soup(html, 'html.parser')
    movies = page.find_all("img", src = re.compile("/uploads/movie/poster/"))

    for i in range(len(movies)):
        full_url = "http://www.cinemasteresina.com.br{}".format(movies[i]["src"])
        full_url = re.sub(r"midi_", "", full_url)

        if full_url in new_url:
            continue
        else:
            new_url.append(full_url)


@route('/')
def index():
    return template("index.html", src = new_url)


run(host='localhost', port=8000)
