import numpy as np
import cv2
import random
from utils.utils import get_rgb, convert_list_to_rect_object

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,500)
fontScale              = .5
fontColor              = (255,255,255)
lineType               = 1

def get_test_data():
	print 'prepare test_3 data'
	products_rect = [
			[50, 200, 140, 330],
			[140, 200, 230, 330],
			[310, 200, 380, 330],
			[381, 200, 440, 330],
			# [441, 200, 520, 330],
			]

	labels_rect = [
			[150, 350, 240, 400],
			[350, 350, 450, 400],
			# [385, 350, 460, 400]
			]

	img = np.zeros((500, 500, 3), np.uint8)

	# bounding box
	cv2.rectangle(img, (50, 50), (450, 450), (get_rgb()), 0)

	# products
	for each in products_rect:
		cv2.rectangle(img, (each[0],  each[1]), (each[2], each[3]), (get_rgb()), -1)

	# labels
	for each in labels_rect:
		cv2.rectangle(img, (each[0],  each[1]), (each[2], each[3]), (get_rgb()), -1)


	# write to output file
	cv2.imwrite('./panos/fp_test_3.jpg', img)

	return convert_list_to_rect_object(products_rect), convert_list_to_rect_object(labels_rect), \
		products_rect, labels_rect

# test_2()