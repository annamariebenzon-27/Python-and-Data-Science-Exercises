from bs4 import BeautifulSoup
import requests

url='http://CNN.com'
response=requests.get(url)
soup=BeautifulSoup(response.content,'lxml')
print(soup.find('title').text)
