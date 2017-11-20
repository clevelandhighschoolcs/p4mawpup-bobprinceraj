import urllib2
from bs4 import BeautifulSoup
pguri = "https://weather.com/weather/today/l/USOR0275:1:US" #URI of the page; feel free to replace it with whatever you like

#First Test
page = urllib2.urlopen(pguri)
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find('span', attrs={'classname': 'deg-feels'}) #This identifies the specific html elements you want to inspect
name = name_box.text.strip()
print name #optional

#Wait
import time
import winsound
t = input ("How long do you want to run the program (in secs)?  ")
tm = float(t)
time.sleep(tm)

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
