import cv2
import numpy as np

# STEP-1: Read any of the input images using cv2
img = cv2.imread('images/IMG_6726.jpg')

# Step-2: We scale the image to 600*800 size. We finalize on the specifications by trial methods.
img = cv2.resize(img, (600, 800))

# Step-3: convert input image to gray scale
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step-4: Thresholding an Image.
# Once the getimage is obtained, next step is to get a threshold image.
# If pixel value is greater than a threshold value, it is assigned  white value,
# else it is assigned black. To achieve this, we need cv2.threshold.
# In our case, let minVal = 190 and maxVal=255 for the threshold.
retval, thresholdedimage = cv2.threshold(imgray, 190, 255, cv2.THRESH_BINARY)

# Step-5: Contouring an image.
# Contouring helps us in finding the "white" image from te "black" background.
# RETR_TREE is a contour retrieval mode (We use this method as it helps us finding the complete hierarchy tree).
# CHAIN_APPROX_SIMPLE is an approximation method. (We use this method as it saves only 4 boundary points thereby saving a lot of memory).
contourimage, contours, hierarchy = cv2.findContours(thresholdedimage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Verify if we get the contour image as expected
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
cv2.imshow("image with contours", img)
cv2.imwrite("intermediateoutput/Contoured-image.PNG", img);
cv2.waitKey()

# ==============================Step-6: Detecting and analysing only the barcode pattern from the entire white paper. ============#

# Let's compute the area for each contour co-ordinates.
areas = [cv2.contourArea(contour) for contour in contours]
print (areas)
# #Index of the contour with max area.
max_area_index = np.argmax(areas)
print ("max_area_index", max_area_index)

# #Get the contour array(The one that represents the pattern in the white image)
patterncontour = contours[max_area_index]

# # #Get the minimal up-right bounding rectangle for our contour pattern.
# x, y, w, h = cv2.boundingRect(patterncontour)


# ================================ Step:7 - Analyse the rotation of the pattern.============#
d = {}
for contour in contours:
    # moments() help us in finding centers of all contours
    M = cv2.moments(contour)
    if M["m00"] == 0:
        continue
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    if d.get((cX, cY), 0):
        d[(cX, cY)] += 1  # If the coordinates already exits, we just increment the value
    else:
        d[(cX, cY)] = 1  # else add the list to the array.
three_hits = []
two_hits = []
for key in d:
    if d[key] == 3:
        three_hits.append(key)
    if d[key] == 2:
        two_hits.append(key)
# this will be used if the rotation of the barcode is necessary, for now I will use the rotation of the rectangle
if len(three_hits) == 3:
    pass
elif len(three_hits) == 2:
    pass
else:
    pass

# =============================Step-8:  Get the rotated angle of the pattern.=============#
# minAreaRect : gets the  minimum-area bounding the rotated rectangle for a specified contour
rect = cv2.minAreaRect(patterncontour)
print (rect)
# boxPoints: Helps us finding the four vertices of a rotated rect.
box = cv2.boxPoints(rect)

# int0: Converts the box vertices into integers.
box = np.int0(box)

cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
rotatedangle = rect[2]

print("Rotation Angle of the pattern: ", rotatedangle)
