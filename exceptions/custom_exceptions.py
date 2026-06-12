class CustomExceptions(Exception):
    """Base class for custom exceptions in the test framework."""
    pass

class APIException(CustomExceptions):
    """Raised when an HTTP request fails or the response is unexpected."""
    pass

class JSONException(CustomExceptions):
    """Raised when there is an error parsing JSON data."""
    pass
