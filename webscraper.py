import urllib2
from bs4 import BeautifulSoup
pguri = raw_input("URL/URI of page you want to scrape (including http or https):  ")
import requests
from twilio.rest import Client

#Get Info
account_sid = raw_input("What is your account sid? ")
auth_token = raw_input("What is your authorization token? ")
twilio_phone_number = raw_input("What is your Twilio phone number? ")
my_phone_number = raw_input("What is your phone number? (must be registered in twilio).")

#First Test
page = urllib2.urlopen(pguri)
soup = BeautifulSoup(page, "html.parser")
p_box = soup.find("p") #Inspects the paragraph tags of the page
words = p_box.text.strip()

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
t = float(raw_input ("How long do you want to run the program (in secs)?  "))
time.sleep(t)

#Second Test
page = urllib2.urlopen(pguri)
soup = BeautifulSoup(page, "html.parser")
p_box2 = soup.find('p') #Same html elements as above
words2 = p_box2.text.strip()
if (words2 != words):
	body = "Text has changed." #Make this whatever you like
	print body
	message()
	winsound.Beep(2500, 1200)
else:
	body = "Text has not changed." #Make this whatever you like
	print body
	message()
	winsound.Beep(250, 2000)
