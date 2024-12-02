from pageObject.HomePage import HomePage
from pageObject.SearchPage import SearchPage
from utilities.BaseClass import BaseClass


class TestThree(BaseClass):
    # receive setup once from fixture REVIEW
    def test_01_open_categories_section(self):
        home_page = HomePage(self.driver)
        home_page.click_categories_section()

    def test_02_hover_onto_sub_menu_and_then_click_in_sub_category(self):
        home_page = HomePage(self.driver)
        home_page.hover_onto_sub_menu("Belleza")
        home_page.hover_and_click_onto_desired_sub_category("Perfumes Hombre")

    def test_03_filter_the_results(self):
        search_page = SearchPage(self.driver)
        search_page.fill_search_by_brand("DIOR")
        search_page.click_and_wait_on_brand_filter_desired("DIOR")