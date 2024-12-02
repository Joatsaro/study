from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pageObject.ProductPage import ProductPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SearchPageElements:
    SEARCHED_VALUE = "//*[@class='a-breadcrumb__label']/strong[contains(text(), '{}')]"
    ITEM_DESCRIPTION_TEXT = "//article/h3[contains(text(), '{}')]"
    FIRST_ITEM_DESCRIPTION_TEXT = "(//article/h3[contains(text(), '{}')])[1]"
    FILTER_NAME = "//*[@class='col a-text__filter']/label[@title='{}']"
    SIZE_FILTER = ("//label[contains(text(),'{}')]/../div[@class='m-checkbox "
                   "mdc-checkbox mdc-checkbox--upgraded mdc-ripple-upgraded mdc-ripple-upgraded--unbounded']")
    PRICE_FILTER = ("//label[contains(text(), '{}')]/../div[@class='m-radio  mdc-radio "
                    "mdc-ripple-upgraded mdc-ripple-upgraded--unbounded']")
    BRAND_FILTER = ("//input[@id='brand-{}']/../../div[@class='m-checkbox mdc-checkbox mdc-checkbox--upgraded "
                    "mdc-ripple-upgraded mdc-ripple-upgraded--unbounded']")
    FILTER_APPLIED = ("//div[@class='m-plp__filterApplied mt-4']//.."
                      "//div[@class='mdc-chip a-plp__filterSelection']//div[contains(text(), '{}')]")
    EXPAND_SIZE_FILTERS = "//a[contains(text(), 'Ver más') and @id='Tamao']"
    NAMES_OF_PRODUCTS = "//h3[@class='card-title a-card-description']"
    PRICES_OF_PRODUCTS = "//div/p[@class='a-card-discount']"
    SEARCH_BY_BRAND_TEXTBOX = "//*[@id='searchBrand']"


class SearchPage:
    # constructor to receive driver from Test Case
    def __init__(self, driver):
        self.driver = driver

    def was_item_searched(self, item):
        """
        Verify if item was correctly searched
        :param item: str
        :return: bool
        """
        try:
            self.driver.find_element(By.XPATH, SearchPageElements.SEARCHED_VALUE.format(item))
        except NoSuchElementException:
            return False
        return True

    def is_item_present_on_catalog(self, description):
        """
        Return true if at least an item which name matches the description is present on the catalog
        :param description: str
        :return: bool
        """
        try:
            (WebDriverWait(self.driver, 10).
             until(EC.presence_of_element_located((By.XPATH,
                                                   SearchPageElements.ITEM_DESCRIPTION_TEXT.format(description)))))
        except NoSuchElementException:
            return False
        return True

    def click_on_first_catalog_item(self, description):
        """
        Click the first match of a description on the catalog
        :param description: str
        :return: ProductPage.ProductPage(self.driver)
        """
        self.driver.find_element(By.XPATH, (SearchPageElements.FIRST_ITEM_DESCRIPTION_TEXT.format(description))).click()
        return ProductPage(self.driver)

    def is_filter_present(self, name):
        """
        Verify if a filter is present
        :param name: str
        :return: bool
        """
        try:
            (WebDriverWait(self.driver, 10).
             until(EC.presence_of_element_located((By.XPATH,
                                                   SearchPageElements.FILTER_NAME.format(name)))))
        except NoSuchElementException:
            return False
        return True

    def click_and_wait_on_size_filter_desired(self, size):
        """
        Select desired size filter
        :param size: str
        """
        self.driver.find_element(By.XPATH, SearchPageElements.EXPAND_SIZE_FILTERS).click()
        (WebDriverWait(self.driver, 10).
         until(EC.presence_of_element_located((By.XPATH,
                                               SearchPageElements.SIZE_FILTER.format(size)))))
        self.driver.find_element(By.XPATH, SearchPageElements.SIZE_FILTER.format(size)).click()
        (WebDriverWait(self.driver, 10).
         until(EC.presence_of_element_located((By.XPATH,
                                               SearchPageElements.FILTER_APPLIED.format(size)))))
        time.sleep(5)

    def click_and_wait_on_price_filter_desired(self, price):
        """
        Click on price filter
        :param price: str
        """
        (WebDriverWait(self.driver, 10).
         until(EC.presence_of_element_located((By.XPATH,
                                               SearchPageElements.PRICE_FILTER.format(price)))))
        self.driver.find_element(By.XPATH, SearchPageElements.PRICE_FILTER.format(price)).click()
        (WebDriverWait(self.driver, 10).
         until(EC.presence_of_element_located((By.XPATH,
                                               SearchPageElements.FILTER_APPLIED.format(price)))))
        WebDriverWait(self.driver, 5)
        time.sleep(5)

    def click_and_wait_on_brand_filter_desired(self, brand):
        """
        Click on brand filter desired
        :param brand: str
        """
        (WebDriverWait(self.driver, 10).
         until(EC.presence_of_element_located(((By.XPATH,
                                                SearchPageElements.BRAND_FILTER.format(brand))))))
        self.driver.find_element(By.XPATH, SearchPageElements.BRAND_FILTER.format(brand)).click()
        (WebDriverWait(self.driver, 10).
         until(EC.presence_of_element_located((By.XPATH,
                                               SearchPageElements.FILTER_APPLIED.format(brand)))))
        time.sleep(5)

    def return_names_of_catalog_products(self):
        """
        Return list of names of catalog products
        :return: list of str
        """
        names = []
        elements = self.driver.find_elements(By.XPATH, SearchPageElements.NAMES_OF_PRODUCTS)
        for name in elements:
            names.append(name.text)
        return names

    def return_prices_of_catalog_products(self):
        """
        Return prices of products
        :return: list of str
        """
        prices = []
        elements = self.driver.find_elements(By.XPATH, SearchPageElements.PRICES_OF_PRODUCTS)
        for price in elements:
            prices.append(price.text)
        return prices

    def fill_search_by_brand(self, brand):
        """
        Fill Search by brand textbox
        :param brand: str
        """
        (WebDriverWait(self.driver, 10).
         until(EC.presence_of_element_located(((By.XPATH,
                                                SearchPageElements.SEARCH_BY_BRAND_TEXTBOX.format(brand))))))
        self.driver.find_element(By.XPATH, SearchPageElements.SEARCH_BY_BRAND_TEXTBOX).send_keys(brand)
