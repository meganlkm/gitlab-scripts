""" mygitlab init """
from os import path

__version__ = '0.0.3'
__all__ = [
    'config_file',
    'package_dir',
    'helper'
]

package_dir = path.abspath(path.dirname(__file__))
config_file = path.join(path.dirname(package_dir), 'config.yml')

from . import helper
