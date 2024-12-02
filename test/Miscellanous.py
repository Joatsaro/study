from selenium import webdriver
from selenium.webdriver.chrome.service import Service


#chrome driver
from selenium.webdriver.chrome.service import Service

#Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

service_obj = Service("/Users/asaquelares/Downloads/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")

driver.get_screenshot_as_file("screen.png")
