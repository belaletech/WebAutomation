from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the Chrome WebDriver with options
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()), options=options)

# Open the login page
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(3)

# Search for LambdaTest Login
driver.find_element("name", "q").send_keys("LambdaTest Login")
driver.find_element("name", "q").send_keys(Keys.ENTER)

# Click on the login link
driver.find_element("partial link text", "Log in - LambdaTest").click()

# Enter email and password
driver.find_element("id", "email").send_keys("ritamg@lambdatest.com")
driver.find_element("id", "password").send_keys("Shiva@12")

# Click login button
driver.find_element("id", "login-button").click()

time.sleep(10)
driver.quit()
