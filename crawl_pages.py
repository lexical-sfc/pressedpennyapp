import time
import random
import json
from bs4 import BeautifulSoup
import requests
import pandas as pd

with open('all_locations2.txt','r') as jsons_file:
    states_locations = json.load(jsons_file)


# for location in states_locations:
#     location_html = requests.get('http://209.221.138.252/' + states_locations[location])
#     #print('209.221.138.252/'+states_locations[location])
#     #print(location_html)
#     print(random.randint(6,13)/10.0)

raw_html_california = requests.get('http://209.221.138.252/Locations.aspx?area=45')
california_soup = BeautifulSoup(raw_html_california.text, 'html.parser')
# print(california_soup.prettify())
# prettify is for printing/ presenting

# class of table with locations is
# <table border="1" cellspacing="0" class="tbllist" id="DG" rules="all">

'''
l = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text for tr in td]
    l.append(row)
pd.DataFrame(l, columns=["A", "B", ...])

# https://stackoverflow.com/questions/50633050/scrape-tables-into-dataframe-with-beautifulsoup
# search
'''

cali_table = california_soup.find_all('table',{"class":"tbllist"})
type(cali_table)
#this gives a list with one element
# https://pythonprogramminglanguage.com/web-scraping-with-pandas-and-beautifulsoup/
# the above tutorial made me realize that the content is placed as a single element in a list
# cali_dataframe = pd.read_html(str(cali_table[0])) # don't use pandas, can't pull links

#https://medium.com/@ageitgey/quick-tip-the-easiest-way-to-grab-data-out-of-a-web-page-in-python-7153cecfca58
# other_california_df = pd.read_html('http://209.221.138.252/Locations.aspx?area=45')
# print(other_california_df[0]) # don't use pandas, can't pull links
# https://datascience.stackexchange.com/questions/10857/how-to-scrape-a-table-from-a-webpage
# https://chihacknight.org/blog/2014/11/26/an-intro-to-web-scraping-with-python.html
cali_dict = {}
cali_list_of_lists = []
index = 0
'''
for row in cali_table[0].find_all('tr'):
    holder_row = []
    for column in row.find_all('td'):
        #holder_row.append(column)
        #holder_row.append(column.text)
        try:
            holder_row.append(column.find('span').text)
        except (TypeError,AttributeError):
            pass
    cali_list_of_lists.append(holder_row)
'''

# https://stackoverflow.com/questions/19595296/whats-the-correct-try-exception-for-nonetype-when-using-regexs-groups-funct
# This is because some of the closed locations don't have an address, so there is no span in the first column
for row in cali_table[0].find_all('tr'):
    cali_dict[index] = index
    index+=1
    holder_row = []
    for n, column in enumerate(row.find_all('td')):
        #holder_row.append((n, column))
        holder_row.append(column.text)
        #holder_row.append(column.find('span'))
        if n == 0:
            try:
                holder_row.append(column.find('span'))
                holder_row.append(column.find('span').text)
            except (TypeError,AttributeError):
                pass
    cali_list_of_lists.append(holder_row)
print(cali_list_of_lists[1])
#print(cali_list_of_lists[0].find_all('span'))
'''
table_rows = cali_table[0].find_all('tr') # note that this is also a list with one element
table_headers = [el for el in table_rows[0].find_all('td')]
table_row = [el for el in table_rows[0].find_all('td')]
table_col = [el for el in table_rows[1].find_all('td')]
# print(table_rows[0:5])
for el in table_headers:
    print(el)

print(len(table_rows))
print(len(table_col))
for el in table_col:
    print(el)
    print(el.text)
    print(el.find('span'))
    print(el.find('a'))


    # if 'Details.aspx?location=' in table_row.descendants:
    #     print('start of --------- row\n')
    #     for element in table_row.descendants:
    #         print('element ---------')
    #         print(element)


# create a list of lists, for each row of the table (find tr) for each el (find td)
# for each td, depending on the position, apply the right function.

'''