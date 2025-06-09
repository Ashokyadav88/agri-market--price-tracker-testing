from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://example-agri-price-tracker.com")

driver.find_element(By.NAME, "crop_name").send_keys("Wheat")
driver.find_element(By.ID, "search_button").click()

time.sleep(2)
assert "Wheat" in driver.page_source

driver.quit()
