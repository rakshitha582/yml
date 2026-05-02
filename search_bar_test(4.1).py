""" This code automatically detects the google searc bar and searches something """


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get("https://www.google.com")

try:
    search_box = driver.find_element(By.NAME,"q")
    print("Search box found successfully")
    try:
        search_box.send_keys("What is selenium ?")
        search_box.submit()
        print("searched something")
    except:
        print("not searched anything")
except:
    print("Search box not found")
    
print("browser closing...")
driver.quit()

