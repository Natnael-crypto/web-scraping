from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://www.upwork.com/nx/search/jobs/?nbs=1&q=web+scraping')
driver.save_screenshot('screenshot.png')
driver.quit()


