import urllib2
from bs4 import BeautifulSoup
import requests
from twilio.rest import Client

#Get Info
pguri = raw_input("URL/URI of page you want to scrape (including http or https):  ")
t = float(raw_input ("How long do you want to wait in between scrapings? (in seconds, must be greater than one)  "))
message = raw_input("Do you want to get a message of the results?(y/n)  ")
if (message == "y"):
	twil = raw_input("Do you have a twilio account?(y/n)  ")
	if (twil == "y"):
		twill = raw_input("Do you want to use your twilio account?(y/n)  ")
		if (twill == "y"):
			account_sid = raw_input("What is your account sid?  ")
			auth_token = raw_input("What is your authorization token?  ")
			twilio_phone_number = raw_input("What is your Twilio phone number?  ")
			my_phone_number = raw_input("What is your phone number? (must be registered in twilio)  ")

#First Test
page = urllib2.urlopen(pguri)
soup = BeautifulSoup(page, "html.parser")
p_box = soup.find("p") #Inspects the paragraph tags of the page
words = p_box.text.strip()
words2 = words
#Send a message
def message():
	tclient = Client(account_sid, auth_token)
	tclient.messages.create(
		body=body,
		to=my_phone_number,
		from_=twilio_phone_number
	)
#Wait
import time
import winsound
if t < 1:
	print("time delay must be greater than one, read the directions next time")
	quit()
time.sleep(t)


#Second Test
while words2 == words:
	page = urllib2.urlopen(pguri)
	soup = BeautifulSoup(page, "html.parser")
	p_box2 = soup.find('p') #Same html elements as above
	words2 = p_box2.text.strip()
	time.sleep(t)
	
body = "Text has changed." #Make this whatever you like
print body
if (twill == "y"):
	message()
winsound.Beep(2500, 1200)
