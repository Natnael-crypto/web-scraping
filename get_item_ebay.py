from selenium import webdriver
from selenium.webdriver.common.by import By
import time



Url="https://www.ebay.com/sch/i.html?_nkw=iphone+13&_pgn="

for i in range(1,3):
    driver = webdriver.Chrome()
    driver.get(Url+str(i)) 
    time.sleep(5)

    items = driver.find_elements(By.CSS_SELECTOR, 'li.s-item')

    print(len(items))
    for item in items:
        try:
            title = item.find_element(By.CSS_SELECTOR, 'div.s-item__title span').text
            price = item.find_element(By.CSS_SELECTOR, 'span.s-item__price').text
            link_tag = item.find_element(By.CSS_SELECTOR, 'a.s-item__link')
            url = link_tag.get_attribute("href") if link_tag else "URL not found"
            try:
                shipping = item.find_element(By.CSS_SELECTOR, 'span.s-item__shipping').text
            except:
                shipping = "No shipping info"
            try:
                condition = item.find_element(By.CSS_SELECTOR, 'span.SECONDARY_INFO').text
            except:
                condition = "No condition info"
            try:
                rating = item.find_element(By.CSS_SELECTOR, 'div.x-star-rating').text
                reviews = item.find_element(By.CSS_SELECTOR, 'span.s-item__reviews-count').text
            except:
                rating = "No ratings"
                reviews = "No reviews"
            try:
                seller_info = item.find_element(By.CSS_SELECTOR, 'span.s-item__seller-info-text').text
            except:
                seller_info = "No seller info"
            try:
                features = item.find_elements(By.CSS_SELECTOR, 'div.s-item__subtitle')
                feature_list = [feature.text for feature in features if feature.text.strip() != '']
            except:
                feature_list = []
            try:
                img_tag = item.find_element(By.CSS_SELECTOR, 'img.s-item__image-img')
                img_url = img_tag.get_attribute("src") if img_tag else "No image"
            except:
                img_url = "No image"

            # Print extracted details
            print(f"Title: {title}")
            print(f"Price: {price}")
            print(f"Shipping: {shipping}")
            print(f"Condition: {condition}")
            print(f"Rating: {rating}")
            print(f"Reviews: {reviews}")
            print(f"Seller: {seller_info}")
            print(f"Features: {', '.join(feature_list) if feature_list else 'No features'}")
            print(f"Product URL: {url}")
            print(f"Image URL: {img_url}")
            print("-" * 80)

        except Exception as e:
            print(f"Error extracting item: {e}")

    # Close the browser once done
    driver.quit()
