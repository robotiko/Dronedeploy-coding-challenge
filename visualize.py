import cv2

# STEP-1: Read any of the input images using cv2
img = cv2.imread('images/IMG_6723.jpg')

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
cv2.waitKey()
