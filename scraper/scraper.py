# Referenced from https://gist.github.com/julia-git/5fb77bbfbbf08a5b9f1f8e7e739d9817#file-webscraping_nyc_mta-py

# Import libraries
import requests
from bs4 import BeautifulSoup

def getTemp():
    url = 'https://freemeteo.co.uk/weather/ascot/current-weather/location/?gid=2656992&language=english&country=united-kingdom'

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    return(soup.find(class_="temp").getText())
