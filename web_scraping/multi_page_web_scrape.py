from bs4 import BeautifulSoup
import requests

url = "https://scrapingclub.com/exercise/list_basic/?page=1"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
items = soup.find_all("div", class_="p-4")
# print(items)
count = 1
for i in items:
    itemName = i.find("a").text if i.find("a") else "no element"
    itemPrice = i.find("h5").text if i.find("h5") else "no element"
    # print("%s ) Price: %s, ItemName: %s" % (count, itemPrice, itemName))
    count = count + 1
pages = soup.find("nav", class_="pagination")
urls = []
links = soup.find_all("a")
for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum != None:
        x = link.get("href")
        urls.append(x)
count = 1
for i in urls:
    newUrl = url + i
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, "lxml")
    items = soup.find_all("div", class_="p-4")
    # print(items)

    for i in items:
        itemName = i.find("a").text if i.find("a") else "no element"
        itemPrice = i.find("h5").text if i.find("h5") else "no element"
        print("%s ) Price: %s, ItemName: %s" % (count, itemPrice, itemName))
        count = count + 1
