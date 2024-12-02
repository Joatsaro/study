from pageObject.HomePage import HomePage
from pageObject.SearchPage import SearchPage
from utilities.BaseClass import BaseClass


class TestTwo(BaseClass):
    # receive setup once from fixture REVIEW
    def test_01_search_smart_tv(self):
        home_page = HomePage(self.driver)
        home_page.fill_search_bar("smart tv")
        search_page = home_page.click_search_icon()
        search_page.was_item_searched("smart tv")

    def test_02_verify_size_and_prize_filters_available(self):
        search_page = SearchPage(self.driver)
        assert search_page.is_filter_present("Tamaño")
        assert search_page.is_filter_present("Precios")

    def test_03_filter_by_size_and_price_and_brand(self):
        search_page = SearchPage(self.driver)
        search_page.click_and_wait_on_size_filter_desired("55 pulgadas")
        search_page.click_and_wait_on_price_filter_desired("Mas de $10000.0")
        search_page.click_and_wait_on_brand_filter_desired("SONY")

    def test_04_verify_brand_and_size_and_price_on_catalog_are_correct(self):
        search_page = SearchPage(self.driver)
        names = search_page.return_names_of_catalog_products()
        prices = search_page.return_prices_of_catalog_products()
        for name in names:
            assert "55" in name
        for price in prices:
            price = price[1:-2]
            price = price.replace(",", "")
            assert int(price) > 10000
