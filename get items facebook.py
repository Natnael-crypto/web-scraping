# card class name= x1uepa24

# price tage dir="auto"

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the Selenium WebDriver
driver = webdriver.Chrome()  # Specify your chromedriver path
driver.get("https://web.facebook.com/marketplace/search?query=iphone 14")  # Replace with the target page URL

driver.save_screenshot('facebook.png')

# Wait for the page to load completely
time.sleep(5)

# Find all div elements with class "x1uepa24"
items = driver.find_elements(By.CSS_SELECTOR, 'div.x1uepa24')

# Loop through all the extracted items and retrieve information
for item in items:
    try:
        # Extract the item name
        name = item.find_element(By.CSS_SELECTOR, 'span[style*="-webkit-line-clamp"]').text

        # Extract the price
        price = item.find_element(By.CSS_SELECTOR, 'span[dir="auto"]').text

        # Extract the location
        location = item.find_element(By.CSS_SELECTOR, 'span.x1lliihq.x6ikm8r.x10wlt62.x1n2onr6.xlyipyv.xuxw1ft.x1j85h84').text

        # Extract the URL
        link_tag = item.find_element(By.CSS_SELECTOR, 'a[role="link"]')
        url = "https://www.facebook.com" + link_tag.get_attribute("href") if link_tag else "URL not found"

        # Print extracted details
        print(f"Name: {name}")
        print(f"Price: {price}")
        print(f"Location: {location}")
        print(f"URL: {url}")
        print("-" * 50)

    except Exception as e:
        print(f"Error extracting item: {e}")

# Close the browser once done
driver.quit()
