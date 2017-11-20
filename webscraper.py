import urllib2
from bs4 import BeautifulSoup

#First Test
page = urllib2.urlopen('https://weather.com/weather/today/l/USOR0275:1:US')
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find('span', attrs={'classname': 'deg-feels'})
name = name_box.text.strip()
print name

#Wait
import time
import winsound
t = input ("How long do you want to run the program (in secs)?  ")
tm = float(t)
time.sleep(tm)

#Second Test
page = urllib2.urlopen('https://weather.com/weather/today/l/USOR0275:1:US')
soup = BeautifulSoup(page, 'html.parser')
name_box2 = soup.find('span', attrs={'classname': 'deg-feels'})
name2 = name_box2.text.strip()
if (name2 != name):
	print "Text has changed."
	print name2
	winsound.Beep(2500, 1000)
else:
	print "Text has not changed."
	winsound.Beep(250, 2000)
