from pages.base_page.base_page import BasePage
from pages.sale_property_page.sale_property_page_locators import SalePropertyPageLocators


class SalePropertyPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def search_location(self, location):
        self.enter_text(SalePropertyPageLocators.SEARCH_INPUT_FIELD, location)
        self.click_element(SalePropertyPageLocators.search_result_option(location))

    def apply_bedroom_filter(self, bedroom_count):
        self.click_element(SalePropertyPageLocators.BEDROOM_FILTER_DROPDOWN)
        self.click_element(SalePropertyPageLocators.bedroom_option(bedroom_count))
        self.click_element(SalePropertyPageLocators.APPLY_BUTTON)

    def apply_price_filter(self, min_price, max_price):
        self.click_element(SalePropertyPageLocators.PRICE_FILTER_DROPDOWN)
        self.click_element(SalePropertyPageLocators.select_min_price_option(min_price))
        self.click_element(SalePropertyPageLocators.select_max_price_option(max_price))
        self.click_element(SalePropertyPageLocators.APPLY_BUTTON)

    def apply_property_type_filter(self, property_type):
        self.click_element(SalePropertyPageLocators.PROPERTY_TYPE_DROPDOWN)
        self.click_element(SalePropertyPageLocators.select_property_type_option(property_type))
        self.click_element(SalePropertyPageLocators.APPLY_BUTTON)

    def click_more_filters(self):
        self.click_element(SalePropertyPageLocators.FILTERS_DROPDOWN)

    def apply_multiple_filters(self, filters):
        self.click_more_filters()
        if filters.get("bathrooms"):
            self.click_element(SalePropertyPageLocators.select_more_filters_option("bathrooms"))
            self.click_element(SalePropertyPageLocators.bathroom_option(filters["bathrooms"]))
        if filters.get("verified_listing"):
            self.click_element(SalePropertyPageLocators.VERIFIED_LISTING_TOGGLE)
        self.click_element(SalePropertyPageLocators.APPLY_BUTTON)

    def clear_all_filters(self):
        self.click_element(SalePropertyPageLocators.CLEAR_BUTTON)