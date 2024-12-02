from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPageElements:
    PRODUCT_TITLE = (By.CSS_SELECTOR, "[class='a-product__information--title']")
    PRICE_DISCOUNT = (By.CSS_SELECTOR, "[class='a-product__paragraphDiscountPrice m-0 d-inline']")
    PRICE_NORMAL = (By.CSS_SELECTOR, "[class='a-product__paragraphRegularPrice m-0 d-inline']")


class ProductPage:
    # constructor to receive driver from Test Case
    def __init__(self, driver):
        self.driver = driver

    def return_product_title(self):
        """
        Return text in product title
        :return: str
        """
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(ProductPageElements.PRODUCT_TITLE))
        return self.driver.find_element(*ProductPageElements.PRODUCT_TITLE).text

    def return_product_price(self):
        """
        Return text in product price
        :return: str
        """
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(ProductPageElements.PRICE_NORMAL))
        if self.driver.find_element(*ProductPageElements.PRICE_DISCOUNT):
            return self.driver.find_element(*ProductPageElements.PRICE_DISCOUNT).text
        else:
            return self.driver.find_element(*ProductPageElements.PRICE_NORMAL).text

