from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Edge()
driver.get("https://www.google.com")
print("google search box opened")
time.sleep(2)
search_box=driver.find_element(By.NAME,"q")
search_box.send_keys("Selenium")
print("search box opens selenium")
search_box.send_keys(Keys.RETURN)
time.sleep(3)
driver.quit()
