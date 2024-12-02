from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#chrome driver
service_obj = Service("/Users/asaquelares/Downloads/chromedriver_mac_arm64/chromedriver");
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()
