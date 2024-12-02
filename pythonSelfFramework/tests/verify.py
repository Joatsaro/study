import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()
windows = driver.window_handles

driver.switch_to.window(windows[1])
print(driver.title)

email = driver.find_element(By.XPATH, "//a[contains(text(),'.com')]").text

print(email)

driver.switch_to.window(windows[0])
driver.find_element(By.CSS_SELECTOR, "#username").send_keys(email)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("123456789")
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
time.sleep(2)

print(driver.find_element(By.XPATH, "//form[@id='login-form']/div[1]").text)
