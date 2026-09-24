from importlib.metadata import version, PackageNotFoundError
from .bzwwmo8qqsuhtj2ucdvu9xzyl import bzwwmo8qqsuhtj2ucdvu9xzyl as _

try:
    __version__ = version("bzwwmo8qqsuhtj2ucdvu9xzyl")
except PackageNotFoundError:
    __version__ = "unknown"

__all__ = ["_", "__version__"]
