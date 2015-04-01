import requests

from bs4 import BeautifulSoup

import datetime

def nouda( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

	aika = datetime.date.today()

	numero = raw_input("Kuinka monta artikkelia? ")

	a = int(numero)

	for x in range(0,a):
		#teksti = soup.find_all( class_='news-item-wrapper' )
		linkki = soup.find_all('a', class_='news-item-headline')
		aika = soup.find_all( class_='news-item-date col')

		for string in linkki[x].stripped_strings:
	        	out.write(repr(string))


		for string in aika[x + 1].stripped_strings:
			out.write(repr(string))


if __name__ == '__main__':

	nouda("http://www.ampparit.com/eduskuntavaalit", file('ampparit.txt', 'w'))
