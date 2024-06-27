def validate_data(data):
    """
    Validate the extracted data to ensure it meets expected patterns.
    """

    if not data['passport_number']:
        return False
    if not data['name']:
        return False
    if not data['dob']:
        return False
    return True
