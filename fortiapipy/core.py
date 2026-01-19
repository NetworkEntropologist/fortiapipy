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
import posixpath
import json
from urllib import parse

# Third-party imports
import requests

# Local imports
from fortiapipy.enums import FortiAPIDeviceType
from fortiapipy.logger import FortiAPILogger, LogLevel
from fortiapipy.exceptions import FortiAPIError

# Initialise module logger
logger = FortiAPILogger(level=LogLevel.WARNING) 

_API_URI_PREFIX = {
    FortiAPIDeviceType.FORTIOS: '/api/v2',
}

class APIResource:
    """Base API resources class."""

    # === Start Public Property methods ===
    @property
    def url(self) -> str:
        """Return the full URL for the API request"""
        return self._store['base_url']
    # === End Public Property methods ===

    # === Start private methods ===
    def __init__(self, **kwargs):
        """Initialize the FortiAPIResource."""

        self._store = kwargs
        
    def __getattr__(self, item):
        """Dynamically create sub-resources as attributes."""

        # Attributes cannot start with a _ character
        if item.startswith('_'):
            raise AttributeError(f'Attribute {item} not found.')

        kwargs = self._store.copy()

        item = item.replace('_', '-') # Correct the item to turn a _ into a -
        kwargs['base_url'] = self._url_join(self._store['base_url'], item)
        
        return APIResource(**kwargs)
    
    def _url_join(self, base_url: str, *args) -> str:
        """Add path components to a base URL."""

        # Split the base URL into its individual components and append the new path components
        _protocol, _host, _path, _query, _fragment = parse.urlsplit(base_url)
        _path = _path if len(_path) else '/'
        _path = posixpath.join(_path, *[str(arg) for arg in args])

        return parse.urlunsplit([_protocol, _host, _path, _query, _fragment])

    def _do_request(self, method: str, data=None, params=None) -> requests.Response:
        """Perform an HTTP request"""

        try:
            resp = requests.request(url = self._store['base_url'], method=method, params=params,
                                    verify=self._store['verify_ssl'], 
                                    timeout=self._store['timeout'], headers=self._store['headers'],
                                    data=data)
        except ConnectionError as e:
            logger.error(f'Connection error while connecting to {self._store["base_url"]}: {e}')
            raise

        if resp.status_code != 200:
            logger.error(f'Error response from {self._store["base_url"]}: ' \
                         f'{resp.status_code} {resp.reason} - {resp.text}')
            raise FortiAPIError(resp.status_code, resp.text)
        
        logger.debug(f'Received response: {resp.status_code} {resp.reason} - {resp.text}')

        return resp.json()['results']
    # === End private methods ===

    # === Start public methods ===
    def get(self, *args, **params):
        """
        Perform a GET request to the API resource.

        Args:
            *args: Additional path components to append to the URL.
            **params: Query parameters for the GET request.

        Returns:
            Response object from the requests library.
        """

        logger.debug(f'Performing GET request to URL: {self._store["base_url"]} with params: {params}')

        return self._do_request('GET', params=params)
    
    def post(self, *args, **data):
        """
        Perform a POST request to the API resource.

        Args:
            data (dict): Data to send in the body of the POST request.

        Returns:
            Response object from the requests library.
        """

        return self._do_request('POST', data=data)
    
    def put(self, data: dict):
        """
        Perform a PUT request to the API resource.

        Args:
            data (dict): Data to send in the body of the PUT request.

        Returns:
            Response object from the requests library.
        """

        logger.debug(f'Performing PUT request to URL: {self._store["base_url"]} with data: {data}')

        return self._do_request('PUT', params=json.dumps(data))

    def delete(self, *args, **params):
        """
        Perform a DELETE request to the API resource.

        Args:
            *args: Additional path components to append to the URL.
            **params: Query parameters for the DELETE request.

        Returns:
            Response object from the requests library.
        """

        logger.debug(f'Performing DELETE request to URL: {self._store["base_url"]} with params: {params}')

        return self._do_request('DELETE', params=params)
    
    def create(self, *args, **data):
        """
        Create a new resource via a POST request.

        Args:
            data (dict): Data for the new resource.

        Returns:
            Response object from the requests library.
        """

        logger.debug(f'Creating resource at URL: {self._store["base_url"]} with data: {data}')

        return self.post(self, *args, **data)
    
    def set(self, data: dict):
        """
        Update an existing resource via a PUT request.

        Args:
            data (dict): Updated data for the resource.

        Returns:
            Response object from the requests library.
        """

        logger.debug(f'Updating resource at URL: {self._store["base_url"]} with data: {data}')

        return self._do_request('PUT', params=json.dumps(data))
    # === End public methods ===

class FortiAPIClient(APIResource):
    """Client class for Fortinet API interactions."""

    # === Start Public Property methods ===
    @property
    def host(self) -> str:
        """Get the base URL of the Fortinet device API."""
        return self._store['host']
    # === End Public Property methods ===

    def __init__(self, type: FortiAPIDeviceType, host: str, 
                 log_level: LogLevel = LogLevel.WARNING, api_token: str = '',
                 username: str = '', password: str = '', verify_ssl: bool = True, 
                 timeout: int = 10, port: int = 443):
        """
        Initialize the FortiAPIClient.

        Args:
            type (FortiAPIDeviceType): Type of Fortinet device. 
            host (str): Hostname or IP Address for the device.
            api_token (str): API key for authentication.
            username (str): Username for authentication.
            password (str): Password for authentication.
            log_level (LogLevel): Logging level for the client. Defaults to WARNING.
            verify_ssl (bool): Confirm SSL certificates. Defaults to True.
            timeout (int): Timeout for requests in seconds. Defaults to 10.
            port (int): TCP port number. Defaults to 443.
        """

        logger.level = log_level.value

        self._store = {
            'type' : type,
            'api_token' : api_token,
            'username' : username,
            'password' : password,
            'verify_ssl' : verify_ssl,
            'base_url' : f"https://{host}:{port}{_API_URI_PREFIX[type]}",
            'timeout' : timeout,
            'port' : port,
        }

        # Set headers
        _headers = {'Authorization' : f'Bearer {api_token}',
                    'Content-Type' : 'application/json'}
        self._store['headers'] = _headers

        # Host cannot be blank or empty
        if host is not None and host != '':
            self._store['host'] = host
        else:
            raise ValueError('Host paramenter cannot be None or empty string.')
        
        # For type FortiOS, api_token is required
        if type == FortiAPIDeviceType.FORTIOS and (api_token is None or api_token == ''):
            raise ValueError('API key is required for FortiOS devices.')

        logger.debug(f"Initialized FortiAPIClient of type {type.value} at {host} ' \
                     'with log level {log_level.name}")
        
    def __repr__(self):
        return f'<FortiAPIClient type={self._type.value} host={self._host}>'