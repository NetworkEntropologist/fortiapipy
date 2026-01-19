"""
Fortinet API client library for Python.

This is the core module that provides the main functionality for interacting 
with Fortinet devices via their APIs.
"""

__author__ = "The Network Entropologist"
__copyright__ = "(c) 2026 The Network Entropologist"
__version__ = "0.1.0"
__license__ = "Apache-2.0"

# Python core imports

# Third-party imports
import requests

# Local imports
from fortiapipy import enums
from fortiapipy.logger import FortiAPILogger, LogLevel

# Initialise module logger
logger = FortiAPILogger(level=LogLevel.WARNING) 
"""
Setup module logging. Default level is WARNING, but can be overridden as follows:
`logger.level = logger.DEBUG`
"""

class FortiAPIClient:
    """Client class for Fortinet API interactions."""

    def __init__(self, api_type: enums.FortiAPIDeviceType, base_url: str, 
                 api_key: str, log_level: LogLevel = LogLevel.WARNING):
        """
        Initialize the FortiAPIClient.

        Args:
            api_type (enums.FortiAPIDeviceType): Type of Fortinet device.
            base_url (str): Base URL of the Fortinet device API.
            api_key (str): API key for authentication.
            log_level (LogLevel): Logging level for the client. Defaults to WARNING.
        """
        
        self._api_type = api_type
        self._base_url = base_url
        self._api_key = api_key
        logger.level = log_level.value

        logger.debug(f"Initialized FortiAPIClient for {api_type} at {base_url}")
        
class APIResource:
    """Base API resources class."""

    def __init__(self, client: FortiAPIClient, path=""):
        """
        Initialize the FortiAPIResource.
        
        Args:
            api_type (enums.FortiAPIDeviceType): Type of Fortinet device.
            base_url (str): Base URL of the Fortinet device API.
            api_key (str): API key for authentication.
        """

        self._client = client
        self._path = path

        logger.debug(f"Initialized APIResource with path: {path}")
