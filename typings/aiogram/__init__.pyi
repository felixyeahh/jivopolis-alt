"""
This type stub file was generated by pyright.
"""

import sys
import asyncio
import os
from . import bot, contrib, dispatcher, types, utils
from .bot import Bot
from .dispatcher import Dispatcher, filters, middlewares
from .utils import exceptions, executor, helper, markdown as md

if sys.version_info < (3, 7):
    ...
__all__ = ('Bot', 'Dispatcher', '__api_version__', '__version__', 'bot', 'contrib', 'dispatcher', 'exceptions', 'executor', 'filters', 'helper', 'md', 'middlewares', 'types', 'utils')
__version__ = ...
__api_version__ = ...
