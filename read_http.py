# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
raw_html_main = requests.get('http://209.221.138.252/AreaList.aspx')
raw_html_california = requests.get('http://209.221.138.252/Locations.aspx?area=45')


overall_soup = BeautifulSoup(raw_html_main.text, 'html.parser')
# print(overall_soup)

state_tags = overall_soup.find_all('a')

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#a-function
print(state_tags[8].content)