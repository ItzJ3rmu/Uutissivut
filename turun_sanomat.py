import requests

from bs4 import BeautifulSoup

def nouda( url , out ):

	r = requests.get( url )
	r.encoding = 'UTF-8'
	soup = BeautifulSoup( r.text )

	teksti = soup.find_all( class_='text' )

	for string in teksti[0].stripped_strings:
	        out.write(repr(string))

if __name__ == '__main__':
	
	nouda("http://www.ts.fi/uutiset/kotimaa/707662/Nuorten+sosiaalisen+median+kaytto+huolestuttaa+poliisia", file('turun_sa.txt', 'w'))
