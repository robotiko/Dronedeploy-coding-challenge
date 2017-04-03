# Dronedeply-coding-challenge

## Challenge-1


This zip file https://www.dropbox.com/s/afrfye7hvra7wvy/images.zip?dl=0 contains a number of images taken from different positions and orientations with an iPhone 6. Each image is the view of a pattern on a flat surface. The original pattern that was photographed is 8.8cm x 8.8cm and is included in the zip file. Write a Python program that will visualize (i.e. generate a graphic) where the camera was when each image was taken and how it was posed, relative to the pattern.

You can assume that the pattern is at 0,0,0 in some global coordinate system and are thus looking for the x, y, z and yaw, pitch, roll of the camera that took each image. Please submit a link to a Github repository contain the code for your solution. Readability and comments are taken into account too. You may use 3rd party libraries like OpenCV and Numpy.
## Approach:

1. Installed Python,OpenCV and the Numpy libraries.
2. Below are the steps involved in solving the coding challenge:

 - Read any of the input images using cv2. I chose (IMG_6726.jpg).
 - Later ,we scale the image to 600*800 size. We finalize on the specifications by trial methods.
 - Convert input image to gray scale.
 - Thresholding an Image using THRESH_BINARY to classify image into white and black.
 - Contouring an image.
 - Detecting and analysing only the barcode pattern from the entire white paper.
 - Analyse the rotation of the pattern.
 - Get the rotated angle of the pattern.
 - Get the the distance between contour corner and bounded rectangle.

 Each of these steps are heavily commented in the "visualize.py" file along with the usage of inbuilt CV library functions.

 Please note that this repository is PRIVATE as of now and I have only shared it with authorized github users.
 Let me know if the access is to be given to any other user(s) or if the repo has to be made public.





