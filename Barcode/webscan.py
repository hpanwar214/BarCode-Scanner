
import requests
from bs4 import BeautifulSoup
import barcode as brc

# Enter the City Name
search=brc.BarcodeReader().decode("utf-8")
# URL

url = "https://www.google.com/search?&q="
url=url+search
print(url)
# Sending HTTP request
req = requests.get(url)
# Pulling HTTP data from internet
sor = BeautifulSoup(req.text, "html.parser")

product=sor.find('h3')
print(product.text);
# product =sor.find_all('h3') #'span', class_='aCOpRe'
# #sor.find("span", class_='aCOpRe').text aCOpRe LC20lb DKV0Md
# print(len(product))
# for pname in product:
# 	print(pname.text)

#print(temp)

# https://www.google.com/search?&q=9789390166268
# https://www.google.com/search?client=ubuntu&channel=fs&q={}&ie=utf-8&oe=utf-8'.format(b'9789390166268')
