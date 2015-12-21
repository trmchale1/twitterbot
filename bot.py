import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')
import requests
from bs4 import BeautifulSoup

data = raw_input("Enter the handle of the tweets you would like to see. ")
def printTweets(username):

    page = requests.get("https://twitter.com/"+username)
    
    soup = BeautifulSoup(page.content, 'html.parser')
#    print soup.prettify()
    tweets = soup.find_all('p')
    for tweet in tweets:
	print "-----------------------------------------"
	print tweet
 
#    print twit_text   
#	message = twit_text[0].contents[0]
#    for j in range(len(twit_text)):
#    print twit_text[j].contents[0]

printTweets(data)
