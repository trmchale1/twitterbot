#Fuck ISIS
 
#We are Anonymous. We are Legion. We do not forgive. We do not forget. Expect us
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')
import requests
from bs4 import BeautifulSoup

#data = [line.strip() for line in open("targets.txt",'r')]

data = "realDonaldTrump"
def printTweets(username):

    page = requests.get("https://twitter.com/"+username)
    
    soup = BeautifulSoup(page.content, 'html.parser')
#    print soup.prettify()
    tweets = soup.find_all('p')
    for tweet in tweets:
	print "-----------------------------------------"
	print tweet
#    tweets = soup.find_all('li','js-stream-item')
    twit_text = soup('p',{'class': 'js-tweet-text'}) 
 
#    print twit_text   
#	message = twit_text[0].contents[0]
#    for j in range(len(twit_text)):
#    print twit_text[j].contents[0]

printTweets(data)
