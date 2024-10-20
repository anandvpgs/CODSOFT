
import cv2
import face_recognition
import numpy as np

def load_known_faces(known_faces_path):
    known_face_encodings = []
    known_face_names = []

    # Load known faces and their encodings
    # This is a placeholder. You would need to implement this function
    # to load images from a directory and encode them.

    return known_face_encodings, known_face_names

def detect_and_recognize_faces(image_path, known_face_encodings, known_face_names):
    # Load the image
    image = cv2.imread(image_path)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detect faces in the image
    face_locations = face_recognition.face_locations(rgb_image)
    face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

    # Loop through each face found in the image
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # Use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        # Draw a box around the face
        cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(image, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(image, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    return image

def main():
    # Load known faces
    known_face_encodings, known_face_names = load_known_faces("path/to/known_faces")

    # Detect and recognize faces in an image
    image_path = "path/to/test_image.jpg"
    result_image = detect_and_recognize_faces(image_path, known_face_encodings, known_face_names)

    # Display the result
    cv2.imshow("Face Detection and Recognition", result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()