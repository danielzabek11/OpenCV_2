import cv2
import random

img = cv2.imread('assets/landscape.jpg', -1)


#print(img.shape)
#Outputs (1001, 1500, 3) - (Number of rows, Number of columns, Amount of values representing each pixel 'RGB' in OpenCV 'BGR')

#print(img[500][50:700])
#In row 500 check pixels between 50-700

#print(img[500][50])
#Values of one specific pixel

#for i in range(100):    
#    for j in range(img.shape[1]):
#        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

#Change first 100 rows (height of image) and all columns in them (width of image) to random pixel values

img_part = img[500:700, 600:900]
#Copy rows from <500 ; 700) and columns from <600:900)

img[500:700, 200:500] = img_part
#Paste our copied part to specified place (dimensions need to be the same there we put our copied part in rows 500-700 and columns 200-500 of our original image)
 
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()