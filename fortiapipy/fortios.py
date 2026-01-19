"""
# FortiOS API client library.

This library extends the core FortiAPIClient class to provide access to
FortiOS-specific API resources.
"""

# Python core imports

# Third-party imports

# Local imports
from fortiapipy import core
from fortiapipy.enums import FortiAPIDeviceType
from fortiapipy.logger import LogLevel

__author__ = core.__author__
__copyright__ = core.__copyright__
__version__ = core.__version__
__license__ = core.__license__

class FortiOSClient(core.FortiAPIClient):
    """Client class for FortiOS API interactions."""

    # === Start Public Property methods ===

    @property
    def api_type(self) -> FortiAPIDeviceType:
        """Get the API device type."""
        return self._api_type
    
    @property
    def base_url(self) -> str:
        """Get the base URL of the FortiOS device API."""
        return self._base_url
    
    @property
    def log_level(self) -> LogLevel:
        """Get the logging level for the client."""
        return self._logging_level
    # === End Public Property methods ===

    def __init__(self, base_url: str, api_key: str, log_level: LogLevel = LogLevel.WARNING):
        """
        Initialize the FortiOSClient.
        
        Args:
            base_url (str): Base URL of the FortiOS device API.
            api_key (str): API key for authentication.
            log_level (LogLevel): Logging level for the client. Defaults to WARNING.
        """

        self._api_type = FortiAPIDeviceType.FORTIOS
        self._base_url = base_url
        self._api_key = api_key
        self._logging_level = log_level

        super().__init__(FortiAPIDeviceType.FORTIOS, base_url, api_key, log_level=log_level)

