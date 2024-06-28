import cv2
import face_recognition


def extract_face_from_passport(image):
    """
    Detect and extract the face from the passport image.
    """
    # Detect faces in the image
    face_locations = face_recognition.face_locations(image)

    if len(face_locations) == 0:
        print("No face detected in the passport image.")
        return None

    # Assume the first face detected is the passport photo
    top, right, bottom, left = face_locations[0]
    face_image = image[top:bottom, left:right]

    return face_image


def capture_real_time_face():
    """
    Capture real-time video and detect faces.
    """
    video_capture = cv2.VideoCapture(0)  # Open the webcam (device 0)

    while True:
        ret, frame = video_capture.read()  # Capture a single frame from the webcam

        if not ret:
            print("Failed to capture video frame.")
            break

        # Convert the frame from BGR (OpenCV format) to RGB (face_recognition format)
        rgb_frame = frame[:, :, ::-1]

        # Detect faces in the frame
        face_locations = face_recognition.face_locations(rgb_frame)

        for (top, right, bottom, left) in face_locations:
            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Break the loop when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the window
    video_capture.release()
    cv2.destroyAllWindows()

    if len(face_locations) == 0:
        print("No face detected in the video frame.")
        return None

    # Assume the first face detected is the user's face
    top, right, bottom, left = face_locations[0]
    user_face_image = rgb_frame[top:bottom, left:right]

    return user_face_image


def compare_faces(passport_face, user_face):
    """
    Compare the extracted face from the passport with the user's face captured from the webcam.
    """
    # Encode the faces to create face encodings
    passport_face_encoding = face_recognition.face_encodings(passport_face)[0]
    user_face_encoding = face_recognition.face_encodings(user_face)[0]

    # Compare the faces
    results = face_recognition.compare_faces(
        [passport_face_encoding], user_face_encoding)

    return results[0]  # Return True if the faces match, otherwise False
