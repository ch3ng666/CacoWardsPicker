'''Create List'''
from bs4 import BeautifulSoup as bs
import requests
import time

# WARNING THIS SCRIPT WILL CLEAR ALL PLAYED STATUS


### 1994 - 2003 ###
URL = 'https://doomwiki.org/wiki/Top_100_WADs_of_All_Time'
url_get = requests.get(URL)
html_get = bs(url_get.content, 'html.parser')

lista = []
for i in range(1994, 2004):
    tables_find = html_get.find('span',
                                class_='mw-headline',
                                string=f'{i}')

    tables_find = tables_find.parent.next_sibling.next_sibling

    tables_year_find = tables_find.findAllNext('li', limit=10)

    for j in range(10):
        year_table = tables_year_find[j]
        year = i
        title = year_table.find_next('a').text
        link = year_table.find_next('a', class_='external text').get('href')
        lista.append(f'{year} - {title} - {link} - 0')

with open('1994-2023.txt', 'w', encoding='utf-8') as wadlist:
    for i in lista:
        wadlist.write(f'{i}\n')

### 2004 - 2023 ###

for i in range(4, 24):
    year = 2000+i
    URL = f'https://doomwiki.org/wiki/Cacowards_{year}'
    url_get = requests.get(URL)
    html_get = bs(url_get.content, 'html.parser')

    tables_find = html_get.find(
        'span', id='Winners').parent.next_sibling.next_sibling

    tables_year_find = tables_find.find_all_next('li', limit=10)

    lista = []
    for j in range(10):
        year_table = tables_year_find[j]
        title = year_table.find_next('a').text
        link = year_table.find_next('a', class_='external text').get('href')
        lista.append(f'{year} - {title} - {link} - 0')

    with open('1994-2023.txt', 'a', encoding='utf-8') as wadlist:
        for i in lista:
            wadlist.write(f'{i}\n')

    time.sleep(5)
