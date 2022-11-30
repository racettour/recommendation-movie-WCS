import requests as rq
from bs4 import BeautifulSoup
import PIL
import urllib
import matplotlib.pyplot as plt


def find_picture(index):
    # To fake a web browser
    navigator = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'
    cookies = dict(language='fr')

    url = 'https://www.imdb.com/title/' + index + '/'
    headers = {"Accept-Language": "fr_FR"}
    response = rq.get(url, headers={'User-Agent': navigator, "Accept-Language": "fr"})

    soup = BeautifulSoup(response.content, 'html.parser')

    resume = soup.findAll(class_= 'sc-16ede01-2 gXUyNh')
    text_resume = resume[0].text

    movie_data = soup.findAll(class_= 'ipc-lockup-overlay ipc-focusable')
    url_end = movie_data[0].attrs['href']

    url2 = "https://www.imdb.com" + url_end
    response2 = rq.get(url2, headers={'User-Agent': navigator})
    soup2 = BeautifulSoup(response2.content, 'html.parser')
    tt = soup2.findAll("div", {"class": "sc-7c0a9e7c-2 bkptFa"})

    url_image = tt[0].find("img")["src"]




    return  url_image, text_resume



index = "tt1793931"
image,text = find_picture(index)

print("fini")

