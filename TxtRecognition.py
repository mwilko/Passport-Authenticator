import pytesseract


def extract_text(image):
    """
    Extract text from the image using Optical Character Recognition (OCR).
    """

    text = pytesseract.image_to_string(image)
    print(text)
    return text
