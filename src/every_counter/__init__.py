# read version from installed package
from importlib.metadata import version
__version__ = version("every_counter")

from every_counter import every_counter

print(every_counter.__version__)