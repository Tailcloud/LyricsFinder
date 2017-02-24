#-*- coding: utf-8 -*-　　 
#-*- coding: cp950 -*-　
# coding: utf8
from urllib2 import Request, urlopen, URLError
from bs4 import BeautifulSoup
import urllib, urllib2
import sys
import re

def findUrl(NameofSong):
	request = urllib2.urlopen('https://mojim.com/'+NameofSong+'.html?u3')
	soup = BeautifulSoup(request,"html.parser")
	spans = soup('span',{'class':'mxsh_ss4'})
	for span in spans:
		spanas = span.findAll('a')
		for spana in spanas:
			cont = spana['title']
			print 'Title: '+ spana['title']
			print 'Url: http://mojim.com'+ spana['href']+'\n'
def findLyrics(Url):
	request = urlopen(Url)
	soup = BeautifulSoup(request,"html.parser")
	for article in soup.find('dd',{'class':'fsZx3'}):
		print article.extract().string
def main(argv1,argv2):
	if argv1 == 'Qurl':
		findUrl(argv2)
	if argv1 == 'Qlyric':
		findLyrics(argv2)

if __name__=="__main__": 
	print '*********************************************'
	print '* If you want to search the url of songs,   *'
	print '* Usage: python mojimLyrics.py Qurl title   *'
	print '* And then find lyrics with Qurl            *'            
	print '* Usage: python mojimLyrics.py Qlyric Qurl  *'
	print '*********************************************'
	main(sys.argv[1],sys.argv[2])
