from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def main():
    driver = None
    
    try:
        # ---------------------------
        # Browser Setup
        # ---------------------------
        edge_options = Options()
        edge_options.add_argument("--start-maximized")
        
        # Selenium Manager auto handles driver
        driver = webdriver.Edge(options=edge_options)
        
        wait = WebDriverWait(driver, 10)
        
        # ---------------------------
        # Open Google Homepage
        # ---------------------------
        driver.get("https://www.google.com")
        
        # Wait for search box
        search_box = wait.until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        
        print("Page Title:", driver.title)
        
        # ---------------------------
        # Validate Search Box
        # ---------------------------
        print("Search Box Displayed:", search_box.is_displayed())
        print("Search Box Enabled:", search_box.is_enabled())
        
        # Activate hidden buttons
        search_box.click()
        
        # ---------------------------
        # Validate Buttons
        # ---------------------------
        search_button = wait.until(
            EC.visibility_of_element_located((By.NAME, "btnK"))
        )
        
        lucky_button = wait.until(
            EC.visibility_of_element_located((By.NAME, "btnI"))
        )
        
        print("Google Search Button Displayed:", search_button.is_displayed())
        print("I'm Feeling Lucky Button Displayed:", lucky_button.is_displayed())
        
        # ---------------------------
        # Validate Header Links
        # ---------------------------
        gmail_link = driver.find_element(By.LINK_TEXT, "Gmail")
        images_link = driver.find_element(By.LINK_TEXT, "Images")
        
        print("Gmail Link Displayed:", gmail_link.is_displayed())
        print("Images Link Displayed:", images_link.is_displayed())
        
        # ---------------------------
        # Count Elements
        # ---------------------------
        all_links = driver.find_elements(By.TAG_NAME, "a")
        all_inputs = driver.find_elements(By.TAG_NAME, "input")
        
        print("Total Links on Page:", len(all_links))
        print("Total Input Fields:", len(all_inputs))
        
        # ---------------------------
        # Perform Search
        # ---------------------------
        search_box.send_keys("Selenium Automation")
        search_button.click()
        
        wait.until(EC.title_contains("Selenium"))
        
        print("After Search Title:", driver.title)
        print("Current URL:", driver.current_url)

    except TimeoutException:
        print("Error: Element not found within given time.")
    
    except NoSuchElementException:
        print("Error: Unable to locate element.")
    
    except Exception as e:
        print("Unexpected Error:", e)
    
    finally:
        if driver:
            driver.quit()
            print("Browser closed successfully.")

if __name__ == "__main__":
    main()
