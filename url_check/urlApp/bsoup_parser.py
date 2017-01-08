from bs4 import BeautifulSoup
import requests
from ipwhois import IPWhois
import pywhois
import pythonwhois
import whois
from pprint import pprint
import datetime

def findLink(reference, url):
	r  = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data, 'lxml')
	results = soup.findAll(reference)
	return results
	
def checkItems(reference, url, getter):
	count = 0
	occur = 0
	items = findLink(reference, url)
	if items:
		for item in items:
			if not isItemFromSameHost(item, url, getter):
				occur = occur + 1
			count = count + 1
		return occur/float(count)
	return 0
	
def isItemFromSameHost(item, url, getter):
	newItem = str(item.get(getter))
	if newItem.count('.')<=1:
		return True
	elif url not in newItem:
		return False
	return True

def isOrgOnUrl(url):
	prefix = 'http://www'
	prefix2 = 'https://www'
	prefix3 = 'www'
	if (prefix in url) or (prefix2 in url) or (prefix3 in url):
		urlArr = url.split('.')[1:]
		url = '.'.join(urlArr)
	details = pythonwhois.get_whois(url)
	org = str(details['contacts']['admin']['organization'].split(' ')[0]).lower()
	if org in url:
		return True
	else:
		return False

def isValidFor6Months(url):
	prefix = 'http://www'
	prefix2 = 'https://www'
	prefix3 = 'www'
	if (prefix in url) or (prefix2 in url) or (prefix3 in url):
		urlArr = url.split('.')[1:]
		url = '.'.join(urlArr)
	details = pythonwhois.get_whois(url)
	today = datetime.datetime.now()
	delta = details['expiration_date'][0] - today 
	deltaDays = float(delta.days) - 180
	if deltaDays>0:
		return True
	else:
		return False




"""
domains = ['google.com', 'stackoverflow.com']
for dom in domains:
	domain = whois.query(dom)
	pprint(domain)

"""

"""
obj = IPWhois('www.google.com')

res=obj.lookup()

pprint(res)

w = pywhois.whois('google.com')
print w
"""

"""
url = "http://www.python.org"
reference = "a"
getter = "href"

links = findLink(reference, url)
for link in links:
    print(link.get('href'))

n = checkItems(reference, url, getter)
print n
"""


"""

r  = requests.get("http://www.python.org")
data = r.text
soup = BeautifulSoup(data)
imgs = soup.findAll("img")

for img in imgs:
    print(img.get('src'))

"""
"""
for link in soup.find_all('a'):
    print(link.get('href'))
"""
