from bs4 import BeautifulSoup
import urllib.request
from urllib import request
from urllib.request import Request, urlopen
from time import sleep
from datetime import datetime
from urllib.request import Request, urlopen

req = Request(
    url='https://www.gold.org', 
    headers={'User-Agent': 'Mozilla/5.0'}
)
webpage = urlopen(req).read()
 
url = "https://www.gold.org"

def getGoldPrice():
    url = "https://www.gold.org"
    req = urllib.request.urlopen(url)
    page = req.read()
    scraping = BeautifulSoup(page)
    price = scraping.findAll("td",attrs={"id":"spotpriceCellAsk"})[0].text
    return price


with open("goldPrice.out","w") as f:
    for x in range(0,10):
        sNow = datetime.now().strftime("%I:%M:%S%p")
        f.write("{0}, {1} \n ".format(sNow, getGoldPrice()))
        sleep(1)
