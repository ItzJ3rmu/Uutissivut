import requests

from bs4 import BeautifulSoup

r = requests.get("http://prakticum.fi")
r.encoiding = 'UTF-8'
soup = BeautifulSoup( r.text )

teksti = soup.find_all( class_="viivax" )

for i in teksti:
    print i

i.contents[0]

for string in i.stripped_strings:
        print(repr(string))
