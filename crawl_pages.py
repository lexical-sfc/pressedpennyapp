import time
import random
import json
from bs4 import BeautifulSoup
import requests

with open('all_locations2.txt','r') as jsons_file:
    states_locations = json.load(jsons_file)


# for location in states_locations:
#     location_html = requests.get('http://209.221.138.252/' + states_locations[location])
#     #print('209.221.138.252/'+states_locations[location])
#     #print(location_html)
#     print(random.randint(6,13)/10.0)

raw_html_california = requests.get('http://209.221.138.252/Locations.aspx?area=45')
california_soup = BeautifulSoup(raw_html_california.text, 'html.parser')
#print(california_soup)

for table_row in california_soup.find_all('tr'):
    print(table_row)