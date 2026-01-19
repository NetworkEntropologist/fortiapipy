"""Custom exceptions"""

class FortiAPIError(Exception):
    """An exception thrown when an error occurs interacting with the API."""

    def __init__(self, status_code: int, message:str):
        super().__init__(f"FortiAPIError: Status Code {status_code} - {message}")
    