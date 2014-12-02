import requests

from bs4 import BeautifulSoup

r = requests.get("http://www.hs.fi/ulkomaat/a1417488621135")
r.encoiding = 'UTF-8'
soup = BeautifulSoup( r.text )

teksti = soup.find_all( id="article-text" )

for i in teksti:
    print i

i.contents[0]

for string in i.stripped_strings:
        print(repr(string))
