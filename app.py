import random

import requests
from flask import Flask, jsonify
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/')
def get_random_movie():
    # IMDB search returns 50 listings per request, accepting 'n' as a start position 
    # (ex. n = 9951 returns 9951-10,000) 

    page = random.randint(0, 9951) #IMDB's hardcoded limit for integer requests
    args = { 'title_type': 'feature', 'start': page}

    url = 'https://www.imdb.com/search/title/'
    r = requests.get(url, params=args)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    films = []
    for film in soup.findAll('div', class_='lister-item'):
        film = film.get_text()
        
        # Strips out all info about the film except for the title
        film = film[film.find(".") + 1 : film.find("(")]
        film = " ".join(film.split())
        films.append(film)
    return random.choice(films) 

if __name__ == '__main__':
    app.run("0.0.0.0", port=5000, debug=False)
