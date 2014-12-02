import requests

from bs4 import BeautifulSoup

r = requests.get("http://www.iltasanomat.fi/ulkomaat/art-1288789081654.html")
r.encoiding = 'UTF-8'
soup = BeautifulSoup( r.text )

teksti = soup.find_all( id="article-text" )

for i in teksti:
    print i

i.contents[0]

for string in i.stripped_strings:
        print(repr(string))
