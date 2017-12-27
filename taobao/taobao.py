import io
import re
import sys
import webbrowser
from urllib import request
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Kevin_Bacon'
def getSoup(url):
    req = request.Request(url)
    #设置请求头
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
    try:
        response = request.urlopen(req)
        return BeautifulSoup(response.read(), "html.parser")
    except AttributeError as e:
        print(e)
    except HTTPError as e:
        print(e)

soup = getSoup(url)

for link in soup.find_all("a"):
    f = open('wikiLink.txt',"a+")
    if 'href' in link.attrs:
        f.write(link.attrs['href']+"\n")
    f.close()

for link in soup.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
    f = open('wikiLess.txt',"a+")
    if 'href' in link.attrs:
        f.write(link.attrs['href']+"\n")
    f.close()