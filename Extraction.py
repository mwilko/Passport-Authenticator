import re


def extract_passport_data(text):
    """
    Extract specific data fields from the OCR text.
    Fields:
    - Passport number
    - Name
    - Date of Birth
    """

    data = {}
    data['passport_number'] = re.findall(r'\b[A-Z0-9]{8,9}\b', text)
    data['name'] = re.findall(r'Name:\s*(.*)', text)
    data['dob'] = re.findall(r'Date of Birth:\s*(\d{2}/\d{2}/\d{4})', text)
    # Add more fields as necessary
    return data
