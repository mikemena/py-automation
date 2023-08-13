# https://www.selenium.dev/documentation/webdriver/elements/interactions/

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

# Clear field to empty it from any previous data
driver.find_element(By.NAME, "email_input").clear()
driver.find_element(By.NAME, "number_input").clear()
driver.find_element(By.NAME, "range_input").clear()
driver.find_element(By.NAME, "password_input").clear()
driver.find_element(By.NAME, "search_input").clear()

# handling text fields
driver.find_element(By.NAME, "email_input").send_keys("test@localhost.dev")
driver.find_element(By.NAME, "number_input").send_keys(10)
driver.find_element(By.NAME, "password_input").send_keys("12ggT45abc#")
driver.find_element(By.NAME, "search_input").send_keys("golden retrievers")
driver.find_element(By.NAME, "checkbox_input").click()

# Get the radio element with value='radio2'
radio_button = driver.find_element(
    By.XPATH, "//input[@type='radio' and @value='radio2']"
)
# Click on the radio button element
radio_button.click()

# set date input
element = driver.find_element(By.NAME, "date_input")
driver.find_element(By.NAME, "date_input").send_keys("08-12-2023")
driver.execute_script("arguments[0].setAttribute('value', '08/12/2023')", element)

# Take a screenshot
driver.save_screenshot("screenshot-1.png")

driver.find_element(By.NAME, "reset_input").click()
# Close the driver
driver.quit()
