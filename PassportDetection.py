import cv2


def detect_passport(image):
    """
    Detect the passport in the image.
    Steps:
    1. Apply Canny edge detection to find edges in the image.
    2. Find contours from the edge-detected image.
    3. Filter contours to find a quadrilateral (passport-like shape).
    4. Extract the region of interest (ROI) corresponding to the passport.
    """

    edged = cv2.Canny(image, 30, 150)
    contours, _ = cv2.findContours(
        edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        approx = cv2.approxPolyDP(
            contour, 0.02 * cv2.arcLength(contour, True), True)
        if len(approx) == 4:  # Assuming passport is a rectangle
            x, y, w, h = cv2.boundingRect(approx)
            passport = image[y:y+h, x:x+w]
            return passport
    return None
