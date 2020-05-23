"""
kopia.config
===========

Base Configuration of Kopia.
"""

from pathlib import Path


SECRET_KEY = 'sskslfnsnk23erhovskj579'


PATH = Path.home() / '.kopia/'

DATABASE = PATH.resolve() / 'db.json'
LOG = PATH / 'log'
