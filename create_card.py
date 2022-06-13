import cv2

img = cv2.imread("poster.jpg")
rocket = img[120:360,400:500]
# this line put the image in this position
img[0:240,400:500] = rocket
# img[0:240,0:100] = rocket

cv2.imshow("output",img)
cv2.waitKey(0)