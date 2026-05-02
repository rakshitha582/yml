from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time

# ---------- CHANGE THIS PATH ----------
EDGE_DRIVER_PATH = r"C:\Users\sangi\OneDrive\Desktop\msedgedriver.exe"
# ------------------------------------

edge_options = Options()
edge_options.add_argument("--start-maximized")

service = Service(EDGE_DRIVER_PATH)
driver = webdriver.Edge(service=service, options=edge_options)

# Open Facebook login page
driver.get("https://www.facebook.com")

print("Facebook login page opened.")
print("Please login manually in the browser...")

# Wait until user logs in
input("After login is successful, press ENTER here to continue...")

print("Facebook homepage displayed successfully!")

time.sleep(5)
driver.quit()
