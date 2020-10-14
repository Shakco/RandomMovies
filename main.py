import requests, bs4, webbrowser, sys, time, random, os
from bs4 import BeautifulSoup


def main():
    movies = [
    'interstellar', 'Fast Furious', 'pulp fiction', 'inglorious bastards', 'moonlight', 'boyhood',
    'up in the air', 'slumdog millionaire', 'spectre', 'ps i love you', 'bruce almighty',
    'cornetto trilogy', 'i love you man', 'Paul', 'Chef', 'hail caesar', 'her'
    ]

    im_feeling_lucky(get_movie(movies))


def get_movie(movies):
    movie = movies[random.randint(0, len(movies) - 1)]
    #os.system("say 'looks like we are going to watch" + movie + "tonight'")
    return movie


def im_feeling_lucky(movie):
    sterm = movie + ' imdb '
    response = requests.get('https://www.google.com/search?q=' + sterm, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36 OPR/60.0.3255.69'})
    response.raise_for_status()
    bso = bs4.BeautifulSoup(response.text, "lxml")
    linkeles = bso.select('.r a')
    webbrowser.open_new(linkeles[0].get('href'))
    time.sleep(0.5)


main()