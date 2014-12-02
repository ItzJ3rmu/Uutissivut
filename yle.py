import requests

from bs4 import BeautifulSoup

r = requests.get("http://yle.fi/uutiset/nordea_synkkyys_jatkuu/7663512")
r.encoiding = 'UTF-8'
soup = BeautifulSoup( r.text )

teksti = soup.find_all( class_='text' )

for i in teksti:
    print i

i.contents[0]

for string in i.stripped_strings:
        print(repr(string))
