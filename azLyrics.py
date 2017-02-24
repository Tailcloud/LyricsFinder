import sys
import re
from urllib.request import urlopen, URLError, HTTPError

from bs4 import BeautifulSoup

def main(artist, title):
        url = 'http://azlyrics.com/lyrics/'+artist+'/'+title +'.html'
        find(url, artist, title)
        
def find(url, artist, title):
    global response
    try: 
        response = urlopen(url)
    except URLError as e:
        print(e.reason)
        return
    except HTTPError as e:
        print(e.code)
        return
    read_lyrics = response.read()
    soup = BeautifulSoup(read_lyrics,"html.parser")
    lyrics = soup.find_all("div", attrs={ "class": False, "id": False })
    for x in lyrics:
    	lyrics = x.getText()
    	print(lyrics)
if __name__=="__main__":
	print( '*******************************************' )
	print( '* Usage: python3 azLyrics.py adele hello  *' )
	print( '*******************************************' )
	main(sys.argv[1],sys.argv[2])