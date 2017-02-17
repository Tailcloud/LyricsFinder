#-*- coding: utf-8 -*-　　 
#-*- coding: cp950 -*-　
# coding: utf8
from urllib2 import Request, urlopen, URLError
from bs4 import BeautifulSoup
import urllib, urllib2
import sys

def findLyrics(NameofSong):
	request = urllib2.urlopen('https://mojim.com/'+NameofSong+'.html?u3')
	soup = BeautifulSoup(request,"html.parser")
	for article in soup.findAll('a', title=True):
	    print "Title: "+article['title']
	    print "URL: http://mojim.com"+article['href']
	try:
		response = urlopen(request)
		result = response.read()
		print result
	except URLError, e:
	    print 'No kittez. Got an error code:', e
      
def downloadLyrics(Url):
	request = urlopen(Url)
	soup = BeautifulSoup(request,"html.parser")
	for article in soup.find('dd',{'class':'fsZx3'}):
		print article.extract().string
	try:
		response = urlopen(request)
		result = response.read()
		print result
	except URLError, e:
	    print 'No kittez. Got an error code:', e
      
def main(argv1,argv2):
	if argv1 == 'find':
		findLyrics(argv2)
	if argv1 == 'download':
		downloadLyrics(argv2)

if __name__=="__main__": 
	print '*********************************************'
	print '* If you want to search the lyricsfinder,   *'
	print '* Usage: python mojimLyrics.py find Ma-yu  *'
	print '* If you want to download it,               *'            
	print '* Usage: python mojimLyrics.py download url*'
	print '*********************************************'
	main(sys.argv[1],sys.argv[2])
