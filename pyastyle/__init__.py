try:
    from ._win32.pyastyle import *
except ImportError:
    from ._win64.pyastyle import *
