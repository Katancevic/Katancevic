from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



my_options = ChromeOptions()
my_options.add_argument("start-maximized")
driver = Chrome(options=my_options)
driver.get("https://www.dmv-control-center.com/login")

username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
         
username_field.send_keys("ivan.katancevic")
password_field.send_keys("KaTaNaC8888!")
signInButton = driver.find_element(By.TAG_NAME, "button")
signInButton.click()
signInButton = driver.find_element(By.CLASS_NAME, "username")
signInButton.click()

driver.get_screenshot_as_file('form.png')

