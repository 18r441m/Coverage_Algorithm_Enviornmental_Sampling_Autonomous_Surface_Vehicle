import cv2

#read image
img_grey = cv2.imread('./map.jpg', cv2.IMREAD_GRAYSCALE)

# define a threshold, 128 is the middle of black and white in grey scale
thresh = 220

# threshold the image
img_binary = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)[1]
img = cv2.bitwise_not(img_binary)

#save image
cv2.imwrite('black-and-white.png',img) 