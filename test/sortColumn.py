from selenium import webdriver
from selenium.webdriver.common.by import By

#chrome driver
from selenium.webdriver.chrome.service import Service
#Chrome
service_obj = Service("/Users/asaquelares/Downloads/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# collect all veggie names -> BrowserSortedVeggieList (A, B, C)
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
browserSortedVeggies = []
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

originalBrowserSortedList = browserSortedVeggies.copy()
# sort this veggie list -> newSortedList (A, B, C)
browserSortedVeggies.sort()

# BrowserSortedVeggieList == newSortedList
assert browserSortedVeggies == originalBrowserSortedList
