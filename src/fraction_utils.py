"""Fraction mapping utility functions."""

from typing import Dict, Tuple


def build_fraction_mapping() -> Dict[str, Tuple[int, int]]:
    """
    Build the fraction mapping for the building.

    Rules:
    - Floor 1: apartments 1..7
    - Floors 2..5: apartments 1..8

    Fraction letters are assigned sequentially:
    A, B, C, ...
    """
    mapping: Dict[str, Tuple[int, int]] = {}
    current_letter_code = ord("A")

    for floor in range(1, 6):
        max_apartment = 7 if floor == 1 else 8
        for apartment in range(1, max_apartment + 1):
            fraction = chr(current_letter_code)
            mapping[fraction] = (floor, apartment)
            current_letter_code += 1

    return mapping


FRACTION_MAP = build_fraction_mapping()


def get_fraction_info(fraction: str) -> Tuple[str, str, str]:
    """
    Return fraction, floor, and apartment.

    Example:
        Input: 'B'
        Output: ('B', '1', '2')
    """
    fraction = fraction.strip().upper()

    if fraction not in FRACTION_MAP:
        raise ValueError(f"Unknown fraction: {fraction}")

    floor, apartment = FRACTION_MAP[fraction]
    return fraction, str(floor), str(apartment)
