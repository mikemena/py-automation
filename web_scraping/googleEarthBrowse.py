from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.amazon.com/s?k=kindle+paperwhite+e-reader"
driver = webdriver.Chrome()
driver.get(url)

searchFieldXpath = driver.find_element(By.ID, "twotabsearchtextbox")
searchButtonXpath = driver.find_element(
    By.CLASS_NAME, "nav-search-submit-text nav-sprite"
)


homeUrl = "https://www.amazon.com/"
homeTitle = "Amazon.com: Online Shopping for Electronics, Apparel, Computers,..."


# this is an explicit wait
if (!wait.until(new PageLoaded(homeTitle, homeUrl)))
throw new RuntimeException("home page is not displayed");

searchField = wait.until(elementToBeClickable(searchFieldXpath));
searchField.click(); 
searchField.sendKeys(keyword);
searchButton = wait.until(elementToBeClickable(searchButtonXpath));
searchButton.click();