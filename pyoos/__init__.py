__version__ = '0.6.3-dev'

# Package level logger
import logging
try:
    # Python >= 2.7
    from logging import NullHandler
except ImportError:
    # Python < 2.7
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass
logger = logging.getLogger("pyoos")
logger.addHandler(logging.NullHandler())
