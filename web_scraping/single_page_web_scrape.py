from bs4 import BeautifulSoup
import requests

url = "https://scrapingclub.com/exercise/list_basic/?page=1"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
items = soup.find_all("div", class_="p-4")
count = 1
for i in items:
    itemName = i.find("a").text
    itemPrice = i.find("h5").text
    print("%s ) Price: %s, Item Name: %s" % (count, itemPrice, itemName))
    count = count + 1
