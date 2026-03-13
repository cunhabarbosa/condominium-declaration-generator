"""Date-related utility functions."""

from datetime import datetime
from typing import Tuple


MONTHS_PT = {
    1: "janeiro",
    2: "fevereiro",
    3: "março",
    4: "abril",
    5: "maio",
    6: "junho",
    7: "julho",
    8: "agosto",
    9: "setembro",
    10: "outubro",
    11: "novembro",
    12: "dezembro",
}


def parse_date(date_str: str | None = None) -> datetime:
    """
    Parse a date string into a datetime object.

    Supported formats:
    - dd/mm/yyyy
    - yyyy-mm-dd

    If no date is given, today's date is used.
    """
    if not date_str:
        return datetime.today()

    for fmt in ("%d/%m/%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue

    raise ValueError(
        f"Invalid date format: {date_str}. Use dd/mm/yyyy or yyyy-mm-dd."
    )


def generate_date(date_str: str | None = None) -> Tuple[str, str]:
    """
    Generate a Portuguese long date and a short numeric date.

    Returns:
        tuple[str, str]:
            - long date, e.g. '12 de março de 2026'
            - short date, e.g. '12/03/2026'
    """
    date_obj = parse_date(date_str)
    date_long = f"{date_obj.day} de {MONTHS_PT[date_obj.month]} de {date_obj.year}"
    date_short = date_obj.strftime("%d/%m/%Y")
    return date_long, date_short
