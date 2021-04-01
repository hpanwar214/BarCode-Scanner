
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
