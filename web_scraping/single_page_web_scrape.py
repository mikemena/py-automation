from bs4 import BeautifulSoup
import requests

url = "https://scrapingclub.com/exercise/list_basic/?page=1"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
items = soup.find_all("div", class_="p-4")
print(items)
count = 1
for i in items:
    itemName = i.find("a").text if i.find("a") else "no element"
    itemPrice = i.find("h5").text if i.find("h5") else "no element"
    print("%s ) Price: %s, ItemName: %s" % (count, itemPrice, itemName))
    count = count + 1
