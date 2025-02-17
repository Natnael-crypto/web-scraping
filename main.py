from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = False  # Run in non-headless mode
driver = webdriver.Chrome(options=options)

driver.get("https://example.com")
print(driver.page_source)
driver.quit()