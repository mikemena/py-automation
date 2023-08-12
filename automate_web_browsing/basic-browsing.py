# https://www.selenium.dev/documentation/webdriver/elements/interactions/

from selenium import webdriver, 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.


driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

# Clear field to empty it from any previous data
driver.find_element(By.NAME, "email_input").clear()
driver.find_element(By.NAME, "number_input").clear()
driver.find_element(By.NAME, "range_input").clear()
driver.find_element(By.NAME, "password_input").clear()
driver.find_element(By.NAME, "search_input").clear()
driver.find_element(By.NAME, "checkbox_input").clear()
driver.find_element(By.NAME, "radio_input").clear()

# Enter Text
driver.find_element(By.NAME, "email_input").send_keys("test@localhost.dev")
driver.find_element(By.NAME, "number_input").send_keys(10)
driver.find_element(By.NAME, "password_input").send_keys("12ggT45abc#")
driver.find_element(By.NAME, "search_input").send_keys("golden retrievers")
driver.find_element(By.NAME, "checkbox_input").send_keys("false")
driver.find_element(By.NAME, "search_input").send_keys("golden retrievers")


checkbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "w-enabled-24"))
)
if not checkbox.is_selected():
    checkbox.click()
