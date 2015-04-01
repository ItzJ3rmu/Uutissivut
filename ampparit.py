import requests

from bs4 import BeautifulSoup

import datetime

def nouda( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

        aika = datetime.date.today

	teksti = soup.find_all( class_='news-item-wrapper' )

	for string in teksti[0].stripped_strings:
	        out.write(repr(string))

if __name__ == '__main__':

	nouda("http://yle.fi/uutiset/nordea_synkkyys_jatkuu/7663512", file('yle.txt', 'w'))
