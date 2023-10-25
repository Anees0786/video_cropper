# video_cropper
OpenCV Webcam Feed Manipulation

This Python script uses the OpenCV library to capture video from the webcam, detect faces in real-time, and manipulate the webcam feed by replacing the detected faces with black and white versions. The face detection is performed using a pre-trained Haar Cascade classifier.

Prerequisites

Install the OpenCV library:

```bash
pip install opencv-python
```
Usage

Save the script with an appropriate name, for example, webcam_manipulation.py.

Run the script:

```bash
python webcam_manipulation.py
```
The webcam feed will open in a new window.

As faces are detected, they will be replaced by black and white versions in real-time.

Press the 'Enter' key to exit the program.

Caution

The script relies on the Haar Cascade classifier for face detection. Adjust the parameters in detectMultiScale for optimal face detection based on your environment.

The faces are replaced with a black and white version in real-time, providing a simple example of image manipulation.

Feel free to customize the script to add more sophisticated manipulations or features based on your requirements.

Note

The script uses the cv2.data.haarcascades path to access the pre-trained Haar Cascade classifier XML file. Ensure that the file haarcascade_frontalface_default.xml is available in this directory.

Consider extending the script to include additional image processing techniques or other features.
