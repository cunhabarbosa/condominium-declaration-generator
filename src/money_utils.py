"""Money formatting utility functions."""

from typing import Tuple
from num2words import num2words


def normalize_money_input(value: str | float | int) -> float:
    """
    Normalize money input into a float.

    Accepts:
    - 61.32
    - "61.32"
    - "61,32"
    - "61,32€"
    - "61.32€"
    """
    if isinstance(value, str):
        value = value.replace("€", "").replace(" ", "").replace(",", ".")
    return float(value)


def format_money(value: str | float | int) -> Tuple[str, str]:
    """
    Format a monetary value into:
    - Portuguese numeric format, e.g. '735,81€'
    - Portuguese full text, e.g. 'setecentos e trinta e cinco euros e oitenta e um cêntimos'
    """
    numeric_value = normalize_money_input(value)

    euros = int(numeric_value)
    cents = round((numeric_value - euros) * 100)

    value_str = (
        f"{numeric_value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        + "€"
    )

    euros_text = num2words(euros, lang="pt")
    cents_text = num2words(cents, lang="pt")

    euro_word = "euro" if euros == 1 else "euros"
    cent_word = "cêntimo" if cents == 1 else "cêntimos"

    value_text = f"{euros_text} {euro_word} e {cents_text} {cent_word}"
    return value_str, value_text