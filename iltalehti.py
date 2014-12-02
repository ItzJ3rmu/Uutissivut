import requests

from bs4 import BeautifulSoup

r = requests.get("http://www.iltalehti.fi/uutiset/2014120218885176_uu.shtml")
r.encoiding = 'UTF-8'
soup = BeautifulSoup( r.text )

teksti = soup.find_all( 'isense' )

for i in teksti:
    print i

i.contents[0]

for string in i.stripped_strings:
        print(repr(string))
