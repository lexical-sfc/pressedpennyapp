# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import json
import requests
raw_html_main = requests.get('http://209.221.138.252/AreaList.aspx')
# raw_html_california = requests.get('http://209.221.138.252/Locations.aspx?area=45')


overall_soup = BeautifulSoup(raw_html_main.text, 'html.parser')
# print(overall_soup)

# create dictionary of links
states_countries = dict()
for link in overall_soup.find_all("a"):
    #print(link["href"])
    if "Locations.aspx?area=" in link["href"]:
        #print(link.text.strip())
        states_countries[link.text.strip()] = link["href"]

# save locations to external file as a string, hence dump's'
with open('all_locations.txt','w') as file:
    file.write(json.dumps(states_countries))
# print(states_countries)
# state_tags = overall_soup.find_all('a')

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#a-function
#print(state_tags[8])


