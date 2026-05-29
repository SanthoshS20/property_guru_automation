import requests
from core.api_client import APIClient
from config.config_manager import ConfigManager


class AuthManager:

    @staticmethod
    def authenticate(username, password):
        api_client = APIClient()
        api_client.make_api_request(
            method="POST",
            url=ConfigManager.get("auth_url"),
            json={
                "username": username,
                "password": password
            }
        )
        return api_client
