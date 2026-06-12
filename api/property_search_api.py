from config.config_manager import ConfigManager
from core.api_client import APIClient

class PropertySearchAPI:

    SEARCH_PATH = "/property-for-sale"

    def __init__(self, api_client=None):
        self.api_client = api_client or APIClient()
        self.base_url = ConfigManager.get("base_url")

    def search_properties(self, search_query_params):
        url = f"{self.base_url}{self.SEARCH_PATH}"
        response = self.api_client.make_api_request(url, params=search_query_params)
        return response.json()
