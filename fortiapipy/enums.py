"""
Enums for fortiapipy.
"""

__author__ = "The Network Entropologist"
__copyright__ = "(c) 2026 The Network Entropologist"
__version__ = "0.1.0"
__license__ = "Apache-2.0"

from enum import Enum

class FortiAPIDeviceType(Enum):
    """Enumeration of supported Fortinet device types."""
    FORTIOS = 'fortios'
