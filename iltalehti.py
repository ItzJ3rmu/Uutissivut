import requests

from bs4 import BeautifulSoup

def nouda( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

	teksti = soup.find_all( 'isense' )

	for string in teksti[0].stripped_strings:
	        out.write(repr(string))

if __name__ == '__main__':
	
	nouda("http://www.iltalehti.fi/uutiset/2014120218885176_uu.shtml", file('ilta.txt', 'w'))
