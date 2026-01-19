"""
Fortinet API client library for Python.

This is the core module that provides the main functionality for interacting 
with Fortinet devices via their APIs.
"""

__author__ = "The Network Entropologist"
__copyright__ = "(c) 2026 The Network Entropologist"
__version__ = "0.1.0"
__license__ = "Apache-2.0"


import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.WARNING)

SUPPORTED_FORTINET_DEVICES = {
    'fortios': 'FortiOS Powered Devices',
}
"""dict: A list of currently supported Fortinet device types."""

