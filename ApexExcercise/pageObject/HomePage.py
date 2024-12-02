from selenium.webdriver.common.by import By
from pageObject.SearchPage import SearchPage
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePageElements:
    SEARCH_BAR = (By.CSS_SELECTOR, "[id='mainSearchbar']")
    SEARCH_ICON = (By.XPATH, "//*[@class='input-group-text']//*[@class='icon-zoom']")
    CATEGORIES_BUTTON = (By.XPATH, "//span[@class='a-header__strongLink nav-desktop-menu-action pr-3 pb-3']")
    DESIRED_SUB_MENU = "//li/a[contains(text(), '{}')]"
    DESIRED_SUB_CATEGORY = "//ul[@class='m-desktop-subcategory-list']//a[contains(text(), '{}')]"


class HomePage:
    # constructor to receive driver from Test Case
    def __init__(self, driver):
        self.driver = driver

    def fill_search_bar(self, item):
        """
        Returns search bar element
        :param item: str
        """
        self.driver.find_element(*HomePageElements.SEARCH_BAR).send_keys(item)

    def click_search_icon(self):
        """
        Pre-requisite: write something on search bar
        Clicks search icon
        :return: SearchPage.SearchPage(self.driver)
        """
        self.driver.find_element(*HomePageElements.SEARCH_ICON).click()
        return SearchPage(self.driver)

    def click_categories_section(self):
        """
        Open categories menu
        :return:
        """
        self.driver.find_element(*HomePageElements.CATEGORIES_BUTTON).click()

    def hover_onto_sub_menu(self, sub_menu):
        """
        Hover mouse onto desired sub_menu
        :param sub_menu: str
        """
        (WebDriverWait(self.driver, 10).
         until(EC.presence_of_element_located((By.XPATH,
                                               HomePageElements.DESIRED_SUB_MENU.format(sub_menu)))))
        actions = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH, HomePageElements.DESIRED_SUB_MENU.format(sub_menu))
        actions.move_to_element(element).perform()

    def hover_and_click_onto_desired_sub_category(self, sub_category):
        """
        Pre-requisite, hover into previous sub menu
        click  onto desired sub_category
        :param sub_category: str
        :return: SearchPage(self.driver)
        """
        (WebDriverWait(self.driver, 10).
         until(EC.presence_of_element_located((By.XPATH,
                                               HomePageElements.DESIRED_SUB_CATEGORY.format(sub_category)))))
        actions = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH, HomePageElements.DESIRED_SUB_CATEGORY.format(sub_category))
        actions.move_to_element(element).perform()
        self.driver.find_element(By.XPATH, HomePageElements.DESIRED_SUB_CATEGORY.format(sub_category)).click()
        return SearchPage(self.driver)
