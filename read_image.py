import cv2
# loads an image from the specifed file
# syntax: cv2.imread(path,flag)
img = cv2.imread("tulips.jpg")
# imshow() is used to display an image in a window
# syntax: cv2.imshow(window_name, image)
cv2.imshow("Mostrar imagen", img)
# print(img)
# print(img.shape )
# converting to gray image
# cvtColor() is used to covert an image from one color space to another
# syntax: cv2.cvtColor(src, code[, dst[, dstCn]])
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# Displaying the image
cv2.imshow("Escala de grises", gray_img)
print(gray_img)
#waits for user to press any key 
cv2.waitKey(0)