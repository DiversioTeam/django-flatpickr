"""Datastructures of the package."""

from enum import Enum
from typing import Any, Dict, List, NoReturn, Optional

from pydantic import BaseModel, Extra, Field, validator

from typing_extensions import TypeAlias

InputAttrs: TypeAlias = Dict[str, Any]


class ThemeEnum(str, Enum):
    """Flatpickr theme options."""

    dark = "dark"
    material_blue = "material_blue"
    material_green = "material_green"
    material_red = "material_red"
    material_orange = "material_orange"
    airbnb = "airbnb"
    confetti = "confetti"


class FlatpickrOptions(BaseModel, extra=Extra.allow):
    """Flatpickr options to create flatpickr instance."""

    allowInput: Optional[bool] = None
    allowInvalidPreload: Optional[bool] = None
    altFormat: Optional[str] = None
    altInput: bool = True
    altInputClass: Optional[str] = None
    ariaDateFormat: Optional[str] = None
    clickOpens: Optional[bool] = None
    dateFormat: Optional[str] = None
    defaultDate: Optional[str] = None
    defaultHour: Optional[int] = Field(default=None, ge=0, le=23)
    defaultMinute: Optional[int] = Field(default=None, ge=0, le=59)
    disable: Optional[List[str]] = None
    disableMobile: Optional[bool] = None
    enable: Optional[List[str]] = None
    enableSeconds: Optional[bool] = None
    enableTime: Optional[bool] = None
    hourIncrement: Optional[int] = Field(default=None, ge=1, le=12)
    inline: Optional[bool] = None
    locale: Optional[str] = None
    maxDate: Optional[str] = None
    minDate: Optional[str] = None
    minuteIncrement: Optional[int] = Field(default=None, ge=0, le=59)
    mode: Optional[str] = None
    monthSelectorType: Optional[str] = None
    nextArrow: Optional[str] = None
    noCalendar: Optional[bool] = None
    position: Optional[str] = None
    prevArrow: Optional[str] = None
    shorthandCurrentMonth: Optional[bool] = None
    showMonths: Optional[int] = Field(default=None, ge=1, le=12)
    static: Optional[bool] = None
    time_24hr: Optional[bool] = None
    weekNumbers: Optional[bool] = None
    wrap: bool = True

    @validator("mode")
    def _disallow_mode(cls, v: str) -> NoReturn:
        raise ValueError(
            "Option mode is reserved and always set to static."
            " For range mode see how to use range picker in django-flatpickr docs"
        )

    @validator("dateFormat")
    def _disallow_dateFormat(cls, v: str) -> NoReturn:
        raise ValueError(
            "Option dateFormat is reserved and always set to Y-m-d."
            " Use altFormat to set date format selected by calendar"
        )

    @validator("altInput")
    def _disallow_altInput(cls, v: str) -> NoReturn:
        raise ValueError("Option altInput is reserved and always set to True.")

    @validator("wrap")
    def _disallow_wrap(cls, v: str) -> NoReturn:
        raise ValueError("Option wrap is reserved and always set to True.")

    @validator("enableTime")
    def _disallow_enableTime(cls, v: str) -> NoReturn:
        raise ValueError("Option enableTime is reserved and set based on widget used.")

    @validator("noCalendar")
    def _disallow_noCalendar(cls, v: str) -> NoReturn:
        raise ValueError("Option noCalendar is reserved and set based on widget used.")
