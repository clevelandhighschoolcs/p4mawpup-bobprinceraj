import urllib2
from bs4 import BeautifulSoup
pguri = raw_input("URL/URI of page you want to scrape (including http or https):  ")

#First Test
page = urllib2.urlopen(pguri)
soup = BeautifulSoup(page, "html.parser")
p_box = soup.find("p") #Inspects the paragraph tags of the page
words = p_box.text.strip()

#Wait
import time
import winsound
t = float(raw_input ("How long do you want to run the program (in secs)?  "))
time.sleep(t)

#Second Test
page = urllib2.urlopen(pguri)
soup = BeautifulSoup(page, "html.parser")
p_box2 = soup.find('p') #Same html elements as above
words2 = p_box2.text.strip()
if (words2 != words):
	print "Text has changed." #Make this whatever you like
	winsound.Beep(2500, 1200)
else:
	print "Text has not changed." #Make this whatever you like
	winsound.Beep(250, 2000)
