from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.by import By

# chrome driver
from selenium.webdriver.chrome.service import Service

# Chrome
service_obj = Service("/Users/asaquelares/Downloads/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/loginpagePractise")
driver.find_element(By.XPATH, "//body/a").click()

windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])
emailRetrieved = driver.find_element(By.XPATH, "//strong/a").text
driver.close()

driver.switch_to.window(windowsOpened[0])
driver.find_element(By.XPATH, "//input[@name='username']").send_keys(emailRetrieved)
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("wrongPassword")
driver.find_element(By.XPATH, "//input[@id='terms']").click()
driver.find_element(By.XPATH, "//input[@id='signInBtn']").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)
