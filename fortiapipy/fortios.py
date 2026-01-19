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
    def host(self) -> str:
        """Get the base URL of the FortiOS device API."""
        return self._host
    
    @property
    def log_level(self) -> LogLevel:
        """Get the logging level for the client."""
        return self._logging_level
    # === End Public Property methods ===

    def __init__(self, host: str, api_token: str, log_level: LogLevel = LogLevel.WARNING,
                 verify_ssl: bool = True, port: int = 443):
        """
        Initialize the FortiOSClient.
        
        Args:
            host (str): Hostname or IP Address to reach the device. Do not include protocol!
            api_token (str): API key for authentication.
            log_level (LogLevel): Logging level for the client. Defaults to WARNING.
            verify_ssl (bool): Confirm SSL certificate. Defaults to True.
        """

        self._host = host
        self._api_token = api_token
        self._logging_level = log_level
        self._verify_ssl = verify_ssl

        super().__init__(host=host, type=FortiAPIDeviceType.FORTIOS, api_token=api_token, 
                         log_level=log_level, verify_ssl=self._verify_ssl, port=port)

