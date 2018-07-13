
import requests
from bs4 import BeautifulSoup


def get_user_country():
    #generating request from user country of origin 
    #Parsing it through BeutifulSoup
    r = requests.get("https://whatismycountry.com/")
    return str(
                BeautifulSoup(r.text, 'html.parser').
                findAll("h3", {"class": "widget-title"})[0])[41:-5]
    
    