import cv2
import numpy as np

image = cv2.imread('testSquare.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original image', image)
cv2.imshow('Gray image', gray)
# gray scale

edges = cv2.Canny(gray, 25, 240)

# Write image back to disk.
cv2.imshow('result.jpg', edges)
# # edge deteaction
# # todo:
#
# params = cv2.SimpleBlobDetector_Params()
#
# # Change thresholds
# params.minThreshold = 10
# params.maxThreshold = 200
#
# # Filter by Area.
# params.filterByArea = True
# params.minArea = 1500
#
# # Filter by Circularity
# params.filterByCircularity = True
# params.minCircularity = 0.1
#
# # Filter by Convexity
# params.filterByConvexity = True
# params.minConvexity = 0.87
#
# # Filter by Inertia
# params.filterByInertia = True
# params.minInertiaRatio = 0.01
#
# # Create a detector with the parameters
#
# detector = cv2.SimpleBlobDetector(params)
# # else:
# #     detector = cv2.SimpleBlobDetector_create(params)
# keypoints = detector.detect(image)
#
# # Draw detected blobs as red circles.
# # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
# im_with_keypoints = cv2.drawKeypoints(image, keypoints, image)

# sadfasdf
img = cv2.imread('/home/uco1518/PycharmProjects/crossword2/testSquare.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 25, 200)
cv2.imshow('sdsdf.jpg', edges)
#
# minLineLength = 10
# maxLineGap = 10
# lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength, maxLineGap)
# for x1, y1, x2, y2 in lines[0]:
#     cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0))
#
# cv2.imshow('houghlines3.jpg', img)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# image = cv2.imread("/home/uco1518/PycharmProjects/crossword2/boxes.jpeg", 1)
#
# # red color boundaries [B, G, R]
# lower = [1, 0, 20]
# upper = [60, 40, 200]
#
# # create NumPy arrays from the boundaries
# lower = np.array(lower, "uint8")
# upper = np.array(upper, "uint8")

# find the colors within the specified boundaries and apply
# the mask
# mask = cv2.inRange(image, lower, upper)
# output = cv2.bitwise_and(image, image, mask)
#
# ret, thresh = cv2.threshold(mask, 40, 255, 0)
# im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#
# if len(contours) != 0:
#     # draw in blue the contours that were founded
#     cv2.drawContours(output, contours, -1, 255, 3)
#
#     # find the biggest area
#     c = max(contours, cv2.contourArea)
#
#     x, y, w, h = cv2.boundingRect(c)
#     # draw the book contour (in green)
#     cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
# # show the images
# cv2.imshow("Result", np.hstack([image, output]))
#
# cv2.waitKey(0)
