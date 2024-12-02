from pageObject.HomePage import HomePage
from pageObject.SearchPage import SearchPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    # receive setup once from fixture REVIEW
    def test_01_search_playstation(self):
        home_page = HomePage(self.driver)
        home_page.fill_search_bar("playstation")
        search_page = home_page.click_search_icon()
        search_page.was_item_searched("playstation")

    def test_02_verify_console_and_games_present(self):
        search_page = SearchPage(self.driver)
        assert search_page.is_item_present_on_catalog("Consola")
        assert search_page.is_item_present_on_catalog("físico")

    def test_03_select_a_console_then_validate_title_and_price(self):
        search_page = SearchPage(self.driver)
        product_page = search_page.click_on_first_catalog_item("Consola")
        assert product_page.return_product_title() == "Consola PS5 de 1 TB edición bundle"
        assert product_page.return_product_price() == "$7,799\n22"
