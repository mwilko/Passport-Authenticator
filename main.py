import Extraction as Extract
import ImgProcessing as ImgProcess
import PassportDetection as PassDetect
import TxtRecognition as TxtRecog
import Validation as Valid
import FaceRecognition as FaceRecog

# Path to the passport image
image_path = 'passport_example1.jpeg'

# Preprocess the image
preprocessed_image = ImgProcess.preprocess_image(image_path)

# Detect the passport in the image
passport_image = PassDetect.detect_passport(preprocessed_image)

if passport_image is not None:
    # Extract text from the detected passport
    print("Passport detected.")
    text = TxtRecog.extract_text(passport_image)

else:
    print("Passport not detected.")

if text:
    # Extract and validate data from the OCR text
    passport_data = Extract.extract_passport_data(text)
    if Valid.validate_data(passport_data):
        # Print the extracted and validated data
        print("Extracted Data:", passport_data)
    else:
        # Print a message if data validation fails
        print("Data validation failed.")
else:
    # Print a message if text extraction fails
    print("Text extraction failed. \nText: ", text)

passport_face = FaceRecog.extract_face_from_passport(passport_image)

if passport_face is not None:
    # Capture real-time video and detect the user's face
    user_face = FaceRecog.capture_real_time_face()

    if user_face is not None:
        # Compare the passport face with the user's face
        is_match = FaceRecog.compare_faces(passport_face, user_face)

        if is_match:
            print("The face from the passport matches the real-time face.")
        else:
            print("The face from the passport does not match the real-time face.")
    else:
        print("No face detected in the real-time video.")
else:
    print("No face detected in the passport image.")
