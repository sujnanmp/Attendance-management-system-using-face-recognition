import cv2
import face_recognition
import numpy as np
import os
import pandas as pd
from datetime import datetime

# Create a pandas DataFrame to store attendance data
attendance_df = pd.DataFrame(columns=['Name', 'Time'])

# Create a list of known face encodings and their names
known_face_encodings = []
known_names = []

# Add your known faces and names to the lists
image = face_recognition.load_image_file('photos/photos/deepika.jpeg')
encoding = face_recognition.face_encodings(image)[0]
known_face_encodings.append(encoding)
known_names.append('deepika')

image = face_recognition.load_image_file('photos/photos/Myook.jpeg')
encoding = face_recognition.face_encodings(image)[0]
known_face_encodings.append(encoding)
known_names.append('Mayook')

image = face_recognition.load_image_file('photos/photos/scarlet.jpeg')
encoding = face_recognition.face_encodings(image)[0]
known_face_encodings.append(encoding)
known_names.append('scarlet')

image = face_recognition.load_image_file('photos/photos/sujnan.jpeg.jpg')
encoding = face_recognition.face_encodings(image)[0]
known_face_encodings.append(encoding)
known_names.append('sujnan')

image = face_recognition.load_image_file('photos/photos/devraj.jpeg.jpg')
encoding = face_recognition.face_encodings(image)[0]
known_face_encodings.append(encoding)
known_names.append('devraj')

image = face_recognition.load_image_file('photos/photos/nagarathna.jpeg.jpg')
encoding = face_recognition.face_encodings(image)[0]
known_face_encodings.append(encoding)
known_names.append('nagarathna')

image = face_recognition.load_image_file('photos/photos/venkatesh.jpeg.jpg')
encoding = face_recognition.face_encodings(image)[0]
known_face_encodings.append(encoding)
known_names.append('venkatesh')

image = face_recognition.load_image_file('photos/photos/wsmith.jpeg')
encoding = face_recognition.face_encodings(image)[0]
known_face_encodings.append(encoding)
known_names.append('wsmith')

# Add more faces and names as necessary

# Initialize the video capture object
cap = cv2.VideoCapture(0)

# Initialize the list to keep track of the names that have already been added to the attendance DataFrame
marked_names = []

while True:
    # Capture frame-by-frame
    ret, frame = cap.rade()

    # Convert the frame from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces in the current frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face in the current frame
    for face_encoding in face_encodings:
        # See if the face is a match for any known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        # If there is a match and the person has not already been marked present, add the person's name and time to the attendance DataFrame
        if True in matches:
            match_index = matches.index(True)
            name = known_names[match_index]
            if name not in marked_names:
                time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                attendance_df = pd.concat([attendance_df, pd.DataFrame({'Name': [name], 'Time': [time]})], ignore_index=True)
                marked_names.append(name)

    # Display the resulting frame
    cv2.imshow('Attendance Management System', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture object and close all windows
cap.release()
cv2.destroyAllWindows()

# Save the attendance DataFrame to an Excel sheet
attendance_df.to_excel('attendance.xlsx', index=False)
