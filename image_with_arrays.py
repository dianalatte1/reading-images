import numpy as np
import cv2
# creating an image 600x600px
# black = np.zeros([6,6])
# print(black)

# showing the image
# cv2.imshow("En negro", black)
# cv2.waitKey(0)

# give us the row 1 [initialRow:finalRow]
# f_row = black[1:2]
# print(f_row)

# give us the column 1 [:,initialColumn:finalColumn]
# f_column = black[:,1:2]
# print(f_column)


# give us 2 rows and 2 columns 
# we assign 255 to this interval
# we need to change the width and height
# black[2:4,2:4] = 255
# print(black)
black = np.zeros([600,600])
black[200:400,200:400] = 255
print(black)
cv2.imshow("En negro", black)
cv2.waitKey(0)
