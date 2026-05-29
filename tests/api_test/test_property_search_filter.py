import pytest

from utils.logger import Logger
from api.property_search_api import PropertySearchAPI
from constants import PROPERTY_SEARCH_API_DATA_PATH
from config.config_manager import ConfigManager
from utils.json_reader import JSONReader

json_data = JSONReader.read_json_data_from_file(PROPERTY_SEARCH_API_DATA_PATH)

class TestPropertySearch:

    def setup_method(self, method):
        print("Setup method for TestPropertySearch API tests")
        self.logger = Logger.get_logger(__name__)
        self.property_search_api = PropertySearchAPI()
        print("ConfigManager._config in setup_method:", ConfigManager._config)

    @pytest.mark.parametrize("test_data", json_data)
    def test_get_properties_with_search_term(self, test_data):
        self.logger.info("Testing: Search properties")
        payload = test_data.get("payload")
        response = self.property_search_api.search_properties(payload)
        self.logger.info(f"Response: {response}")
        assert response is not None, "Response should not be None"
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        assert "properties" in response, "Response should contain 'properties' key"

    