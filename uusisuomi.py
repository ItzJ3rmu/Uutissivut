import requests

from bs4 import BeautifulSoup

def nouda( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

	for teksti in soup.find_all( class_='field field-name-body field-type-text-with-summary field-label-hidden' ):
		for p in teksti.find_all( 'p' ):

			for string in p.stripped_strings:
	        		out.write(repr(string))

if __name__ == '__main__':

	nouda("http://www.uusisuomi.fi/kotimaa/79148-ex-ministeri-kummastelee-jotkut-pitavat-lahes-rikollisena", file('uusisuomi.txt', 'w'))

