import random
import re

import requests
from flask import Flask, jsonify
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def get_random_movie():

    # IMDB search returns 50 listings per request, accepting 'n' as a start position 
    # (ex. n = 9951 returns 9951-10,000) 

    page = random.randint(0, 9951) #IMDB's hardcoded limit for integer requests


    # TODO: If we scrape 50 films per IMBD scrape, we should serve up those 50 films
    # before making another scrape. This would greatly improve speed and make
    # less calls to IMDB.

    url = 'https://www.imdb.com/search/title/'
    args = { 'title_type': 'feature', 'start': page}
    r = requests.get(url, params=args)
    assert(r.status_code == 200)

    soup = BeautifulSoup(r.text, 'html.parser')
    
    films = []
    for film in soup.findAll('div', class_='lister-item mode-advanced'):
        rating = film.find('div', class_="inline-block ratings-imdb-rating")

        content = film.find('h3', class_="lister-item-header").get_text().split(".")[-1]
        content = content.replace("\n", " ")
        print(content)
        #print(content.split(" ("))
        #year = re.match("(\d{4})", year)
        #print(year)


        if rating:
            rating = rating.get_text().strip("\n")


        film = film.get_text()
        # Strips out all info about the film except for the title
        #s[s.find("(")+1:s.find(")")]


        # /^SW\d{4}$/

        film = film[film.find(".") + 1 : film.find("(")]
        film = " ".join(film.split())
        films.append(film)


        """response = {
                title: title,
                rating: rating



        } """
    return random.choice(films) 

if __name__ == '__main__':
    app.run("0.0.0.0", port=5000, debug=False)
