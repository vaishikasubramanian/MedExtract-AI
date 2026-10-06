"""MedExtract-AI – AI-powered medical document classification and extraction engine.

Top-level convenience imports::

    from src import MedExtractEngine, MedExtractSettings, settings, setup_logging
"""

from src.config import MedExtractSettings, get_settings, settings
from src.logging_config import setup_logging

__all__ = [
    "MedExtractSettings",
    "get_settings",
    "settings",
    "setup_logging",
]
