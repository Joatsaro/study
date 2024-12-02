from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import openpyxl


def update_excel_data(filePath, searchTerm, colName, new_value):
    book = openpyxl.load_workbook(filePath)
    sheet = book.active
    Dict = {}
    for i in range(1, sheet.max_column+1):
        if sheet.cell(row=1, column=i).value == colName:
            Dict["col"] = i
    for i in range(1, sheet.max_row+1):
        for j in range(1, sheet.max_column+1):
            if sheet.cell(row=i, column=j).value == searchTerm:
                Dict["row"] = i
    sheet.cell(row=Dict["row"], column=Dict["col"]).value = new_value
    book.save(file_path)


service_obj = Service("/Users/asaquelares/Downloads/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service_obj)
file_path = "/Users/asaquelares/Downloads/download.xlsx"
fruit_name = "Apple"
newValue = "999"
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")

#download
driver.find_element(By.ID, "downloadButton").click()

#edit excel
update_excel_data(file_path, "Apple", "price", "999")

#upload
file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")

file_input.send_keys(file_path)
toast_locator = (By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)")
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(toast_locator))
print(driver.find_element(*toast_locator).text)
priceColumn = driver.find_element(By.XPATH, "//div[text()='Price']").get_attribute("data-column-id")
actual_price = driver.find_element(By.XPATH, "//div[text()='"+fruit_name+"']/parent::div/parent::div/div[@id='cell-"+priceColumn+"-undefined']").text
print(actual_price)
assert actual_price == newValue
