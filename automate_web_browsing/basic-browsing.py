# https://www.techlistic.com/2020/07/automation-testing-demo-websites.html
# https://www.techlistic.com/p/selenium-practice-form.html


from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
name_field = driver.find_element(
    "xpath", "//firstname[text()=’About Software Test Academy’]"
)
name_field.send_keys("test")
print(name_field)
