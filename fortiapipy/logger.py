"""
# Logger module for FortiAPIPy.

This module sets up logging for the FortiAPIPy library.
"""

# Python core imports
import logging
from enum import Enum

class LogLevel(Enum):
    """Enumeration for log levels."""
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

class FortiAPILogger:
    """Logger class for FortiAPIPy."""

    # === Start Public Properties ===

    @property
    def level(self) -> int:
        """Get the current logging level."""
        return self._logger.level
    @level.setter
    def level(self, level: int):
        """Set the logging level."""
        self._logger.setLevel(level)
        for handler in self._logger.handlers:
            handler.setLevel(level)
        
    # === End Public Properties

    def __init__(self, level: LogLevel, format: str = ''):
        """
        Initialize the FortiAPILogger.

        Format defaults to `%(asctime)s - %(name)s - %(levelname)s - %(message)s`
        
        Args:
            name (str): Name of the logger.
            level (LogLevel): Logging level.
            format (str, optional): Logging format.
        """

        self._logger = logging.getLogger('fortiapipy')
        self._logger.setLevel(level.value)
        self._format = format if format else '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

        # Create console handler with the specified log level
        ch = logging.StreamHandler()
        ch.setLevel(level.value)

        # Create formatter and add it to the handler
        formatter = logging.Formatter(self._format)
        ch.setFormatter(formatter)

        # Add the handler to the logger
        self._logger.addHandler(ch)

    # === Start Helper Methods ===

    def debug(self, msg: str):
        """Log a debug message."""
        self._logger.debug(msg)

    def info(self, msg: str):
        """Log an info message."""
        self._logger.info(msg)

    def warning(self, msg: str):    
        """Log a warning message."""
        self._logger.warning(msg)

    def error(self, msg: str):
        """Log an error message."""
        self._logger.error(msg)

    # === End Helper Methods ===
