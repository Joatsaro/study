from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    location = (By.ID, "country")
    india = (By.LINK_TEXT, "India")
    agree = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase = (By.CSS_SELECTOR, "[type='submit']")
    end_text = (By.CLASS_NAME, "alert-success")

    def deliveryLocation(self):
        return self.driver.find_element(*ConfirmPage.location)

    def indiaElement(self):
        return self.driver.find_element(*ConfirmPage.india)

    def agreeTerms(self):
        return self.driver.find_element(*ConfirmPage.agree)

    def purchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def endText(self):
        return self.driver.find_element(*ConfirmPage.end_text)