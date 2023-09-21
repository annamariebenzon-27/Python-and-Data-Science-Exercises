from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen
from time import sleep
from datetime import datetime
def getGoldPrice():
    url="http://gold.org"
    req=urllib.request.urlopen(url)
    request_site=Request(url, headers={"User-Agent": "Safari/15.6.1"})
    webpage=urlopen(request_site).read()
    print(webpage[:500])
    page=req.read()
    scraping=BeautifulSoup(page)
    price=scraping.findAll("td",attrs={"id":"spotpriceCellAsk"})[0].text
    return price
with open("goldPrice.out", "w") as f:
    for x in range(0,60):
        sNow=datetime.now().strftime("%I:%M:%S%p")
        f.write("{0},{1}\n".format(sNow,getGoldPrice()))
        sleep(59)
