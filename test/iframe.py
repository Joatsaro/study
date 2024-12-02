from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


#chrome driver
from selenium.webdriver.chrome.service import Service
#Chrome
service_obj = Service("/Users/asaquelares/Downloads/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()

driver.switch_to.frame("mce_0_ifr")
driver.get("https://the-internet.herokuapp.com/iframe")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am able to automate frames")

driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)