from pages.sale_property_page.sale_property_page import SalePropertyPage
from api.property_search_api import PropertySearchAPI
from utils.logger import Logger
import pytest, constants
from utils.json_reader import JSONReader
from validators.property_search_validator import PropertySearchValidator


json_data = JSONReader.read_json_data_from_file(constants.PROPERTY_SEARCH_FILTER_DATA_PATH)

@pytest.mark.usefixtures("setup_teardown")
class TestSearchFilterProperty:

    def setup_method(self, method):
        self.log = Logger.get_logger(__name__)
        self.log.info("Test setup started.")
        self.sale_property_page = SalePropertyPage(self.driver)
        self.property_search_api = PropertySearchAPI()
        self.log.info("Test setup completed.")

    @pytest.mark.parametrize("test_data", json_data)
    def test_search_filter_property(self, test_data):
        self.log.info(f"Test case ID: {test_data['test_case_id']} - {test_data['description']}")
        if test_data.get("search") != {}:
            self.sale_property_page.search_location(test_data["search"]["location"])
        if test_data.get("quick_filters"):
             filters = test_data["quick_filters"]
             if filters.get("bedrooms"):
                 self.sale_property_page.apply_bedroom_filter(filters["bedrooms"])
             if filters.get("price"):
                 self.sale_property_page.apply_price_filter(filters["price"]["min"], filters["price"]["max"])
             if filters.get("property_type"):
                 self.sale_property_page.apply_property_type_filter(filters["property_type"])
        if test_data.get("more_filters"):
            for filter_name, filter_value in test_data["more_filters"].items():
                if filter_value:
                    self.sale_property_page.apply_multiple_filters({filter_name: filter_value})
        response_json = self.property_search_api.search_properties(test_data["api_search_query_params"])
        PropertySearchValidator.validate_search_results(response_json, test_data)
