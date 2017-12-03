import urllib2
from bs4 import BeautifulSoup
pguri = raw_input("URL/URI of the page you want to inspect:  ")

#First Test
page = urllib2.urlopen(pguri)
soup = BeautifulSoup(page, 'html.parser')
p_box = soup.find('span', attrs={'p'}) #Inspects the paragraph tags of the page
words = p_box.text.strip()
print words #optional

#Wait
import time
import winsound
t = float(raw_input ("How long do you want to run the program (in secs)?  "))
time.sleep(t)

#Second Test
page = urllib2.urlopen(pguri)
soup = BeautifulSoup(page, 'html.parser')
name_box2 = soup.find('span', attrs={'classname': 'deg-feels'}) #Same html elements as above
name2 = name_box2.text.strip()
if (name2 != name):
	print "Text has changed." #Make this whatever you like
	print name2 #optional
	winsound.Beep(2500, 1000)
else:
	print "Text has not changed." #Make this whatever you like
	winsound.Beep(250, 2000)
