import io
import re
import sys
import requests
import webbrowser
from urllib import request
from bs4 import BeautifulSoup

url = 'https://www.zhihu.com/'
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

def getZhihuData():
    try:
        session = requests.Session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
                   'Cookie': 'q_c1=830b52e77c30409fb0c03a6c36ed7e63|1514300443000|1514300443000; _zap=3cd1eabf-e7ce-43e3-b098-a69fa88d8788; aliyungf_tc=AQAAAD4z3EI7JgkAbOzidBQQ7E8TjQlF; l_n_c=1; d_c0="ADBh1KWT5wyPThob7iTQn68a9vT0d0hW9ak=|1514479282"; l_cap_id="ZTliMWFlNmI2M2YzNDk3ZGI0MWU3ZjhhNGY1M2U5OTI=|1514483410|ecacb36a8aef31e43f150c7c312114d0b60416e9"; r_cap_id="MDExN2JkYzBmZDk1NDViMWE5YWUyZDEyYjYzMmEzZjQ=|1514483410|2c6910d2d5d7e1d17df8a1617e00340a44fe1221"; cap_id="NmIzNjhmNDVhNDQxNGEwMGJjZDM1MGJjM2QxNDcxNzk=|1514483410|eeedff31b25f03c3285acad121572f64a9961e0c"; _xsrf=e3cfaf72-0523-4b2f-a1e5-d3ea99a765c6; capsion_ticket="2|1:0|10:1514483453|14:capsion_ticket|44:NDM2Yzg5Y2U2YjUxNGE2Y2I1NTk0MTkxZTQ5NTUxNWU=|b2ee876317b4465c899225436511f8fdde31ddda9fc4cae3a1e1c88232fcdc17"; z_c0="2|1:0|10:1514483481|4:z_c0|92:Mi4xVDdGREFnQUFBQUFBTUdIVXBaUG5EQ1lBQUFCZ0FsVk5HWDB5V3dDSC13RjA2UUZqVmhMWk5rUDh3NHRSeklOUzN3|3db9287b0103da575b98b8d7603f8977f07c6927f8f321c5c6e61a78f8a88a72"'}
        html = session.get('https://www.zhihu.com/', headers=headers).content
        soup = BeautifulSoup(html)
        imgLinks = soup.findAll("img", {'src': re.compile("^.*?\.jpg$")})
        imgLinks.extend(soup.findAll("meta", {'content': re.compile("^.*?\.jpg$")}))
        x=1
        for link in imgLinks:
            url = ""
            if "src" in link.attrs:
                url = link.attrs["src"]
            else:
                url = link.attrs["content"]
            request.urlretrieve(url, 'D:/images/%s.jpg' % x)
            print(url)
            x=x+1
    except TypeError as e:
        print(e)
    finally:
        a = 1

getZhihuData()
#soup = getSoup(url)



def handerLinks():
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