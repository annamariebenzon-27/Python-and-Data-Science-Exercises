from bs4 import BeautifulSoup
from random import seed
import requests
import urllib.request
from time import sleep
from datetime import datetime
def getGoldPrice():
    url="http://gold.org"
    session_obj=requests.Session()
    response=session.obj.get(url, headers={"User-Agent":"Safari/15.6.1"})
    print(response.status_code)
    req=urllib.request.urlopen(url)
    page=req.read()
    scraping=BeautifulSoup(page)
    price=scraping.findAll("td",attrs={"id":"spotpriceCellAsk"})[0].text
    return price
with open("goldPrice.out", "w") as f:
    for x in range(0,60):
        sNow=datetime.now().strftime("%I:%M:%S%p")
        f.write("{0},{1}\n".format(sNow,getGoldPrice()))
        sleep(59)
