"""App declaration for nautobot_waveplan."""

# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata

from nautobot.apps import NautobotAppConfig

__version__ = metadata.version(__name__)


class WaveplanConfig(NautobotAppConfig):
    """App configuration for the nautobot_waveplan app."""

    name = "nautobot_waveplan"
    verbose_name = "Waveplan"
    version = __version__
    author = "James Williams"
    description = "Waveplan."
    base_url = "waveplan"
    required_settings = []
    min_version = "2.0.0"
    max_version = "2.9999"
    default_settings = {}
    caching_config = {}
    docs_view_name = "plugins:nautobot_waveplan:docs"


config = WaveplanConfig  # pylint:disable=invalid-name
