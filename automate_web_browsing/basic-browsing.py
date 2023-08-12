# https://www.selenium.dev/documentation/webdriver/elements/interactions/

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

# Clear field to empty it from any previous data
driver.find_element(By.NAME, "email_input").clear()
driver.find_element(By.NAME, "number_input").clear()

# Enter Text
driver.find_element(By.NAME, "email_input").send_keys("test@localhost.dev")
driver.find_element(By.NAME, "number_input").send_keys(10)
