"""Init and utils."""

from zope.i18nmessageid import MessageFactory

import logging


__version__ = "1.1.dev0"

PACKAGE_NAME = "collective.folderishcollection"

_ = MessageFactory(PACKAGE_NAME)

logger = logging.getLogger(PACKAGE_NAME)
