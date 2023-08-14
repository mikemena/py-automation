from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

url = "https://www.amazon.com/s?k=kindle+paperwhite+e-reader"
driver = webdriver.Chrome()
driver.get(url)

wait = WebDriverWait(driver, 10)

searchFieldXpath = driver.find_element(By.ID, "twotabsearchtextbox")
searchButtonXpath = driver.find_element(By.ID, "nav-search-submit-button")

homeUrl = "https://www.amazon.com/"
homeTitle = "Amazon.com: Online Shopping for Electronics, Apparel, Computers,..."


# this is an explicit wait

searchField = wait.until(EC.element_to_be_clickable(searchFieldXpath))
searchField.click()
searchButton = wait.until(EC.element_to_be_clickable(searchButtonXpath))
searchButton.click()

# close browser
driver.quit()
