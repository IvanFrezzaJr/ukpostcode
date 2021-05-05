from uk_postcode import postcode

def IndexResource():
    return 'UK Postcode'


def CodeResource(code):
    ukpostcode = code

    ukpostcode_sanitised = str.upper(ukpostcode.replace(" ", ""))

    try:
        check = postcode.validate(ukpostcode_sanitised)
    except ValueError as e:
        return {"message": "UK Postcode not valid", "success": False}

    try:
        ukpostcode_formatted = postcode.format_(ukpostcode_sanitised)
    except ValueError as e:
        return {"message": "Format size should be between 5 and 7 with no space.", "success": False}

    return {"postcode": ukpostcode_formatted, "success": True}