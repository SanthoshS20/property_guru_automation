import requests
from utils.logger import Logger
from exceptions.custom_exceptions import APIException

class APIClient:
    def __init__(self):
        self.logger = Logger.get_logger(__name__)
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json"
        })

    def make_api_request(self, method, url, params=None, json=None, data=None, headers=None, files=None, timeout=30):
        try:
            response = self.session.request(method=method, url=url, params=params, json=json, data=data, headers=headers,
                                        files=files, timeout=timeout)
            response.raise_for_status()
            self.logger.info(f"Request: {method} {url}")
            self.logger.info(f"Status Code: {response.status_code}")
            return response
        except requests.HTTPError as http_err:
            raise requests.HTTPError(f"HTTP error occurred: {http_err}")
        except APIException as api_err:
            raise APIException(f"API error occurred: {api_err}")
