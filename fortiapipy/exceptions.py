"""Custom exceptions"""

__author__ = "The Network Entropologist"
__copyright__ = "(c) 2026 The Network Entropologist"
__version__ = "0.1.0"
__license__ = "Apache-2.0"

class FortiAPIError(Exception):
    """An exception thrown when an error occurs interacting with the API."""

    def __init__(self, status_code: int, message:str):
        """
        Create a new FortiAPIError.

        args:
            status_code (int): The HTTP status code returned by the API.
            message (str): A message describing the error.
        """
        super().__init__(f"FortiAPIError: Status Code {status_code} - {message}")
        self.status_code = status_code
        self.message = message
