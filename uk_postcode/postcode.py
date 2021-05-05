"""
Write a library that supports validating and formatting post codes for UK. 
The details of which post codes are valid and which are the parts they consist of can be found at https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting. 
The API that this library provides is your choice.
"""

import re


def validate(ukpostcode:str)-> bool:

    if len(ukpostcode) > 7:
        raise ValueError("UK Postcode should have less than 7 characters")

    if len(ukpostcode) < 5:
        raise ValueError("UK Postcode should have more than 5 characters")

    validated = _simple(ukpostcode)

    if not validated:
        validated = _special(ukpostcode)

    if not validated:
        return False

    return True


def format_(ukpostcode:str)-> str:
    """ format uk postcode insering space character in the correct place
    """

    if len(ukpostcode) == 5:
        return ukpostcode[:2] + " " + ukpostcode[2:]
    if len(ukpostcode) == 6:
        return ukpostcode[:3] + " " + ukpostcode[3:]
    if len(ukpostcode) == 7:
        return ukpostcode[:4] + " " + ukpostcode[4:]

    raise ValueError("Uk postcode size not accepted. The size should be between 5 and 7 with no space.")


def _simple(ukpostcode:str) -> str:
    """ check uk postcode
    """
    if not isinstance(ukpostcode, str):
        raise TypeError("Value should be a string")

    m = re.search(r"^[A-Z]{1,2}[0-9][A-Z0-9]? ?[0-9][A-Z]{2}$", ukpostcode)
    if not m:
        return False
    
    return True


def _special(ukpostcode:str) -> str:
    """ check postcode special cases

    E.g. https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Special_cases

    """
    if not isinstance(ukpostcode, str):
        raise TypeError("Value should be a string")

    pattern = r"^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) "
    pattern += r"?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]"
    pattern += r"?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$"
    m = re.search(pattern, ukpostcode)
    if not m:
        return False
    
    return True
