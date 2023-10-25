import cv2

def manipulate_webcam_feed():
    cam = cv2.VideoCapture(0)

    # Load the pre-trained Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        status, photo = cam.read()

        if not status:
            break

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(photo, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            # Crop the region of interest (ROI) around the face
            roi = photo[y:y+h, x:x+w]

            # Resize the ROI to the desired small window size (e.g., 150x150 pixels)
            roi_resized = cv2.resize(roi, (150, 150))

            # Display the small window with the face
            cv2.imshow("Face", roi_resized)

            # Replace the original frame's face region with the black and white version of the face
            roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            roi_gray_bgr = cv2.cvtColor(roi_gray, cv2.COLOR_GRAY2BGR)
            photo[y:y+h, x:x+w] = roi_gray_bgr

        # Display the modified frame with the original face region replaced by the black and white version
        cv2.imshow("MyPhoto", photo)

        # Break the loop if the 'Enter' key is pressed
        if cv2.waitKey(10) == 13:
            break

    # Release the webcam and close the OpenCV windows
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    manipulate_webcam_feed()