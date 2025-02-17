from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()  
driver.get("https://www.upwork.com/nx/search/jobs/?nbs=1&q=web+scraping")

time.sleep(5)


job_elements = driver.find_elements(By.CSS_SELECTOR, 'article[data-test="JobTile"]')

for job in job_elements:

    title = job.find_element(By.CSS_SELECTOR, 'h2.job-tile-title a').text

    posted_time = job.find_element(By.CSS_SELECTOR, 'small[data-test="job-pubilshed-date"]').text
    

    job_link = job.find_element(By.CSS_SELECTOR, 'h2.job-tile-title a').get_attribute('href')
    
    
    print(f"Title: {title}")
    print(f"Posted: {posted_time}")
    print(f"Link: {job_link}")
    print("-" * 50)

# Close the browser once done
driver.quit()
