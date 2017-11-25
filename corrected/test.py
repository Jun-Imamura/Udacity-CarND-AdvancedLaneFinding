import cv2

img = cv2.imread("./test4.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
imgS = img[:,:,2]
cv2.imshow("test", imgS)
cv2.waitKey(-1)