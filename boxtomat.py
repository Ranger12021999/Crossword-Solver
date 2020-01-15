import numpy as np
import pytesseract as tess
import cv2
from PIL import Image

img = cv2.imread('box3.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
thresh2 = cv2.bitwise_not(thresh)

contours,hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, 1)

max_area = -1

# find contours with maximum area
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt,True), True)
    if len(approx) == 4:
        if cv2.contourArea(cnt) > max_area:
            max_area = cv2.contourArea(cnt)
            max_cnt = cnt
            max_approx = approx

row = int(input ("Enter Row number :"))
column =int(input ("Enter Column number :"))

# cut the crossword region, and resize it to a standard size of 130x130
x,y,w,h = cv2.boundingRect(max_cnt)
cross_rect = thresh2[y:y+h, x:x+w]
cross_rect = cv2.resize(cross_rect,(row*10,column*10))

#new_pts = np.float32([[0,0], [0,129],[129,129],[129,0]])
#old_pts = max_approx.reshape(4,2).astype('float32')
#M = cv2.getPerspectiveTransform(old_pts,new_pts)
#cross_rect = cv2.warpPerspective(thresh2,M,(130,130))

cross = np.zeros((row ,column))

# select each box, if number of white pixels is more than 50, it is white box
for i in range(row):
    for j in range(column):
        box = cross_rect[i*10:(i+1)*10, j*10:(j+1)*10]
        if cv2.countNonZero(box) > 50:
            cross.itemset((i,j),1)

print (cross)

# im = Image.open("box3.jpg")
# text = tess.image_to_string(im)
# print(text)