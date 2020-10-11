import webbrowser
import requests
import bs4
import re

#list = ['Auchentoshan']
list_of_links = []
list = []
file = open('whiskys.txt', 'r')
list = file.read().splitlines()
list = [element for element in list if element != '']
for element in list:
    res = requests.get('https://www.whisky.de/shop/index.php?lang=0&cl=search&searchparam=' + element) 
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    elems = soup.select('.article-title a[id]')
    for elem in elems[:2]:
        print(elem.get('href'))
        list_of_links.append(elem.get('href'))
   

list_of_links = set(list_of_links)
print(list_of_links)
for element in list_of_links:

    webbrowser.open(element)


