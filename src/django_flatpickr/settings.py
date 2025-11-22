"""Package settings."""
import functools
from typing import Any, Dict, Optional

from django.conf import settings as django_settings
from pydantic import BaseModel, Field

from .schemas import FlatpickrOptions, ThemeEnum


def _django_settings_source() -> Dict[str, Any]:
    """Return djsettings override dictionary, if any."""
    return getattr(django_settings, "DJANGO_FLATPICKR", {})


class DjangoFlatpickrSettings(BaseModel):
    """Package settings to customize inputs.

    This implementation uses Pydantic v2's BaseModel directly instead of
    pydantic.v1 BaseSettings, to ensure compatibility with Python 3.14+.
    """

    theme_name: Optional[ThemeEnum] = None
    theme_url: Optional[str] = None
    template_name: Optional[str] = None
    attrs: Dict[str, str] = {}
    options: FlatpickrOptions = FlatpickrOptions()
    flatpickr_cdn_url: str = "https://cdn.jsdelivr.net/npm/flatpickr@4.6.13/dist/"
    app_static_url: str = (
        "https://cdn.jsdelivr.net/gh/monim67/django-flatpickr@2.0.0/src/"
        "django_flatpickr/static/django_flatpickr/"
    )
    debug: bool = Field(default_factory=lambda: getattr(django_settings, "DEBUG", True))


@functools.lru_cache(maxsize=1)
def get_django_flatpickr_settings() -> DjangoFlatpickrSettings:
    """Initialize and return DjangoFlatpickrSettings."""
    return DjangoFlatpickrSettings(**_django_settings_source())
