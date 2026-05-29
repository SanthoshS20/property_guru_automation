from selenium.webdriver.common.by import By
from pages.base_page.base_page_locators import BasePageLocators


class SalePropertyPageLocators(BasePageLocators):

    SEARCH_INPUT_FIELD = (By.XPATH, '//input[@placeholder="Search Location"]')
    BEDROOM_FILTER_DROPDOWN = (By.XPATH, '//button[@da-id="quick-filter-bedrooms-root"]')
    PRICE_FILTER_DROPDOWN = (By.XPATH, '//button[@da-id="quick-filter-price-search-root"]')
    PROPERTY_TYPE_DROPDOWN = (By.XPATH, '//button[@da-id="quick-filter-property-type-search-root"]')
    VERIFIED_LISTING_TOGGLE = (By.XPATH, '//label[@da-id="verified-listing-root"]')
    MIN_PRICE_INPUT = (By.XPATH, '//input[@placeholder="Min"]')
    MAX_PRICE_INPUT = (By.XPATH, '//input[@placeholder="Max"]')
    FILTERS_DROPDOWN = (By.XPATH, '//button[@label="Filters"]')
    APPLY_BUTTON = (By.XPATH, '//div[text()="Apply"]')
    CLEAR_BUTTON = (By.XPATH, '//div[text()="Clear"]')


    def search_result_option(self, search_term):
        return (By.XPATH, f'//div[@id="search-typeahead-menu"]//child::span[text()="{search_term}"]')
    
    def bedroom_option(self, bedroom_count):
        return (By.XPATH, f'//div[@da-id="bedroom-sub-filter-root"]//child::label[text()="{bedroom_count}"]')
    
    def bathroom_option(self, bathroom_count):
        return (By.XPATH, f'//div[@da-id="bathrooms-root"]//child::label[text()="{bathroom_count}"]')
    
    def select_min_price_option(self, min_price):
        return (By.XPATH, f'//div[text()="Minimum"]//parent::div[@class="range-input"]//child::p[text()="{min_price}"]')
    
    def select_max_price_option(self, max_price):
        return (By.XPATH, f'//div[text()="Maximum"]//parent::div[@class="range-input"]//child::p[text()="{max_price}"]')
    
    def select_property_type_option(self, property_type):
        return (By.XPATH, f'//label[text()="{property_type}"]')
    
    def select_property_checklist_option(self, option):
        return (By.XPATH, f'//div[@da-id="checkbox-list-root"]//child::label[text()="{option}"]')
    
    def select_more_filters_option(self, filter_name):
        return (By.XPATH, f'//h2[@class="accordion-header"]//parent::div[@da-id="{filter_name}-root"]')