import requests, random
from flask import Flask, jsonify
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def get_random_movie():
    page = random.randint(0, 90) * 100 + 51
    url = 'https://www.imdb.com/search/title?title_type=feature&view=simple&start=' + str(page) + '&ref_=adv_nxt'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    films = []
    for film in soup.findAll('div', class_='lister-item'):
        film = film.get_text()
        film = film[film.find(".") + 1 : film.find("(")]
        film = " ".join(film.split())
        films.append(film)

    return(str(films[random.randint(0,len(films))]))
