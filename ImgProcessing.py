import cv2
from PIL import Image


def preprocess_image(image_path):
    """
    Preprocess the image to enhance its quality for better recognition.
    Steps:
    1. Load the image from the specified path.
    2. Convert the image to grayscale to simplify processing.
    3. Apply Gaussian blur to reduce noise and improve edge detection.
    """

    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    return blurred
